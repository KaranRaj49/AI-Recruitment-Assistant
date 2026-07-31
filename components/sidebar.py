import streamlit as st

def render_sidebar():
    st.sidebar.image("https://img.icons8.com/color/96/resume.png", width=80)
    st.sidebar.title("AI Recruitment Assistant")
    st.sidebar.markdown("---")

    st.sidebar.subheader("📄 Job Description")
    jd_file = st.sidebar.file_uploader(
        "Upload Job Description (PDF)",
        type=["pdf"],
        key="jd_uploader"
    )

    st.sidebar.markdown("---")

    st.sidebar.subheader("📋 Resumes")
    resume_files = st.sidebar.file_uploader(
        "Upload Resume(s) (PDF)",
        type=["pdf"],
        accept_multiple_files=True,
        key="resume_uploader"
    )

    st.sidebar.markdown("---")
    st.sidebar.info("Upload a JD and at least one resume to begin.")

    return jd_file, resume_files