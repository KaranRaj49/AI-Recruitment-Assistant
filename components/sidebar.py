import streamlit as st

def render_sidebar():
    st.sidebar.markdown("""
    <div style="
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 16px 0 20px;
        border-bottom: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 20px;
    ">
        <div style="
            width: 32px; height: 32px;
            background: #3b82f6;
            border-radius: 8px;
            display: flex; align-items: center;
            justify-content: center;
            font-size: 16px;
        ">🤖</div>
        <div>
            <div style="color:#ffffff; font-weight:600; font-size:14px; font-family:'Space Grotesk',sans-serif;">RecruitAI</div>
            <div style="color:#475569; font-size:11px;">HR Assistant</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="color:#64748b; font-size:11px; font-weight:500;
    text-transform:uppercase; letter-spacing:0.05em; margin-bottom:8px;">
        Job Description
    </div>
    """, unsafe_allow_html=True)

    jd_file = st.sidebar.file_uploader(
        "Upload JD",
        type=["pdf"],
        key="jd_uploader",
        label_visibility="collapsed"
    )

    if jd_file:
        st.sidebar.markdown(f"""
        <div style="
            background: rgba(34,197,94,0.08);
            border: 1px solid rgba(34,197,94,0.2);
            border-radius: 8px;
            padding: 8px 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 6px;
        ">
            <div style="width:6px;height:6px;border-radius:50%;background:#22c55e;flex-shrink:0;"></div>
            <div>
                <div style="color:#e2e8f0;font-size:12px;font-weight:500;">{jd_file.name[:25]}...</div>
                <div style="color:#64748b;font-size:11px;">Ready</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="color:#64748b; font-size:11px; font-weight:500;
    text-transform:uppercase; letter-spacing:0.05em;
    margin-top:20px; margin-bottom:8px;">
        Resumes
    </div>
    """, unsafe_allow_html=True)

    resume_files = st.sidebar.file_uploader(
        "Upload Resumes",
        type=["pdf"],
        accept_multiple_files=True,
        key="resume_uploader",
        label_visibility="collapsed"
    )

    if resume_files:
        st.sidebar.markdown(f"""
        <div style="
            background: rgba(59,130,246,0.08);
            border: 1px solid rgba(59,130,246,0.2);
            border-radius: 8px;
            padding: 8px 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 6px;
        ">
            <div style="
                background:#3b82f6; color:white;
                border-radius:100px; font-size:11px;
                font-weight:600; padding:1px 8px;
            ">{len(resume_files)}</div>
            <div style="color:#e2e8f0;font-size:12px;font-weight:500;">
                {len(resume_files)} resume{'s' if len(resume_files)>1 else ''} selected
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.sidebar.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    if not jd_file or not resume_files:
        st.sidebar.markdown("""
        <div style="
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 12px;
            color: #475569;
            font-size: 12px;
            line-height: 1.6;
        ">
            Upload a job description and at least one resume to begin analysis.
        </div>
        """, unsafe_allow_html=True)

    return jd_file, resume_files