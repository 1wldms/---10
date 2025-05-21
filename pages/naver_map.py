import streamlit as st

st.markdown('# Naver map')
st.sidebar.markdown('# 민원')

from streamlit.components.v1 import html

# 네이버 클라이언트 아이디
NAVER_CLIENT_ID = "u85vj7zq6q"

map_html = f"""
<div id="map" style="width:100%;height:400px;"></div>
<script src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId={NAVER_CLIENT_ID}"></script>
<script>
var map = new naver.maps.Map('map', {{
    center: new naver.maps.LatLng(37.5636201943343, 126.93774785651566), // 연대 좌표
    zoom: 15
}});

var marker = new naver.maps.Marker({{
    map: map,
    position: map.getCenter()
}})

</script>
"""

st.markdown("### 네이버 지도 클릭해서 좌표 확인")
html(map_html, height=450)
