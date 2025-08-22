import streamlit as st
import time
import random

st.set_page_config(page_title="마케팅 회피 게임 🎮", layout="wide")

st.title("🎯 마케팅 회피 게임")

# 점수
if 'score' not in st.session_state:
    st.session_state.score = 0

# 캐릭터 초기 위치
if 'char_x' not in st.session_state:
    st.session_state.char_x = 0.5  # 0~1, 비율 좌표
if 'char_y' not in st.session_state:
    st.session_state.char_y = 0.9

# 장애물 리스트
if 'obstacles' not in st.session_state:
    st.session_state.obstacles = []

# 아이템 리스트
if 'items' not in st.session_state:
    st.session_state.items = []

# 마지막 아이템 생성 시간
if 'last_item_time' not in st.session_state:
    st.session_state.last_item_time = time.time()

# 장애물 생성
if random.random() < 0.05:
    st.session_state.obstacles.append([random.random(), 0.0])  # x, y 비율

# 아이템 생성 (15초마다)
if time.time() - st.session_state.last_item_time > 15:
    st.session_state.items.append([random.random(), 0.0])
    st.session_state.last_item_time = time.time()

# 캐릭터 이동 슬라이더 (streamlit 기본 제공)
st.session_state.char_x = st.slider("🕹️ 캐릭터 위치", 0.0, 1.0, st.session_state.char_x, step=0.01)

# 화면 그리기
canvas_height = 400
canvas_width = 600
st.write("⬇️ 회피 게임 화면")

# 나머지 코드 그대로...
