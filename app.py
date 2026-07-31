import streamlit as st
from components.sidebar import render_sidebar
from components.uploader import show_upload_status
from components.ranking import show_ranking_table
from components.styles import load_css
from utils.pdf_reader import extract_text_from_pdf
from ai.chains import analyze_resume


# ============================================================
# ANIMATED HELPER FUNCTIONS
# ============================================================

def shimmer_loading(lines=3):
    widths = ["60%", "85%", "70%", "45%", "90%"]
    bars = ""
    for i in range(lines):
        w = widths[i % len(widths)]
        bars += f"""
        <div style="
            background: linear-gradient(90deg,
                rgba(255,255,255,0.03) 25%,
                rgba(255,255,255,0.07) 50%,
                rgba(255,255,255,0.03) 75%
            );
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
            border-radius: 6px;
            height: 12px;
            width: {w};
            margin-bottom: 8px;
        "></div>
        """
    return f"""
    <div style="
        background: #111827;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 10px;
        padding: 16px 20px;
        animation: fadeUp 0.4s ease;
    ">{bars}</div>
    """


def typing_indicator(text="AI is analyzing..."):
    return f"""
    <div style="
        display: flex;
        align-items: center;
        gap: 10px;
        background: rgba(59,130,246,0.06);
        border: 1px solid rgba(59,130,246,0.2);
        border-radius: 8px;
        padding: 10px 16px;
        margin: 8px 0;
        animation: borderGlow 2.5s ease infinite, fadeUp 0.4s ease;
    ">
        <span style="
            display: inline-block;
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #22c55e;
            animation: pulse 1.5s ease infinite;
            flex-shrink: 0;
        "></span>
        <span style="
            color: #94a3b8;
            font-size: 13px;
            overflow: hidden;
            white-space: nowrap;
            border-right: 2px solid #3b82f6;
            animation: typing 2s steps(30) infinite;
            max-width: 400px;
        ">{text}</span>
    </div>
    """


def animated_score(score):
    if score >= 80:
        color = "#4ade80"
        label = "Excellent Match"
        emoji = "🟢"
    elif score >= 60:
        color = "#facc15"
        label = "Good Match"
        emoji = "🟡"
    else:
        color = "#f87171"
        label = "Low Match"
        emoji = "🔴"

    return f"""
    <div style="
        background: #111827;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 12px;
        padding: 48px 32px;
        text-align: center;
        animation: scaleIn 0.5s ease;
        margin-top: 12px;
    ">
        <div style="
            font-family: 'Space Grotesk', sans-serif;
            font-size: 80px;
            font-weight: 700;
            color: {color};
            line-height: 1;
            margin-bottom: 12px;
            animation: countUp 0.8s ease;
        ">{score}%</div>
        <div style="
            color: #64748b;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            font-weight: 500;
        ">{emoji} {label}</div>
    </div>
    """


def animated_candidate_header(i, name):
    initials = "".join([w[0].upper() for w in name.split()[:2]])
    delay = i * 0.1
    return f"""
    <div style="
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 28px 0 16px;
        animation: slideInLeft 0.5s ease {delay}s both;
    ">
        <div style="
            width: 42px; height: 42px;
            background: rgba(59,130,246,0.15);
            border: 1px solid rgba(59,130,246,0.25);
            border-radius: 10px;
            display: flex; align-items: center;
            justify-content: center;
            color: #60a5fa;
            font-size: 14px;
            font-weight: 600;
            flex-shrink: 0;
            animation: float 3s ease infinite;
        ">{initials}</div>
        <div>
            <div style="
                color: #64748b;
                font-size: 10px;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                font-weight: 500;
            ">Candidate {i+1}</div>
            <div style="
                font-family: 'Space Grotesk', sans-serif;
                color: #ffffff;
                font-size: 17px;
                font-weight: 600;
            ">{name}</div>
        </div>
        <div style="
            margin-left: auto;
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(59,130,246,0.08);
            border: 1px solid rgba(59,130,246,0.2);
            border-radius: 100px;
            padding: 4px 12px;
            font-size: 11px;
            color: #60a5fa;
            animation: borderGlow 2.5s ease infinite;
        ">
            <span style="
                width: 6px; height: 6px;
                border-radius: 50%;
                background: #22c55e;
                animation: pulse 1.5s ease infinite;
                display: inline-block;
            "></span>
            Analyzing...
        </div>
    </div>
    """


