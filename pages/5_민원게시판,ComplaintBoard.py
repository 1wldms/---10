import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

st.set_page_config(page_title="민원 리스트", page_icon="📝", layout="wide")
st.title("📝 민원 리스트 및 공감하기")

SERVICE_ACCOUNT_FILE = "./credentials.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build("sheets", "v4", credentials=credentials)

def read_sheet():
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range="시트1!A:F"
        ).execute()
        return result.get("values", [])
    except HttpError as error:
        st.error(f"❗ 시트 읽기 오류: {error}")
        return []

def write_sheet(data):
    try:
        body = {"values": data}
        service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range="시트1!A1",
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()
    except HttpError as error:
        st.error(f"❗ 시트 쓰기 오류: {error}")

def rerun():
    st.session_state["rerun_trigger"] = not st.session_state.get("rerun_trigger", False)
    st.stop()

data = read_sheet()

if data:
    headers = data[0]
    complaints = data[1:]

    st.markdown("### 📋 등록된 민원 목록")

    for idx, row in enumerate(complaints):
        if len(row) < 5:
            continue

        date, name, content, lat, lon = row[:5]
        sympathy = int(row[5]) if len(row) >= 6 and row[5].isdigit() else 0

        key_session = f"sympathy_val_{idx}"
        key_button = f"sympathy_btn_{idx}"

        if key_session not in st.session_state:
            st.session_state[key_session] = sympathy

        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
            ---
            **📅 날짜**: {date}  
            **✍ 작성자**: {name}  
            **📝 내용**: {content}  
            **📌 위치**: ({lat}, {lon})
            """)

        with col2:
            if st.button(f"👍 {st.session_state[key_session]}", key=key_button):
                st.session_state[key_session] += 1
                if len(complaints[idx]) < 6:
                    complaints[idx].append(str(st.session_state[key_session]))
                else:
                    complaints[idx][5] = str(st.session_state[key_session])
                write_sheet([headers] + complaints)
                st.rerun()
else:
    st.warning("등록된 민원이 없습니다.")

st.markdown("---")
st.caption("정보프로그래밍심화 기말과제 | 만든이: 민지은 박하람")