import streamlit as st

# MBTI별 직업 추천 데이터 (추천 이유도 추가!)
job_recommendations = {
    "ISTJ": [("🧾 회계사", "체계적이고 꼼꼼한 성격에 잘 맞아요!"),
             ("⚖️ 변호사", "논리적 사고와 책임감이 강한 성격에 적합해요!")],
    "ENFP": [("🎤 광고기획자", "창의적이고 에너지가 넘쳐 새로운 아이디어 발굴에 강점이 있어요!"),
             ("📰 언론인", "열정적으로 세상과 소통하고 싶어하는 성향과 잘 맞아요!")],
    "INTP": [("🔬 연구원", "탐구심 많고 분석적인 사고력으로 과학적 발견을 이끌어요!"),
             ("💻 개발자", "논리적이고 독창적인 아이디어로 새로운 프로그램을 만들어낼 수 있어요!")],
    "ESFP": [("🎭 배우", "에너지가 넘치고 사람들 앞에서 빛나는 성격!"),
             ("🎉 이벤트 기획자", "모든 순간을 즐겁게 만드는 능력이 있어요!")],
    "ENTJ": [("👔 CEO", "리더십과 추진력으로 조직을 이끌기에 최적!"),
             ("📊 경영 컨설턴트", "분석력과 전략적 사고로 기업 성장을 이끌어요!")]
}

# 페이지 설정
st.set_page_config(page_title="MBTI Career Finder 🎓", page_icon="🌟", layout="centered")

# 헤더
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🌈 MBTI 기반 진로 추천 🎓</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33C1FF;'>당신의 성격이 반짝이는 직업을 찾아보세요 ✨</h3>", unsafe_allow_html=True)

# MBTI 선택 박스
mbti = st.selectbox("💡 MBTI를 선택하세요:", list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.markdown(f"## 🔮 {mbti} 유형에 어울리는 직업 추천 🌟")
    for job, reason in job_recommendations[mbti]:
        st.markdown(f"### {job}")
        st.write(f"👉 {reason}")
        st.write("---")

# 푸터
st.markdown("<br><br><h4 style='text-align: center; color: gray;'>💖 Made with Streamlit | Explore Your Future 🚀</h4>", unsafe_allow_html=True)
