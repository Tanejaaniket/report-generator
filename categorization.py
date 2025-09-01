import pandas as pd
import streamlit as st


# uploaded_file = st.file_uploader("Upload your Excel File", type=["xlsx"])

# if uploaded_file is not None:
#     df = pd.read_excel(uploaded_file)
#     df.columns = df.columns.astype(str)
    

#     if "total" in df.columns:
#         # Create a form with a submit button
#         with st.form("categorize_form"):
#             st.write("Click here")
#             submit = st.form_submit_button("Submit")

#         if submit:
#             # percentage
#             df["Percentage"] = (df["total"] / 100) * 100

#             # Categorizing students
#             below_40 = df[df["Percentage"] < 40].head(5)
#             between_70_80 = df[(df["Percentage"] >= 70) & (df["Percentage"] <= 80)].head(5)
#             above_80 = df[df["Percentage"] > 80].head(5)

#             st.subheader("Students below 40%")
#             st.dataframe(below_40)

#             st.subheader("Students between 70-80%")
#             st.dataframe(between_70_80)

#             st.subheader("Students above 80%")
#             st.dataframe(above_80)



def categorize_students(df):

    df.columns = df.columns.astype(str)

    # Calculate percentage (assuming total marks are out of 100)
    df["Percentage"] = (df["total"] / 100) * 100

    # Categorize students
    below_40 = df[df["Percentage"] < 40].head(5)
    between_70_80 = df[(df["Percentage"] >= 70) & (df["Percentage"] <= 80)].head(5)
    above_80 = df[df["Percentage"] > 80].head(5)

    return below_40, between_70_80, above_80