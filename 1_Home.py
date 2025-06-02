import streamlit as st

# 페이지 설정
st.set_page_config(page_title="홈", page_icon="🏠")

# 언어 상태 초기화
if "lang" not in st.session_state:
    st.session_state["lang"] = "ko"

# 언어 전환 버튼
if st.session_state["lang"] == "ko":
    button_label = "🌐 Translate"
else:
    button_label = "🌐 원문으로"

if st.button(button_label):
    if st.session_state["lang"] == "ko":
        st.session_state["lang"] = "en"
    else:
        st.session_state["lang"] = "ko"
    st.rerun()  


lang = st.session_state["lang"]

# 언어별 텍스트
if lang == "ko":
    st.title("🏠 동네 민원 신고 플랫폼")
    st.markdown("불편했던 동네 문제, 이제는 직접 신고해보세요!")

    st.subheader("📌 서비스 소개")
    st.markdown("""
    '동네 민원 신고 플랫폼'은 우리 동네의 불편사항을 손쉽게 등록하고,  
    다른 사람들과 공유할 수 있는 웹 애플리케이션입니다.

    이 서비스를 통해 누구나 **지도에서 위치를 클릭**하여 민원을 작성하고,  
    그 내용을 **Google Sheet**에 자동 저장할 수 있습니다.
    """)

    st.subheader("🛠️ 사용 방법 (Manual)")

    with st.expander("1. 민원 등록하기"):
        st.markdown("""
        - 지도에서 문제 발생 위치를 클릭합니다.  
        - 작성자 이름, 민원 내용을 입력합니다.  
        - 날짜를 선택합니다. 기본값은 오늘 날짜입니다.  
        - '민원 제출' 버튼을 누르면 등록 완료!
        """)

    with st.expander("2. 민원 조회하기"):
        st.markdown("""
        - 작성자 이름을 입력한 후 '조회' 버튼을 누르면 해당 작성자의 민원만 볼 수 있습니다.  
        - 날짜별 민원 수를 확인할 수도 있어요.
        """)
        
    st.markdown("---")

    st.subheader("🫵🏻 원하시는 페이지를 선택하세요!")
    st.write("")
    st.write("") 
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("민원 작성하세요(한국어)"):
            st.switch_page("pages/2_map.py")

    with col2:
        if st.button("민원 작성하세요(영어)"):
            st.switch_page("pages/3_English.py")

    with col3:
        if st.button("시설 전화번호 모음"):
            st.switch_page("pages/4_시설 전화번호.py")

    st.markdown("---")
    st.caption("정프심화 기말과제 | 만든이: 민지은 박하람")

else:
    st.title("🏠 Neighborhood Complaint Reporting Platform")
    st.markdown("Now you can directly report inconvenient issues around your neighborhood!")

    st.subheader("📌 Service Overview")
    st.markdown("""
    The **Neighborhood Complaint Reporting Platform** is a web application  
    that allows anyone to easily report local inconveniences and share them with others.

    Through this service, anyone can **click on a location on the map** to file a complaint,  
    and have the contents automatically saved to a **Google Sheet**.
    """)

    st.subheader("🛠️ How to Use (Manual)")

    with st.expander("1. Submit a Complaint"):
        st.markdown("""
        - Click the location where the problem occurred on the map.  
        - Enter the name and complaint content.  
        - Choose a date (default is today).  
        - Click the 'Submit Complaint' button to finish!
        """)

    with st.expander("2. View Complaints"):
        st.markdown("""
        - Enter the name in the sidebar and click the 'Search' button to view that user's complaints.  
        - You can also check the number of complaints by date.
        """)
    
    st.markdown("---")

    st.subheader("🫵🏻 Please select the page you want!")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Write Complaint (Korean)"):
            st.switch_page("pages/2_map.py")

    with col2:
        if st.button("Write Complaint (English)"):
            st.switch_page("pages/3_English.py")

    with col3:
        if st.button("Facility Phone Numbers"):
            st.switch_page("pages/4_시설 전화번호.py")

    st.markdown("---")
    st.caption("Final Project for 정프심화 | By: Min Jieun & Park Haram")