import streamlit as st

def show_upload_status(jd_file, resume_files):
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="📄 Job Description",
            value="Uploaded ✅" if jd_file else "Not Uploaded ❌"
        )

    with col2:
        st.metric(
            label="📋 Resumes",
            value=f"{len(resume_files)} file(s) ✅" if resume_files else "Not Uploaded ❌"
        )


# Example usage
jd_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf"]
)

resume_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

show_upload_status(jd_file, resume_files)