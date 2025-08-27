import streamlit as st
import pandas as pd

st.set_page_config(page_title="🛍️ 소비자 트렌드 퀴즈", layout="centered")
st.title("🛍️ 소비자 트렌드 퀴즈")
st.write("아래 질문에 답하면 당신의 소비 성향이 MZ세대와 얼마나 비슷한지 보여드려요!")

# 질문과 점수
questions = [
    {"q": "주말 활동", "options": ["쇼핑 🛒","운동 🏃","게임 🎮","독서 📚"], "score":[3,1,2,1], "category":"라이프스타일"},
    {"q": "신제품 반응", "options":["즉시 사본다 🏃‍♂️","리뷰 확인 후 구매 ✅","관심 없음 😴","가끔 관심 👀"], "score":[3,2,0,1], "category":"트렌드 민감도"},
    {"q": "SNS 활용 빈도", "options":["하루 종일 📱","하루 1~2회 ⏰","가끔 👋","사용 안 함 ❌"], "score":[3,2,1,0], "category":"트렌드 민감도"},
    {"q": "패션/스타일 소비", "options":["트렌디하게 😎","실용적으로 👕","저렴하게 💸","관심 없음 😐"], "score":[3,2,1,0], "category":"소비 성향"},
    {"q": "맛집/카페 탐방", "options":["자주 가요 ☕🍰","가끔 가요 🍴","별로 안 가요 🚫","관심 없음 ❌"], "score":[3,2,1,0], "category":"라이프스타일"},
    {"q": "온라인 쇼핑 선호", "options":["자주 이용 🛍️","가끔 이용 📦","거의 안 이용 ❌","거의 직접 구매 🏬"], "score":[3,2,1,0], "category":"소비 성향"},
    {"q": "콘텐츠 소비 스타일", "options":["영상 위주 🎬","글/기사 📰","이미지 📸","관심 없음 😴"], "score":[3,2,1,0], "category":"트렌드 민감도"},
    {"q": "가격과 품질 선택", "options":["품질 최우선 🌟","가격/품질 균형 ⚖️","가격 최우선 💸","상관 없음 😎"], "score":[3,2,1,0], "category":"소비 성향"},
]

category_scores = {"라이프스타일":0, "트렌드 민감도":0, "소비 성향":0}

# 질문 표시
for i, q in enumerate(questions):
    choice = st.radio(q["q"], q["options"], key=f"q{i}")
    category_scores[q["category"]] += q["score"][q["options"].index(choice)]

# 결과 버튼
if st.button("🎉 결과 확인"):
    st.subheader("📊 영역별 점수 그래프")

    df = pd.DataFrame(list(category_scores.items()), columns=["영역", "점수"])
    df = df.set_index("영역")

    # Streamlit 내장 막대 그래프
    st.bar_chart(df)

    # 점수 표시 메시지
    total_score = sum(category_scores.values())
    max_score = sum([max(q["score"]) for q in questions])
    similarity = total_score / max_score * 100
    st.write(f"당신은 MZ세대 소비 성향과 **{similarity:.1f}%** 비슷합니다!")

    if similarity > 80:
        st.write("🔥 완전 MZ세대형! 트렌드에 민감하고 새로운 걸 좋아하네요.")
    elif similarity > 50:
        st.write("😊 어느 정도 MZ세대 성향이 있어요. 트렌드를 잘 활용하세요!")
    else:
        st.write("😌 전통적 소비형! 안정적이고 계획적인 소비를 선호해요.")
