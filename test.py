import streamlit as st
import time
import random
from streamlit.elements import slider

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
if random.random() < 0.05:  # 장애물 등장 확률
    st.session_state.obstacles.append([random.random(), 0.0])  # x, y 비율

# 아이템 생성 (15초마다)
if time.time() - st.session_state.last_item_time > 15:
    st.session_state.items.append([random.random(), 0.0])
    st.session_state.last_item_time = time.time()

# 캐릭터 이동 슬라이더
st.session_state.char_x = st.slider("🕹️ 캐릭터 위치", 0.0, 1.0, st.session_state.char_x, step=0.01)

# 화면 그리기
canvas_height = 400
canvas_width = 600
st.write("⬇️ 회피 게임 화면")

screen = [[" "]*50 for _ in range(20)]  # 간단한 텍스트 기반 화면

# 장애물 이동
new_obstacles = []
for ox, oy in st.session_state.obstacles:
    oy += 0.02  # 아래로 이동
    if oy < 1.0:
        new_obstacles.append([ox, oy])
st.session_state.obstacles = new_obstacles

# 아이템 이동
new_items = []
for ix, iy in st.session_state.items:
    iy += 0.015
    if iy < 1.0:
        new_items.append([ix, iy])
st.session_state.items = new_items

# 충돌 체크
for ox, oy in st.session_state.obstacles:
    if abs(ox - st.session_state.char_x) < 0.05 and abs(oy - st.session_state.char_y) < 0.05:
        st.session_state.score -= 1

for ix, iy in st.session_state.items:
    if abs(ix - st.session_state.char_x) < 0.05 and abs(iy - st.session_state.char_y) < 0.05:
        st.session_state.score += 1
        st.session_state.items.remove([ix, iy])

# 장애물 표시
for ox, oy in st.session_state.obstacles:
    st.write(f"🚧 장애물 ({ox:.2f}, {oy:.2f})")

# 아이템 표시
for ix, iy in st.session_state.items:
    st.write(f"💡 아이템 ({ix:.2f}, {iy:.2f})")

# 점수 표시
st.metric("🏆 점수", st.session_state.score)

# 새로고침 버튼
st.button("🔄 다음 프레임", key="refresh")
