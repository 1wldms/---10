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

if lang == "ko":
    st.title("🏠 동네 민원 신고 플랫폼")
    st.markdown("불편했던 동네 문제, 이제는 직접 신고해보세요!")

    st.subheader("📌 서비스 소개")
    st.markdown("""
    <p><strong>'동네 민원 신고 플랫폼'</strong>은 우리 동네의 불편사항을 손쉽게 등록하고,<br>
    다른 사람들과 공유할 수 있는 웹 애플리케이션입니다.</p>
    
    <p>이 서비스를 통해 누구나 <strong>지도에서 위치를 클릭</strong>하여 민원을 작성하고,<br>
    그 내용을 <strong>Google Sheet</strong>에 자동 저장할 수 있습니다.</p>
    """, unsafe_allow_html=True)

    st.subheader("🛠️ 사용 방법")

    with st.expander("1. 민원 등록하기"):
        st.markdown("""
        - 지도에서 문제 발생 위치를 클릭합니다.  
        - 작성자 이름, 민원 내용을 입력합니다.  
        - 날짜를 선택합니다. 기본값은 오늘 날짜입니다.  
        - '민원 제출' 버튼을 누르면 등록 완료!
        """)

    with st.expander("2. 민원 조회/수정하기"):
        st.markdown("""
        - 사이드바에 이름 입력 후 '조회' 버튼 클릭  
        - 각 민원에 비밀번호 입력하면 수정 가능  
        - 날짜별 민원 수 확인도 가능
        """)
    
    with st.expander("3. 민원 목록 보기 및 공감하기"):
        st.markdown("""
        - 지금까지 작성된 모든 민원을 날짜순으로 정렬해서 볼 수 있습니다.  
        - 각 민원 아래에 있는 👍 버튼을 클릭하여 공감할 수 있어요.  
        - 공감 수는 Google Sheet에 실시간으로 저장됩니다.  
        - 이 기능은 사용자들이 서로의 불편에 공감하고  
        **공동의 문제 해결에 함께 참여하도록 유도**합니다.
        """)
    
    st.markdown("---")

    st.subheader("🫵🏻 원하시는 페이지를 선택하세요!")
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📝 민원 작성(한국어)", use_container_width=True):
            st.switch_page("pages/2_민원 작성.py")

    with col2:
        if st.button("📝 민원 작성(영어)", use_container_width=True):
            st.switch_page("pages/3_Write Complaint.py")

    with col3:
        if st.button("📞시설 전화번호", use_container_width=True):
            st.switch_page("pages/4_시설 전화번호(Facility Phone).py")
    
    with col4:
        if st.button("🧾 민원 게시판", use_container_width=True):
            st.switch_page("pages/5_민원게시판(ComplaintBoard).py")

    st.markdown("---")
    
    with st.expander("🧑‍💻 개발 정보"):
        st.markdown("""
        **개발 언어:** Python  
        **프레임워크:** Streamlit  
        **지도 연동:** folium + streamlit-folium  
        **데이터 저장:** Google Sheets API  
        **자동 번역:** Googletrans  
        """)

    st.caption("정보프로그래밍심화 기말과제 | 만든이: 민지은 박하람")

else:
    st.title("🏠 Neighborhood Complaint Reporting Platform")
    st.markdown("Now you can directly report inconvenient issues around your neighborhood!")

    st.subheader("📌 Service Overview")
    st.markdown("""
    <p><strong>Neighborhood Complaint Reporting Platform</strong> is a web application that allows users to easily report local inconveniences and share them with others.</p>

    <p>Through this service, anyone can <strong>click on a location on the map</strong> to file a complaint,<br>
    and the details will be automatically saved to a <strong>Google Sheet</strong>.</p>
    """, unsafe_allow_html=True)


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
        - Enter your name and click 'Search'  
        - Enter password to edit your complaint  
        - View complaint stats by date
        """)
    
    with st.expander("3. View All Complaints and Like"):
        st.markdown("""
        - You can view all complaints submitted so far in chronological order.  
        - Click the 👍 button under each complaint to express empathy.  
        - The number of likes is saved in real time to Google Sheets.  
        - This feature encourages users to empathize with others' concerns  
        and participate in solving shared problems.
        """)
    
    st.markdown("---")

    st.subheader("🫵🏻 Please select the page you want!")
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📝 Write Complaint (Korean)", use_container_width=True):
            st.switch_page("pages/2_민원 작성.py")

    with col2:
        if st.button("📝 Write Complaint (English)", use_container_width=True):
            st.switch_page("pages/3_Write Complaint.py")

    with col3:
        if st.button("📞 Facility Phone Numbers", use_container_width=True):
            st.switch_page("pages/4_시설 전화번호(Facility Phone).py")
    
    with col4:
        if st.button("🧾 Complaint Board", use_container_width=True):
            st.switch_page("pages/5_민원게시판(ComplaintBoard).py")

    st.markdown("---")
    
    with st.expander("🧑‍💻 Development Info"):
        st.markdown("""
        **Language:** Python  
        **Framework:** Streamlit  
        **Map Integration:** folium + streamlit-folium  
        **Data Storage:** Google Sheets API  
        **Auto Translation:** Googletrans  
        """)

    st.caption("Final Project for ADVANCED INFORMATION PROGRAMMING | By: Min Jieun & Park Haram")