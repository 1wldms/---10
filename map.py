import streamlit as st
import folium
from streamlit_folium import st_folium
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"


st.title('📍민원 접수')
st.sidebar.markdown('# 민원')

latitude = 37.5636201943343
longitude = 126.93774785651566

m = folium.Map(location=[latitude, longitude], zoom_start=16)
map_data = st_folium(m, width=725)


def google_sheet_upload(spreadsheet_id, range_name, values):
    creds, _ = default(scopes=SCOPES)
    
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": values}
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def google_sheet_read(spreadsheet_id, range_name):
    creds, _ = default(scopes=SCOPES)
    
    try:
        service = build("sheets", "v4", credentials=creds)
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        return result.get("values",[])
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []


clicked_location = map_data.get("last_clicked")

# 민원 입력 폼
if clicked_location:
    lat = clicked_location["lat"]
    lon = clicked_location["lng"]
    st.success(f"선택한 위치: 위도 {lat:.5f}, 경도 {lon:.5f}")

    with st.form("complaint_form"):
        name = st.text_input("민원 작성자", max_chars=20)
        content = st.text_area("민원 내용", height=150)
        date = st.date_input("📅 민원 날짜")
        submitted = st.form_submit_button("민원 제출")

        if submitted:
            if name and content:
                values = [[str(date), name, content, lat, lon]]
                result = None
                try:
                    creds, _ = default(scopes=SCOPES)
                    service = build("sheets", "v4", credentials=creds)
                    body = {"values": values}
                    result = service.spreadsheets().values().append(
                        spreadsheetId=SPREADSHEET_ID,
                        range="시트1!A:E",  # 날짜, 이름, 내용, 위도, 경도
                        valueInputOption="USER_ENTERED",
                        insertDataOption="INSERT_ROWS",
                        body=body
                    ).execute()
                    st.success("민원이 성공적으로 제출되었습니다!")
                except HttpError as error:
                    st.error(f"Google Sheet 오류: {error}")
            else:
                st.warning("이름과 민원 내용을 모두 입력해주세요.")
else:
    st.info("먼저 지도에서 위치를 클릭해주세요.")



# name = st.text_input('이름을 입력하세요.', max_chars=10)
# context = st.text_area('민원 내용을 입력하세요.', height = 제한 숫자)
# my_date = st.date_input('민원 날짜를 입력하세요.')
# submit = st.form_submit_button
# google_sheet_upload(SPREADSHEET_ID, 시트 range_name, [[name, context]])