import streamlit as st

st.set_page_config(page_title="소비자 트렌드 퀴즈", layout="centered")
st.title("🛍️ 소비자 트렌드 퀴즈")

st.write("아래 질문에 답하면 당신의 소비 성향이 MZ세대와 얼마나 비슷한지 알려드려요!")

# 질문 리스트
questions = [
    {"q": "주말에 주로 하는 활동은?", "options": ["쇼핑 🛒", "운동 🏃", "게임 🎮", "독서 📚"], "score": [3, 1, 2, 1]},
    {"q": "새로운 제품이 나오면?", "options": ["즉시 사본다 🏃‍♂️", "리뷰 확인 후 구매 ✅", "관심 없음 😴", "가끔 관심 👀"], "score": [3,2,0,1]},
    {"q": "SNS 활용 빈도?", "options": ["하루 종일 📱", "하루 1~2회 ⏰", "가끔 👋", "사용 안 함 ❌"], "score": [3,2,1,0]},
    {"q": "패션/스타일 소비 성향?", "options": ["트렌디하게 😎", "실용적으로 👕", "저렴하게 💸", "관심 없음 😐"], "score": [3,2,1,0]},
    {"q": "맛집/카페 탐방?", "options": ["자주 가요 ☕🍰", "가끔 가요 🍴", "별로 안 가요 🚫", "관심 없음 ❌"], "score": [3,2,1,0]},
]

total_score = 0

for i, q in enumerate(questions):
    choice = st.radio(q["q"], q["options"], key=f"q{i}")
    total_score += q["score"][q["options"].index(choice)]

# 결과 계산
if st.button("결과 확인 🎉"):
    max_score = sum([max(q["score"]) for q in questions])
    similarity = total_score / max_score * 100
    st.subheader("📊 결과")
    st.write(f"당신은 MZ세대 소비 성향과 **{similarity:.1f}%** 비슷합니다!")
    
    # 간단한 메시지
    if similarity > 80:
        st.write("🔥 완전 MZ세대형! 트렌드에 민감하고 새로운 걸 좋아하네요.")
    elif similarity > 50:
        st.write("😊 어느 정도 MZ세대 성향이 있어요. 트렌드를 잘 활용하세요!")
    else:
        st.write("😌 전통적 소비형! 안정적이고 계획적인 소비를 선호해요.")
