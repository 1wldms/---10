import streamlit as st
import pydeck as pdk
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"


st.title('📍민원 접수')
st.sidebar.markdown('# 민원')

latitude = 37.5636201943343
longitude = 126.93774785651566

def map(lat, lon, zoom):
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 0,
            },
            layers=[],
        )
    )

map(latitude,longitude,zoom=15)


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


# name = st.text_input('이름을 입력하세요.', max_chars=10)
# context = st.text_area('민원 내용을 입력하세요.', height = 제한 숫자)
# my_date = st.date_input('민원 날짜를 입력하세요.')
# submit = st.form_submit_button
# google_sheet_upload(SPREADSHEET_ID, 시트 range_name, [[name, context]])