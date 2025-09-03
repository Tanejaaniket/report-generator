import streamlit as st
import pandas as pd
import base64

# --------------- PAGE HEADER ---------------
st.set_page_config(page_title="Academic Dashboard", page_icon="🎓", layout="wide")

#def img_to_bytes(img_path):
#    with open(img_path,"rb") as f:
#        data=f.read()
#    return base64.b64encode(data).decode()

#img=img_to_bytes("hospital.png")


#bg_image=f"""
#    <style>
#    .stApp {{
#        background-image: url("data:image/png;base64,{img}");
#        background-size: cover;
#    }}
#    </style>
#    """
#st.markdown(bg_image,unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1976d2;
    }
    .subtitle {
        font-size: 20px;
        color: #424242;
    }
    .card {
        padding: 5px;
        border-radius: 8px;
        background-color: white;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🎓 Academic Dashboard')
st.markdown("---")

# --------------- FACULTY DETAILS SECTION ---------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👨‍🏫 Faculty & Course Information")

    col1, col2 = st.columns(2)

    with col1:
        faculty_name = st.text_input("Faculty Name")
        subject = st.text_input("Subject Name")

    with col2:
        course_code = st.text_input("Course Code")
        class_name = st.text_input("Class/Section")

    if st.button("✅ Save Faculty Details"):
        st.success(f"Saved → Faculty: {faculty_name}, Subject: {subject}, Code: {course_code}, Class: {class_name}")
    else:
            st.warning("⚠️ Please fill in all details before saving.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --------------- UPLOAD SECTION ---------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Upload Excel Data")

    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("### 📋 Data Preview:")
        st.dataframe(df.head())

        if st.button("📤 Submit Data"):
            st.success("Data uploaded successfully!")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------- DOWNLOAD SECTION ---------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⬇️ Download Reports")

    st.download_button("Download Report (Dummy)", "This is a sample file", file_name="report.txt")

   
