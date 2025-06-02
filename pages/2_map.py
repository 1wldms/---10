import streamlit as st
import folium
from streamlit_folium import st_folium
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator 
from googletrans import Translator
translator = Translator()

SERVICE_ACCOUNT_FILE = "./credentials.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1r6u_HkJeCLgdMbbwGvM5b93jRibhgQniHmbVYsX0i04"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build("sheets", "v4", credentials=credentials)

st.set_page_config(page_title="민원 접수", page_icon="📍", layout="wide")
st.title('📍민원 접수')
st.sidebar.markdown('# 민원')

latitude = 37.5636201943343
longitude = 126.93774785651566

m = folium.Map(location=[latitude, longitude], zoom_start=90)  
map_data = st_folium(m, width=1500, height=700)

def google_sheet_upload(spreadsheet_id, range_name, values):
    try:
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
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        return result.get("values",[])
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []


# 민원 지도에 표시
complaints_data = google_sheet_read(SPREADSHEET_ID, "시트1!A:E")

for row in complaints_data:
    if len(row) == 5:
        date, name, content, lat, lon = row
        try:
            lat = float(lat.replace("'", ""))
            lon = float(lon.replace("'", ""))
            
            popup_html = f"""
            <div style='font-size:12px; line-height:1.2; width:200px; word-wrap:break-word;'>
            📍 <b>{name}</b><br>
            📝 {content}<br>
            📅 {date}
            </div>
            """
            
            folium.Marker(
                location=[lat, lon],
                popup=popup_html,
                icon=folium.Icon(color="red", icon="glyphicon-map-marker")
            ).add_to(m)
        except ValueError:
            pass            


clicked_location = map_data.get("last_clicked")

# 민원 입력 폼
if clicked_location:
    lat = clicked_location["lat"]
    lon = clicked_location["lng"]
    
    st.toast("📍 위치가 선택되었습니다! 아래에서 민원을 작성해주세요.")
    
    st.success(f"선택한 위치: 위도 {lat:.5f}, 경도 {lon:.5f}")

    with st.form("complaint_form"):
        name = st.text_input("민원 작성자", max_chars=20)
        content = st.text_area("민원 내용", height=150)
        date = st.date_input("📅 민원 날짜")
        submitted = st.form_submit_button("민원 제출")

        if submitted:
            if name and content:
                values = [[date.strftime("%Y-%m-%d"), name, content, f"'{lat}", f"'{lon}"]]
                result = google_sheet_upload(SPREADSHEET_ID, "시트1!A:E", values)
                if isinstance(result, HttpError):
                    st.error(f"Google Sheet 오류: {result}")
                else:
                    st.success("민원이 성공적으로 제출되었습니다!")
            else:
                st.warning("이름과 민원 내용을 모두 입력해주세요.")
else:
    st.info("먼저 지도에서 위치를 클릭해주세요.")
    

if st.button("📊 날짜별 민원 수 보기"):
    if complaints_data:
        try:
            dates = [row[0] for row in complaints_data if len(row) >= 1]
            
            
            df = pd.DataFrame({
                '날짜': pd.to_datetime(dates, format="%Y. %m. %d", errors='coerce')
            })
            df = df.dropna()
            
            if df.empty:
                st.warning("❗ 유효한 날짜 데이터가 없습니다.")
            else:
                date_counts = df['날짜'].dt.strftime('%Y-%m-%d').value_counts().sort_index()
            
                fig, ax = plt.subplots()
                date_counts.plot(kind='bar', ax=ax)
                ax.set_title('Number of Complaints by Date')
                ax.set_xlabel('Date')
                ax.set_ylabel('Number of Complaints')
                ax.tick_params(axis='x', rotation=45)
                ax.yaxis.set_major_locator(MaxNLocator(integer=True)) 
                st.pyplot(fig)
                
        except Exception as e:
            st.error(f"그래프 생성 중 오류 발생: {e}")
    else:
        st.info("아직 민원 데이터가 없습니다.")

    #조회하기
    # 사이드바에 작성자 조회 UI
st.sidebar.markdown("## 작성자별 민원 조회")
author_name = st.sidebar.text_input("작성자 이름 입력")

if st.sidebar.button("조회"):
    if not author_name.strip():
        st.sidebar.warning("작성자 이름을 입력해주세요.")
    else:
        filtered_complaints = [row for row in complaints_data if len(row) >= 2 and row[1] == author_name.strip()]
        if filtered_complaints:
            st.sidebar.write(f"'{author_name}' 님의 민원 내역:")
            for row in filtered_complaints:
                if len(row) == 5:
                    date, name, content, lat, lon = row
                    #번역
                                        
                    try:
                        detected = translator.detect(content)
                        if detected.lang == 'ko':
                            translated = translator.translate(content, src='ko', dest='en')
                        else:
                            translated = translator.translate(content, src=detected.lang, dest='ko')
                        translated_text = translated.text
                    except Exception as e:
                        translated_text = "⚠️ 번역 실패"

                    st.sidebar.markdown(f"""
                    - 📅 {date}  
                    - 📝 원문: {content}  
                    - 🌐 번역: {translated_text}
                    """)
        else:
            st.sidebar.info("해당 작성자의 민원 내역이 없습니다.")

st.markdown("---")
st.caption("정프심화 기말과제 | 만든이: 민지은 박하람")

