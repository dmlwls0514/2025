import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="🛍️ 소비자 트렌드 퀴즈", layout="centered")
st.title("🛍️ 소비자 트렌드 퀴즈")
st.write("아래 질문에 답하면 당신의 소비 성향이 MZ세대와 얼마나 비슷한지 그래프로 보여드려요!")

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

# 선택과 점수
category_scores = {"라이프스타일":0, "트렌드 민감도":0, "소비 성향":0}

for i, q in enumerate(questions):
    choice = st.radio(q["q"], q["options"], key=f"q{i}")
    category_scores[q["category"]] += q["score"][q["options"].index(choice)]

# 결과 버튼
if st.button("🎉 결과 확인"):
    st.subheader("📊 영역별 점수 그래프")

    # 데이터프레임 생성
    df = pd.DataFrame(list(category_scores.items()), columns=["영역", "점수"])

    # 그래프 그리기
    fig, ax = plt.subplots()
    ax.bar(df["영역"], df["점수"], color=["#FF6F61","#6B5B95","#88B04B"])
    ax.set_ylim(0, max(df["점수"])+1)
    ax.set_ylabel("점수")
    ax.set_title("당신의 소비 성향 영역별 점수")
    for i, v in enumerate(df["점수"]):
        ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

    st.pyplot(fig)
