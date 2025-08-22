import streamlit as st

st.title("🎯 광고 예산 분배 게임 💰")
st.write("당신은 마케터입니다! 100만 원의 예산을 어떻게 쓸까요?")

# 예산 입력
insta = st.slider("📱 인스타그램 광고 (만원)", 0, 100, 30)
tv = st.slider("📺 TV 광고 (만원)", 0, 100, 50)
flyer = st.slider("📰 전단지 광고 (만원)", 0, 100, 20)

total = insta + tv + flyer

if total > 100:
    st.error("❌ 총 예산이 100만 원을 초과했습니다! 다시 조정하세요.")
else:
    st.success(f"✅ 총 {total}만 원 사용 중")

    if st.button("📊 시뮬레이션 실행하기"):
        reach = insta*50 + tv*30 + flyer*10
        awareness = insta*0.4 + tv*0.5 + flyer*0.2

        st.subheader("🔮 결과")
        st.write(f"👥 예상 도달 고객 수: {reach}명")
        st.write(f"📈 브랜드 인지도 상승률: {awareness*100:.1f}%")
