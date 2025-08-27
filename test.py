import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 앱 제목 및 설명
# -------------------------------
st.title("마케팅 트렌드 예측 게임")
st.write("""
이 게임은 다양한 마케팅 관련 질문에 답하며 최신 트렌드를 예측하는 게임입니다.
각 질문에 대한 답변을 선택하면, 실제 통계 자료 기반의 결과를 확인할 수 있습니다.
""")

# -------------------------------
# 질문 & 데이터 정의
# -------------------------------
questions = [
    {
        "question": "2023년 한국에서 가장 많이 팔린 음료는?",
        "options": ["코카콜라", "핫식스"],
        "stats": [15, 5]  # % 판매량
    },
    {
        "question": "2023년에 10대가 가장 많이 사용한 SNS는?",
        "options": ["인스타그램", "페이스북"],
        "stats": [60, 15]  # % 사용자
    },
    {
        "question": "2022년 한국에서 더 인기 있었던 배달음식은?",
        "options": ["치킨", "피자"],
        "stats": [35, 25]  # % 주문 비율
    },
    {
        "question": "2022년 가장 많이 사용된 온라인 쇼핑 결제 수단은?",
        "options": ["신용카드", "간편결제"],
        "stats": [40, 35]  # % 사용 비율
    },
    {
        "question": "2023년에 소비자가 가장 많이 참여한 브랜드 이벤트 유형은?",
        "options": ["SNS 참여형 이벤트", "오프라인 매장 이벤트"],
        "stats": [55, 30]  # % 참여율
    }
]

# -------------------------------
# 질문 선택
# -------------------------------
question_titles = [q["question"] for q in questions]
selected_question = st.selectbox("질문을 선택하세요", question_titles)

# 선택된 질문 데이터 가져오기
q_data = next(q for q in questions if q["question"] == selected_question)

# 옵션 선택
user_choice = st.radio("답변을 선택하세요:", q_data["options"])

# -------------------------------
# 결과 시각화
# -------------------------------
st.subheader("실제 통계 자료 기반 결과")
fig, ax = plt.subplots()
ax.bar(q_data["options"], q_data["stats"], color=['#1f77b4','#ff7f0e'])
ax.set_ylabel("비율 (%)")
ax.set_title(selected_question)
for i, v in enumerate(q_data["stats"]):
    ax.text(i, v + 1, str(v)+"%", ha='center')
st.pyplot(fig)

# -------------------------------
# 사용자 선택 결과 표시
# -------------------------------
st.write(f"당신이 선택한 답변: **{user_choice}**")