def skill_tags(skills, color, bg, border):
    if not skills:
        return "<span style='color:#475569;font-size:13px;'>None found</span>"
    return "".join([
        f"""<span style="
            display: inline-block;
            background: {bg};
            border: 1px solid {border};
            color: {color};
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 12px;
            font-weight: 500;
            margin: 3px;
            animation: scaleIn 0.3s ease;
            transition: all 0.2s ease;
        ">{s}</span>"""
        for s in skills
    ])


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="RecruitAI — HR Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(load_css(), unsafe_allow_html=True)


# ============================================================
# TOP HEADER
# ============================================================

st.markdown("""
<div style="
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 0 24px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 28px;
    animation: fadeUp 0.5s ease;
">
    <div style="display:flex; align-items:center; gap:14px;">
        <div style="
            width: 40px; height: 40px;
            background: #3b82f6;
            border-radius: 10px;
            display: flex; align-items: center;
            justify-content: center;
            font-size: 20px;
            animation: float 3s ease infinite;
        ">🤖</div>
        <div>
            <div style="
                font-family: 'Space Grotesk', sans-serif;
                font-size: 20px;
                font-weight: 700;
                color: #ffffff;
                line-height: 1.2;
            ">AI Recruitment Assistant</div>
            <div style="color:#475569; font-size:12px; margin-top:2px;">
                Intelligent resume screening powered by LangChain + LLaMA
            </div>
        </div>
    </div>
    <div style="
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(59,130,246,0.08);
        border: 1px solid rgba(59,130,246,0.2);
        color: #60a5fa;
        padding: 7px 16px;
        border-radius: 100px;
        font-size: 12px;
        font-weight: 500;
        animation: borderGlow 3s ease infinite;
    ">
        <span style="
            width: 6px; height: 6px;
            border-radius: 50%;
            background: #22c55e;
            animation: pulse 1.5s ease infinite;
            display: inline-block;
        "></span>
        Groq • LangChain • Streamlit
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR + UPLOAD STATUS
# ============================================================

jd_file, resume_files = render_sidebar()
show_upload_status(jd_file, resume_files)

st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)


# ============================================================
# MAIN ANALYSIS
# ============================================================

if jd_file and resume_files:
    if st.button("🚀 Analyze Resumes", type="primary", use_container_width=True):

        # Read JD
        with st.spinner("📄 Reading job description..."):
            jd_text = extract_text_from_pdf(jd_file)

        st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(34,197,94,0.08);
            border: 1px solid rgba(34,197,94,0.2);
            border-radius: 8px;
            padding: 10px 16px;
            color: #4ade80;
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 20px;
            animation: fadeUp 0.4s ease;
        ">
            <span style="font-size:16px;">✓</span>
            Job description loaded successfully
        </div>
        """, unsafe_allow_html=True)

        all_results = []

        # Process each resume
        for i, resume_file in enumerate(resume_files):
            candidate_name = (
                resume_file.name
                .replace(".pdf", "")
                .replace("-", " ")
                .replace("_", " ")
                .title()
            )

            # Animated candidate header
            st.markdown(
                animated_candidate_header(i, candidate_name),
                unsafe_allow_html=True
            )

            # Extract text
            with st.spinner(f"Reading {resume_file.name}..."):
                resume_text = extract_text_from_pdf(resume_file)

            # Typing indicator + shimmer while AI runs
            typing_placeholder = st.empty()
            shimmer_placeholder = st.empty()

            typing_placeholder.markdown(
                typing_indicator(f"Analyzing {candidate_name}'s resume against job requirements..."),
                unsafe_allow_html=True
            )
            shimmer_placeholder.markdown(
                shimmer_loading(4),
                unsafe_allow_html=True
            )

            # Run AI
            result = analyze_resume(resume_text, jd_text)

            # Clear loading indicators
            typing_placeholder.empty()
            shimmer_placeholder.empty()

            # ── TABS ──────────────────────────────────────
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📋 Summary",
                "🎯 Skill Match",
                "📊 Score",
                "💡 Recommendation",
                "❓ Interview Questions"
            ])

            # Tab 1 — Summary
            with tab1:
                st.markdown(f"""
                <div style="
                    background: #111827;
                    border: 1px solid rgba(255,255,255,0.07);
                    border-radius: 10px;
                    padding: 20px 24px;
                    color: #cbd5e1;
                    font-size: 14px;
                    line-height: 1.8;
                    margin-top: 12px;
                    animation: fadeUp 0.5s ease;
                ">{result.get("summary", "No summary available")}</div>
                """, unsafe_allow_html=True)

            # Tab 2 — Skill Match
            with tab2:
                col1, col2, col3 = st.columns(3)
                sections = [
                    (col1, "✅ Matching", result.get("matching_skills", []),
                     "#4ade80", "rgba(34,197,94,0.12)", "rgba(34,197,94,0.3)"),
                    (col2, "❌ Missing", result.get("missing_skills", []),
                     "#f87171", "rgba(239,68,68,0.12)", "rgba(239,68,68,0.3)"),
                    (col3, "➕ Extra", result.get("extra_skills", []),
                     "#60a5fa", "rgba(59,130,246,0.12)", "rgba(59,130,246,0.3)"),
                ]
                for col, title, skills, color, bg, border in sections:
                    with col:
                        st.markdown(f"""
                        <div style="
                            background: #111827;
                            border: 1px solid rgba(255,255,255,0.07);
                            border-radius: 10px;
                            padding: 16px;
                            margin-top: 12px;
                            animation: fadeUp 0.5s ease;
                            min-height: 120px;
                        ">
                            <div style="
                                color: {color};
                                font-size: 11px;
                                font-weight: 600;
                                margin-bottom: 12px;
                                text-transform: uppercase;
                                letter-spacing: 0.06em;
                            ">{title}</div>
                            {skill_tags(skills, color, bg, border)}
                        </div>
                        """, unsafe_allow_html=True)

            # Tab 3 — Score
            with tab3:
                score = result.get("score", 0)
                st.markdown(animated_score(score), unsafe_allow_html=True)
                st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)
                st.progress(score / 100)

            # Tab 4 — Recommendation
            with tab4:
                rec = result.get("recommendation", "Interview")
                justification = result.get("justification", "")

                if rec == "Hire":
                    rc = "#4ade80"
                    rb = "rgba(34,197,94,0.12)"
                    rbr = "rgba(34,197,94,0.3)"
                    emoji = "✅"
                elif rec == "Interview":
                    rc = "#facc15"
                    rb = "rgba(234,179,8,0.12)"
                    rbr = "rgba(234,179,8,0.3)"
                    emoji = "⚠️"
                else:
                    rc = "#f87171"
                    rb = "rgba(239,68,68,0.12)"
                    rbr = "rgba(239,68,68,0.3)"
                    emoji = "❌"

                st.markdown(f"""
                <div style="
                    background: #111827;
                    border: 1px solid rgba(255,255,255,0.07);
                    border-radius: 12px;
                    padding: 32px;
                    text-align: center;
                    margin-top: 12px;
                    animation: scaleIn 0.5s ease;
                ">
                    <span style="
                        background: {rb};
                        border: 2px solid {rbr};
                        color: {rc};
                        padding: 10px 36px;
                        border-radius: 100px;
                        font-size: 18px;
                        font-weight: 600;
                        font-family: 'Space Grotesk', sans-serif;
                        animation: scaleIn 0.5s ease;
                        display: inline-block;
                    ">{emoji} {rec}</span>
                    <div style="
                        color: #94a3b8;
                        font-size: 13px;
                        line-height: 1.7;
                        margin-top: 20px;
                        text-align: left;
                        border-top: 1px solid rgba(255,255,255,0.06);
                        padding-top: 16px;
                        animation: fadeUp 0.6s ease 0.2s both;
                    ">
                        <div style="
                            color: #475569;
                            font-size: 10px;
                            text-transform: uppercase;
                            letter-spacing: 0.06em;
                            margin-bottom: 8px;
                            font-weight: 500;
                        ">Justification</div>
                        {justification}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Tab 5 — Interview Questions
            with tab5:
                tech_qs = result.get("technical_questions", [])
                hr_qs = result.get("hr_questions", [])

                st.markdown("""
                <div style="
                    color: #60a5fa;
                    font-size: 11px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.06em;
                    margin: 12px 0 10px;
                ">🔧 Technical Questions</div>
                """, unsafe_allow_html=True)

                for j, q in enumerate(tech_qs):
                    st.markdown(f"""
                    <div style="
                        background: #111827;
                        border: 1px solid rgba(255,255,255,0.06);
                        border-left: 3px solid #3b82f6;
                        border-radius: 0 8px 8px 0;
                        padding: 12px 16px;
                        color: #cbd5e1;
                        font-size: 13px;
                        line-height: 1.6;
                        margin-bottom: 8px;
                        animation: slideInLeft 0.4s ease {j * 0.1}s both;
                        transition: all 0.2s ease;
                    ">🔹 {q}</div>
                    """, unsafe_allow_html=True)

                st.markdown("""
                <div style="
                    color: #a78bfa;
                    font-size: 11px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 0.06em;
                    margin: 16px 0 10px;
                ">🤝 HR Questions</div>
                """, unsafe_allow_html=True)

                for j, q in enumerate(hr_qs):
                    st.markdown(f"""
                    <div style="
                        background: #111827;
                        border: 1px solid rgba(255,255,255,0.06);
                        border-left: 3px solid #8b5cf6;
                        border-radius: 0 8px 8px 0;
                        padding: 12px 16px;
                        color: #cbd5e1;
                        font-size: 13px;
                        line-height: 1.6;
                        margin-bottom: 8px;
                        animation: slideInLeft 0.4s ease {j * 0.1}s both;
                        transition: all 0.2s ease;
                    ">🔹 {q}</div>
                    """, unsafe_allow_html=True)

            # Store result
            all_results.append({
                "name": candidate_name,
                "score": result.get("score", 0),
                "recommendation": result.get("recommendation", "Interview")
            })

            st.markdown("""
            <div style="
                border-top: 1px solid rgba(255,255,255,0.05);
                margin: 28px 0;
            "></div>
            """, unsafe_allow_html=True)

        # Ranking table
        show_ranking_table(all_results)


# ============================================================
# EMPTY STATE
# ============================================================

else:
    st.markdown("""
    <div style="
        text-align: center;
        padding: 80px 40px;
        background: rgba(255,255,255,0.02);
        border: 1px dashed rgba(255,255,255,0.07);
        border-radius: 16px;
        margin-top: 8px;
        animation: fadeUp 0.6s ease;
    ">
        <div style="
            font-size: 52px;
            margin-bottom: 16px;
            animation: float 3s ease infinite;
            display: inline-block;
        ">📂</div>
        <div style="
            font-family: 'Space Grotesk', sans-serif;
            color: #e2e8f0;
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
        ">Ready to screen candidates</div>
        <div style="color:#475569; font-size:14px; line-height:1.6;">
            Upload a job description and resumes from the sidebar<br>
            to begin AI-powered analysis
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div style="
    text-align: center;
    color: #1e293b;
    font-size: 12px;
    padding: 32px 0 8px;
    border-top: 1px solid rgba(255,255,255,0.04);
    margin-top: 40px;
    animation: fadeIn 1s ease;
">
    AI Recruitment Assistant • LangChain + LLaMA + Streamlit
</div>
""", unsafe_allow_html=True)