import streamlit as st
st.set_page_config(page_title="홈", page_icon="🏠")

st.title("🏠 동네 민원 신고 플랫폼")
st.markdown("불편했던 동네 문제, 이제는 직접 신고해보세요!")

# 간단한 소개
st.subheader("📌 서비스 소개")
st.markdown("""
'동네 민원 신고 플랫폼'은 우리 동네의 불편사항을 손쉽게 등록하고,
다른 사람들과 공유할 수 있는 웹 애플리케이션입니다.

이 서비스를 통해 누구나 **지도에서 위치를 클릭**하여 민원을 작성하고,
그 내용을 **Google Sheet**에 자동 저장할 수 있습니다.
""")

# 사용법 설명 (매뉴얼)
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


# 하단 참고
st.markdown("---")
st.caption("정프심화 기말과제 | 만든이: 민지은 박하람")
