import streamlit as st
import pydeck as pdk


from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"


st.title('민원 접수')
st.sidebar.markdown('# 민원')

#streamlit mapbox으로 지도 생성 (우버에서 지도 생성했던 방법 사용)
#근데 네이버 지도를 사용하는게 좋으려나? 어떻게 연결해야할지 모루겠네

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

'''
사전에 수업 실습 시간에 만들어 놓은 
파일 write
파일 read 코드

이거 수정해서 사용하면 좋을듯?
가능하다면~~


def batch_update_values(spreadsheet_id, range_name, value_input_option, values):
    creds, _ = default(scopes=SCOPES)
    
    try:
        service = build("sheets", "v4", credentials=creds)

        data = [{"range": range_name, "values": values}]
        body = {"valueInputOption": value_input_option, "data": data}
        result = (
            service.spreadsheets()
            .values()
            .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
            .execute()
        )
        print(f"{result.get('totalUpdatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def batch_get_values(spreadsheet_id, range_names):
    creds, _ = default(scopes=SCOPES)
    
    try:
        service = build("sheets", "v4", credentials=creds)
        result = (
            service.spreadsheets()
            .values()
            .batchGet(spreadsheetId=spreadsheet_id, ranges=range_names)
            .execute()
        )
        ranges = result.get("valueRanges", [])
        print(f"{len(ranges)} ranges retrieved.")
        
        value_ranges = result.get("valueRanges", [])
        for value_range in value_ranges:
            values = value_range.get("values", [])
            for row in values:
                col_a = row[0] if len(row) > 0 else ""
                col_b = row[1] if len(row) > 1 else ""
                print(f"{col_a}, {col_b}")

        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == "__main__":
    spreadsheet_id = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"

    batch_update_values(
        spreadsheet_id,
        "A1:B6",
        "USER_ENTERED",
        [
            ["Hello", "It"],
            ["It", "is"],
            ["Is", "time"],
            ["Raining", "to"],
            ["!", "go"],
            ["!", "home"]
        ]
    )

    batch_get_values(
        spreadsheet_id,
        ["A1:B6"]
    )
'''