import streamlit as st

def show_upload_status(jd_file, resume_files):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="
            background:#111827;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;
            padding:16px;
        ">
            <div style="color:#ffffff;font-size:22px;font-weight:600;
            font-family:'Space Grotesk',sans-serif;">
                {'✓' if jd_file else '—'}
            </div>
            <div style="color:#64748b;font-size:11px;margin-top:4px;
            text-transform:uppercase;letter-spacing:0.05em;">Job Description</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        count = len(resume_files) if resume_files else 0
        st.markdown(f"""
        <div style="
            background:#111827;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;
            padding:16px;
        ">
            <div style="color:#ffffff;font-size:22px;font-weight:600;
            font-family:'Space Grotesk',sans-serif;">{count}</div>
            <div style="color:#64748b;font-size:11px;margin-top:4px;
            text-transform:uppercase;letter-spacing:0.05em;">Resumes</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background:#111827;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;
            padding:16px;
        ">
            <div style="color:#ffffff;font-size:22px;font-weight:600;
            font-family:'Space Grotesk',sans-serif;">AI</div>
            <div style="color:#64748b;font-size:11px;margin-top:4px;
            text-transform:uppercase;letter-spacing:0.05em;">LLaMA 3.1</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
            background:#111827;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;
            padding:16px;
        ">
            <div style="color:#ffffff;font-size:22px;font-weight:600;
            font-family:'Space Grotesk',sans-serif;">⚡</div>
            <div style="color:#64748b;font-size:11px;margin-top:4px;
            text-transform:uppercase;letter-spacing:0.05em;">Groq Powered</div>
        </div>
        """, unsafe_allow_html=True)