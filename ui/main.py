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

st.divider()
st.header("商品の検索 (ID指定)")
# (ここに検索フォームを実装 - Task 4)

st.divider()
st.header("このセッションで登録した商品")
st.warning("注意: この一覧はブラウザをリロードすると消えます。")
# (ここに一覧表示を実装 - Task 3)
