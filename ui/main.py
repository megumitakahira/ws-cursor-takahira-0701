import httpx
import pandas as pd
import streamlit as st

# APIのエンドポイント
API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="商品管理", layout="wide")

st.title("商品管理ダッシュボード")

# セッション内で登録した商品を保持するリストを初期化
if "session_items" not in st.session_state:
    st.session_state.session_items = []

# --- 画面レイアウト ---
st.divider()
st.header("商品の登録")
# (ここに登録フォームを実装 - Task 2)
with st.form("create_item_form", clear_on_submit=True):
    item_name = st.text_input("商品名", key="item_name_input")
    item_price = st.number_input("価格", min_value=0.01, step=0.01, key="item_price_input")
    submit_button = st.form_submit_button("商品を登録する")

if submit_button:
    if not item_name:
        st.error("商品名を入力してください。")
    elif not item_price:
        st.error("価格を入力してください。")
    else:
        try:
            response = httpx.post(
                f"{API_BASE_URL}/items",
                json={"name": item_name, "price": item_price},
                timeout=5,
            )
            response.raise_for_status()  # Raises an exception for 4xx/5xx responses
            new_item = response.json()
            st.success(f"✅ 商品「{new_item['name']}」を登録しました！")
            # (ここに一覧への追加処理を実装 - Task 3)
            st.session_state.session_items.insert(0, new_item)
        except httpx.RequestError as e:
            st.error(f"❌ APIサーバーへの接続に失敗しました: {e}")
        except httpx.HTTPStatusError as e:
            st.error(f"❌ 登録に失敗しました: {e.response.json().get('detail', e.response.text)}")

st.divider()
st.header("商品の検索 (ID指定)")
# (ここに検索フォームを実装 - Task 4)
search_id = st.number_input("商品ID", min_value=1, step=1, key="search_id_input")
search_button = st.button("検索")

if search_button:
    try:
        response = httpx.get(f"{API_BASE_URL}/items/{search_id}", timeout=5)
        response.raise_for_status()
        st.success(f"商品 (ID: {search_id}) が見つかりました。")
        st.json(response.json())
    except httpx.RequestError as e:
        st.error(f"❌ APIサーバーへの接続に失敗しました: {e}")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            st.warning(f"⚠️ 商品 (ID: {search_id}) は見つかりませんでした。")
        else:
            st.error(f"❌ 検索に失敗しました: {e.response.json().get('detail', e.response.text)}")

st.divider()
st.header("このセッションで登録した商品")
st.warning("注意: この一覧はブラウザをリロードすると消えます。")
# (ここに一覧表示を実装 - Task 3)
if st.session_state.session_items:
    df = pd.DataFrame(st.session_state.session_items)
    st.dataframe(
        df,
        column_config={
            "id": "ID",
            "name": "商品名",
            "price": "価格",
            "created_at": "登録日時",
        },
        hide_index=True,
    )
else:
    st.info("このセッションではまだ商品が登録されていません。")
