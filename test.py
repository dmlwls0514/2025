import streamlit as st
from PIL import Image

st.set_page_config(page_title="나만의 브랜드 만들기", layout="centered")

st.title("✨ 나만의 브랜드 만들기 ✨")
st.write("당신만의 브랜드를 만들어보세요! 이름, 슬로건, 컬러, 로고까지 한눈에 확인할 수 있어요.")

# 1. 브랜드 이름 입력
brand_name = st.text_input("브랜드 이름을 입력하세요:")

# 2. 브랜드 슬로건 입력
brand_slogan = st.text_input("브랜드 슬로건을 입력하세요:")

# 3. 브랜드 대표 색상 선택
brand_color = st.color_picker("브랜드 대표 색상을 선택하세요:")

# 4. 로고 업로드
logo_file = st.file_uploader("브랜드 로고를 업로드하세요:", type=["png", "jpg", "jpeg"])

# 5. 브랜드 카테고리 선택
category = st.selectbox("브랜드 카테고리를 선택하세요:", ["패션", "식품", "테크", "뷰티", "기타"])

# 6. 결과 표시
if st.button("브랜드 만들기"):
    st.markdown(f"## 🏷 {brand_name}")
    st.markdown(f"**슬로건:** {brand_slogan}")
    st.markdown(f"**카테고리:** {category}")
    
    # 대표 색상 박스
    st.markdown(f"""
    <div style="width:100px; height:50px; background-color:{brand_color}; border-radius:5px"></div>
    """, unsafe_allow_html=True)
    
    # 로고 표시
    if logo_file:
        image = Image.open(logo_file)
        st.image(image, caption="브랜드 로고", use_column_width=True)
    
    st.success("🎉 나만의 브랜드가 완성되었습니다!")

