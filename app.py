import streamlit as st
from components.sidebar import render_sidebar
from components.uploader import show_upload_status
from components.ranking import show_ranking_table
from utils.pdf_reader import extract_text_from_pdf
from ai.chains import analyze_resume

# Page config
st.set_page_config(
    page_title="AI Recruitment Assistant",
    page_icon="🤖",
    layout="wide"
)

# Main header
st.title("🤖 AI Recruitment Assistant Dashboard")

st.markdown("---")

# Render sidebar
jd_file, resume_files = render_sidebar()

# Show upload status
show_upload_status(jd_file, resume_files)

st.markdown("---")

# Main logic
if jd_file and resume_files:
    if st.button("🚀 Analyze Resumes", type="primary", use_container_width=True):

        # Extract JD text
        with st.spinner("📄 Reading Job Description..."):
            jd_text = extract_text_from_pdf(jd_file)
        st.success("✅ Job Description loaded!")
        st.markdown("---")

        # Store results for ranking
        all_results = []

        # Process each resume
        for i, resume_file in enumerate(resume_files):
            candidate_name = resume_file.name.replace(".pdf", "")
            st.subheader(f"👤 Candidate {i+1}: {candidate_name}")

            # Extract resume text
            with st.spinner(f"Reading {resume_file.name}..."):
                resume_text = extract_text_from_pdf(resume_file)

            # Run AI analysis
            with st.spinner(f"🤖 Analyzing with AI..."):
                result = analyze_resume(resume_text, jd_text)

            # Display results in tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📋 Summary",
                "🎯 Skill Match",
                "📊 Score",
                "💡 Recommendation",
                "❓ Interview Questions"
            ])

            # Tab 1 - Resume Summary
            with tab1:
                st.markdown("### 📋 Resume Summary")
                st.write(result.get("summary", "No summary available"))

            # Tab 2 - Skill Match
            with tab2:
                st.markdown("### 🎯 Skill Match Analysis")
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.success("✅ Matching Skills")
                    for skill in result.get("matching_skills", []):
                        st.write(f"• {skill}")

                with col2:
                    st.error("❌ Missing Skills")
                    for skill in result.get("missing_skills", []):
                        st.write(f"• {skill}")

                with col3:
                    st.info("➕ Extra Skills")
                    for skill in result.get("extra_skills", []):
                        st.write(f"• {skill}")

            # Tab 3 - Match Score
            with tab3:
                st.markdown("### 📊 Match Score")
                score = result.get("score", 0)

                if score >= 80:
                    color = "green"
                    emoji = "🟢"
                elif score >= 60:
                    color = "orange"
                    emoji = "🟡"
                else:
                    color = "red"
                    emoji = "🔴"

                st.markdown(
                    f"<h1 style='color:{color}; text-align:center'>"
                    f"{emoji} {score}%</h1>",
                    unsafe_allow_html=True
                )
                st.progress(score / 100)

            # Tab 4 - HR Recommendation
            with tab4:
                st.markdown("### 💡 HR Recommendation")
                recommendation = result.get("recommendation", "Interview")
                justification = result.get("justification", "")

                if recommendation == "Hire":
                    st.success(f"✅ **{recommendation}**")
                elif recommendation == "Interview":
                    st.warning(f"⚠️ **{recommendation}**")
                else:
                    st.error(f"❌ **{recommendation}**")

                st.markdown("**Justification:**")
                st.write(justification)

            # Tab 5 - Interview Questions
            with tab5:
                st.markdown("### ❓ Interview Questions")

                st.markdown("**🔧 Technical Questions:**")
                for q in result.get("technical_questions", []):
                    st.write(f"• {q}")

                st.markdown("**🤝 HR Questions:**")
                for q in result.get("hr_questions", []):
                    st.write(f"• {q}")

            # Store for ranking
            all_results.append({
                "name": candidate_name,
                "score": result.get("score", 0),
                "recommendation": result.get("recommendation", "Interview")
            })

            st.markdown("---")

        # Show ranking table
        show_ranking_table(all_results)

else:
    st.warning("⬅️ Please upload a Job Description and at least one Resume from the sidebar to begin.")

st.markdown("---")
