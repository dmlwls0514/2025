# 아이템 이동
new_items = []
for ix, iy in st.session_state.items:
    iy += 0.015
    if iy < 1.0:
        new_items.append([ix, iy])
st.session_state.items = new_items  # 반복문 밖에서 한 번만 할당

# 충돌 체크
updated_items = []
for ix, iy in st.session_state.items:
    if abs(ix - st.session_state.char_x) < 0.05 and abs(iy - st.session_state.char_y) < 0.05:
        st.session_state.score += 1
    else:
        updated_items.append([ix, iy])  # 부딪히지 않은 아이템만 유지

st.session_state.items = updated_items
