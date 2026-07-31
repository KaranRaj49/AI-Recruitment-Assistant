import streamlit as st
import pandas as pd

def show_ranking_table(results):
    if not results:
        return

    st.markdown("""
    <div style="
        font-family:'Space Grotesk',sans-serif;
        font-size:18px;
        font-weight:600;
        color:#ffffff;
        margin-bottom:16px;
    ">🏆 Candidate Ranking</div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame(results)
    df = df.sort_values("score", ascending=False).reset_index(drop=True)

    col1, col2, col3, col4 = st.columns(4)
    total = len(df)
    hired = len(df[df["recommendation"] == "Hire"])
    interviewed = len(df[df["recommendation"] == "Interview"])
    rejected = len(df[df["recommendation"] == "Reject"])

    for col, val, label, color in [
        (col1, total, "Total", "#ffffff"),
        (col2, hired, "Hire ✓", "#4ade80"),
        (col3, interviewed, "Interview", "#facc15"),
        (col4, rejected, "Reject", "#f87171"),
    ]:
        with col:
            st.markdown(f"""
            <div style="
                background:#111827;
                border:1px solid rgba(255,255,255,0.08);
                border-radius:10px;
                padding:14px 16px;
                text-align:center;
            ">
                <div style="color:{color};font-size:24px;font-weight:600;
                font-family:'Space Grotesk',sans-serif;">{val}</div>
                <div style="color:#64748b;font-size:11px;margin-top:4px;
                text-transform:uppercase;letter-spacing:0.05em;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)

    for i, row in df.iterrows():
        score = row["score"]
        rec = row["recommendation"]
        name = row["name"]

        initials = "".join([w[0].upper() for w in name.split()[:2]])

        if score >= 80:
            score_color = "#4ade80"
            bar_color = "#22c55e"
        elif score >= 60:
            score_color = "#facc15"
            bar_color = "#eab308"
        else:
            score_color = "#f87171"
            bar_color = "#ef4444"

        if rec == "Hire":
            rec_bg = "rgba(34,197,94,0.12)"
            rec_border = "rgba(34,197,94,0.3)"
            rec_color = "#4ade80"
        elif rec == "Interview":
            rec_bg = "rgba(234,179,8,0.12)"
            rec_border = "rgba(234,179,8,0.3)"
            rec_color = "#facc15"
        else:
            rec_bg = "rgba(239,68,68,0.12)"
            rec_border = "rgba(239,68,68,0.3)"
            rec_color = "#f87171"

        st.markdown(f"""
        <div style="
            background:#111827;
            border:1px solid rgba(255,255,255,0.08);
            border-radius:10px;
            padding:14px 16px;
            display:flex;
            align-items:center;
            gap:14px;
            margin-bottom:8px;
            transition: all 0.2s;
        ">
            <div style="color:#475569;font-size:13px;font-weight:500;min-width:20px;">
                {i+1}
            </div>
            <div style="
                width:36px;height:36px;
                background:rgba(59,130,246,0.15);
                border-radius:8px;
                display:flex;align-items:center;
                justify-content:center;
                color:#60a5fa;font-size:12px;
                font-weight:600;flex-shrink:0;
            ">{initials}</div>
            <div style="flex:1;">
                <div style="color:#e2e8f0;font-size:13px;font-weight:500;">{name}</div>
            </div>
            <div style="display:flex;align-items:center;gap:8px;width:140px;">
                <div style="flex:1;height:4px;background:rgba(255,255,255,0.08);border-radius:100px;overflow:hidden;">
                    <div style="width:{score}%;height:100%;background:{bar_color};border-radius:100px;"></div>
                </div>
                <div style="color:#e2e8f0;font-size:12px;font-weight:500;min-width:32px;text-align:right;">
                    {score}%
                </div>
            </div>
            <div style="
                background:{rec_bg};
                border:1px solid {rec_border};
                color:{rec_color};
                padding:3px 12px;
                border-radius:100px;
                font-size:12px;
                font-weight:500;
            ">{rec}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)

    csv = df.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Results as CSV",
        data=csv,
        file_name="candidate_ranking.csv",
        mime="text/csv",
        use_container_width=True
    )