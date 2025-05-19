import streamlit as st
import pydeck as pdk

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