import streamlit as st
import pandas as pd


def show_ranking_table(results):
    st.markdown("---")
    st.subheader("🏆 Candidate Ranking Dashboard")

    if not results:
        st.info("No results yet. Analyze resumes to see rankings.")
        return

    # Create dataframe
    df = pd.DataFrame(results)
    df = df.sort_values("score", ascending=False).reset_index(drop=True)
    df.index += 1

    # Show summary metrics
    col1, col2, col3 = st.columns(3)

    total = len(df)
    hired = len(df[df["recommendation"] == "Hire"])
    rejected = len(df[df["recommendation"] == "Reject"])

    with col1:
        st.metric("Total Candidates", total)
    with col2:
        st.metric("✅ Hire", hired)
    with col3:
        st.metric("❌ Reject", rejected)

    st.markdown("---")

    # Color recommendation column
    def color_recommendation(val):
        if val == "Hire":
            return "background-color: #d4edda; color: #155724"
        elif val == "Interview":
            return "background-color: #fff3cd; color: #856404"
        else:
            return "background-color: #f8d7da; color: #721c24"

    # Show styled table
    styled_df = df.style.map(
        color_recommendation,
        subset=["recommendation"]
    )

    st.dataframe(
        styled_df,
        use_container_width=True,
        height=300
    )

    st.markdown("---")

    # Top candidate callout
    if len(df) > 0:
        top = df.iloc[0]
        st.success(
            f"🏆 **Top Candidate: {top['name']}** "
            f"with a score of **{top['score']}%** — "
            f"Recommendation: **{top['recommendation']}**"
        )

    # CSV Export
    csv = df.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Results as CSV",
        data=csv,
        file_name="candidate_ranking.csv",
        mime="text/csv",
        use_container_width=True
    )