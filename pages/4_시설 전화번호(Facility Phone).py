import streamlit as st
import pandas as pd

st.set_page_config(page_title="시설 전화번호/ Facility Phone", page_icon="☎️")
st.title("☎️ 시설 전화번호/ Facility Phone")

df = pd.DataFrame ({
    "이름": [
        "시설처",
        "시설처 관재팀 ",
        "시설처 건축팀 ",
        "시설처 설비팀 ",
        "시설처 안전관리팀 ",
        "시설처 조경팀 ",
        "기후변화 적응형 사회기반시설 연구센터",
        "[구매팀] 시설공사 및 시설용역 계약 ",
        "[관재팀] 강의실 수업용 기자재 및 PC실 관리 ",
        "[관재팀] 비품등록 및 비품불용 ",
        "[관재팀] 비품수리 및 비품마켓(재활용) ",
        "[건축팀] 리모델링, 공간변경 ",
        "[건축팀] 출입문, 바닥재, 누수 등 시설 보수 ",
        "[건축팀] 도면 관리 ",
        "[설비팀] 전기시설, 음향영상시설, 승강기 ",
        "[설비팀] 냉난방 및 위생설비(화장실) ",
        "[커뮤니케이션대학원 행정팀] 장학금, 시설, 기자재",
        "[조경팀] 조경 유지관리 및 조경 공사 업무 ",
        "[조경팀] 조경 유지관리, 행사 지원 등 현장 업무 ",
        "[안전관리팀] 소방시설 관리 ",
        "[안전관리팀] 연구실 안전관리, 환경시설"],
    "Name": [
        "Facilities Office",
        "Facility Management Team",
        "Facility Department Construction Team",
        "Facility Department Facilities Team",
        "Safety Management Team, Facilities Department",
        "Facilities Department Landscaping Team",
        "Climate Change Adaptive Infrastructure Research Center",
        "[Procurement Team] Facility construction and facility service contract",
        "[Bureaucratic Team] Lecture room equipment and PC room management",
        "[Bureaucratic Team] Registration of supplies and non-use of supplies",
        "[Bureaucratic Team] Supplies Repair and Supplies Market (Recycling)",
        "[Architecture team] remodeling, changing space",
        "[Architecture team] Facility maintenance such as doors, flooring, and leaks",
        "[Architecture team] Drawing management",
        "[Facilities Team] Electrical facilities, audio-visual facilities, elevators",
        "[Facilities Team] Heating and cooling and sanitary facilities (toilets)",
        "[Communication Graduate School Administration Team] Scholarship, facilities, equipment management",
        "[Landscaping Team] Landscaping maintenance and landscaping construction work",
        "[Landscaping Team] Landscaping maintenance, event support, and field work",
        "[Safety Management Team] Firefighting facility management",
        "[Safety Management Team] Laboratory safety management, environmental facilities"],
    "위치/Location": [
        "백양관",
        "백양관 S309호(비품), 백양관 N207호(원스톱지원)",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S310호",
        "백양관 S309",
        "서울특별시 서대문구 연세로 50 연세대학교",
        "백양관 S212호",
        "백양관 N207호",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S309호",
        "백양관 S309호",
        "성암관 220호",
        "백양관 S309호",
        "온실(화원)",
        "백양관S310호",
        "백양관 S310호"],
    "전화번호/Phone number": [
        "1599-1885",
        "02)2123-2180~4, 4000",
        "02)2123-2195~8",
        "02)2123-2199, 2200~3",
        "02)2123-4179, 2176",
        "02)2123-2187, 3716, 2186",
        "1599-1885",
        "02)2123-2208",
        "02)2123-4000",
        "02)2123-2182",
        "02)2123-2181",
        "02)2123-2196",
        "02)2123-2198",
        "02)2123-2197",
        "02)2123-2201,2200",
        "02)2123-2199,2203",
        "02)2123-3445",
        "02)2123-2186",
        "02)2123-3716",
        "02)2123-4179, 4119",
        "02)2123-2176, 4801"]
})

st.markdown("""
    <style>
    .main > div.block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    table {
        width: 120%;
        background-color: white; 
        border-collapse: collapse;
        font-size: 15px;
    }
    
    thead tr {
        text-align: left !important; 
        vertical-align: top;
    }
    
    tbody tr:hover {
        background-color: rgba(65, 105, 255, 0.2); 
    }
    
    tbody td:nth-child(1) {
        text-align: left;
        font-size: 13px; 
        width: 260px;
        font-weight: bold;
    }

    tbody td:nth-child(2) {
        text-align: left;
        font-size: 13px;         
        width: 240px;           
        word-break: break-word;   
    }
    
    tbody td:nth-child(3) {
        font-size: 13px;
        width: 110px;
        text-align: center;   
        word-break: break-word
    }
        
    tbody td:nth-child(4) {
        text-align: center; 
        font-weight: bold;
        width: 170px;
    }

    th, td {
        padding: 12px 20px;
        border: 1px solid gray;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown(df.to_html(index=False), unsafe_allow_html=True)



st.markdown("---")
st.caption("정보프로그래밍심화 기말과제 | 만든이: 민지은 박하람")