import streamlit as st
import pandas as pd
from categorization import categorize_students
from generate_report import create_student_report_pdf
import base64
import os

# --------------- PAGE HEADER ---------------
st.set_page_config(page_title="Academic Dashboard", page_icon="🎓", layout="wide")
st.title('🎓 Academic Dashboard')
st.markdown("---")
if os.path.exists("report.pdf"):    
    os.remove("report.pdf")

# --------------- FACULTY DETAILS SECTION ---------------
with st.container():
    st.subheader("👨‍🏫 Faculty & Course Information")

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        faculty_name = st.text_input("Faculty Name")
        subject = st.text_input("Subject Name")
    with col3:
        class_section = st.text_input("Section")
        course_code = st.text_input("Course Code")
    with col2:    
        class_name = st.text_input("Class")

    if st.button("✅ Save Faculty Details") and (faculty_name and class_name and class_section and course_code and subject):
        st.success(f"Saved → Faculty: {faculty_name}, Subject: {subject}, Code: {course_code}, Class: {class_name}, Subject: {class_section}")
    else:
            st.warning("⚠️ Please fill in all details before saving.")

if (faculty_name and class_name and class_section and course_code and subject):
    
    # --------------- UPLOAD SECTION ---------------
    with st.container():
        st.subheader("📂 Upload Excel Data")

        uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            st.write("### 📋 Data Preview:")
            st.dataframe(df)

            if st.button("Generate report"):
                (below_40, between_70_80, above_80) = categorize_students(df=df)
                create_student_report_pdf(teachers_name=faculty_name,course_name=subject,course_code=course_code,class_name=class_name,section=class_section,df_above80=above_80,df_below40=below_40,df_70to80=between_70_80)
                st.success("Data uploaded successfully!")

    # --------------- DOWNLOAD SECTION ---------------
    with st.container():
        st.subheader("⬇️ Download Reports")

        file_path = "report.pdf"
        if os.path.exists(file_path):
            # Read and encode PDF
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                pdf_link = f'<a href="data:application/pdf;base64,{base64_pdf}" target="_blank">📄 Open PDF in new tab</a>'
                st.markdown(pdf_link, unsafe_allow_html=True)
                st.download_button("Download Report", data=f, file_name="report.pdf",   mime="application/pdf")
        else:
            st.warning("Please click on 'Generate Report' button to generate report.")
        
