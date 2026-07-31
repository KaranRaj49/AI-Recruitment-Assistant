def load_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

/* === ANIMATIONS === */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes slideRight {
    from { width: 0%; }
    to   { width: var(--target-width); }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.4); opacity: 0.5; }
}
@keyframes shimmer {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
@keyframes borderGlow {
    0%, 100% { border-color: rgba(59,130,246,0.2); }
    50%       { border-color: rgba(59,130,246,0.5); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-4px); }
}
@keyframes typing {
    from { width: 0; }
    to   { width: 100%; }
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0; }
}
@keyframes countUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.9); }
    to   { opacity: 1; transform: scale(1); }
}
@keyframes spinOnce {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

/* === GLOBAL === */
.stApp {
    background: #0a0e1a !important;
    font-family: 'Inter', sans-serif !important;
}
#MainMenu, footer, header { visibility: hidden; }

/* === SIDEBAR === */
section[data-testid="stSidebar"] {
    background: #080c18 !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
section[data-testid="stSidebar"] > div {
    padding: 20px 16px !important;
    animation: fadeIn 0.5s ease !important;
}

/* === BUTTONS === */
.stButton > button {
    background: #3b82f6 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    animation: float 3s ease infinite !important;
}
.stButton > button:hover {
    background: #2563eb !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(59,130,246,0.4) !important;
}
.stButton > button:active {
    transform: scale(0.97) !important;
}

/* === TABS === */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03) !important;
    border-radius: 8px !important;
    padding: 3px !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    gap: 2px !important;
    animation: fadeIn 0.4s ease !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 6px !important;
    color: #64748b !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 6px 14px !important;
    transition: all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
    background: #1e293b !important;
    color: #e2e8f0 !important;
}

/* === PROGRESS BAR === */
.stProgress > div > div {
    background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
    border-radius: 100px !important;
    transition: width 1s ease !important;
}
.stProgress > div {
    border-radius: 100px !important;
    background: rgba(255,255,255,0.06) !important;
}

/* === DOWNLOAD BUTTON === */
.stDownloadButton > button {
    background: rgba(59,130,246,0.08) !important;
    color: #60a5fa !important;
    border: 1px solid rgba(59,130,246,0.25) !important;
    border-radius: 8px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    animation: borderGlow 3s ease infinite !important;
}
.stDownloadButton > button:hover {
    background: rgba(59,130,246,0.18) !important;
    transform: translateY(-2px) !important;
}

/* === METRICS === */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2rem !important;
    animation: countUp 0.8s ease !important;
}
[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}
[data-testid="stMetric"] {
    background: #111827 !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    padding: 16px !important;
    animation: fadeUp 0.5s ease both !important;
    transition: all 0.25s ease !important;
}
[data-testid="stMetric"]:hover {
    border-color: rgba(59,130,246,0.3) !important;
    transform: translateY(-2px) !important;
}

/* === SUCCESS / ERROR / WARNING ALERTS === */
.stSuccess {
    background: rgba(34,197,94,0.08) !important;
    border: 1px solid rgba(34,197,94,0.25) !important;
    border-radius: 8px !important;
    animation: fadeUp 0.4s ease !important;
}
.stWarning {
    background: rgba(234,179,8,0.08) !important;
    border: 1px solid rgba(234,179,8,0.25) !important;
    border-radius: 8px !important;
    animation: fadeUp 0.4s ease !important;
}
.stError {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.25) !important;
    border-radius: 8px !important;
}
.stInfo {
    background: rgba(59,130,246,0.08) !important;
    border: 1px solid rgba(59,130,246,0.2) !important;
    border-radius: 8px !important;
}

/* === SPINNER === */
.stSpinner > div {
    border-top-color: #3b82f6 !important;
    animation: spinOnce 0.8s linear infinite !important;
}

/* === FILE UPLOADER === */
[data-testid="stFileUploader"] {
    animation: fadeIn 0.5s ease !important;
}
[data-testid="stFileUploader"] section {
    border: 1px dashed rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    background: rgba(255,255,255,0.02) !important;
    transition: all 0.2s ease !important;
}
[data-testid="stFileUploader"] section:hover {
    border-color: rgba(59,130,246,0.4) !important;
    background: rgba(59,130,246,0.04) !important;
}

/* === EXPANDER === */
[data-testid="stExpander"] {
    background: #111827 !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    animation: fadeUp 0.4s ease !important;
}

/* === SCROLLBAR === */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.1);
    border-radius: 100px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(59,130,246,0.4);
}

/* === DIVIDER === */
hr {
    border-color: rgba(255,255,255,0.05) !important;
    margin: 20px 0 !important;
}

/* === CUSTOM ANIMATED CLASSES === */
.fade-up {
    animation: fadeUp 0.5s ease both;
}
.fade-up-1 { animation: fadeUp 0.5s ease 0.1s both; }
.fade-up-2 { animation: fadeUp 0.5s ease 0.2s both; }
.fade-up-3 { animation: fadeUp 0.5s ease 0.3s both; }
.fade-up-4 { animation: fadeUp 0.5s ease 0.4s both; }
.fade-up-5 { animation: fadeUp 0.5s ease 0.5s both; }

.slide-left { animation: slideInLeft 0.5s ease both; }
.slide-left-1 { animation: slideInLeft 0.5s ease 0.1s both; }
.slide-left-2 { animation: slideInLeft 0.5s ease 0.2s both; }
.slide-left-3 { animation: slideInLeft 0.5s ease 0.3s both; }
.slide-left-4 { animation: slideInLeft 0.5s ease 0.4s both; }

.scale-in { animation: scaleIn 0.4s ease both; }

.shimmer-box {
    background: linear-gradient(90deg,
        rgba(255,255,255,0.03) 25%,
        rgba(255,255,255,0.07) 50%,
        rgba(255,255,255,0.03) 75%
    );
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 6px;
}

.pulse-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #22c55e;
    animation: pulse 1.5s ease infinite;
}

.glow-border {
    animation: borderGlow 2.5s ease infinite;
}

.float {
    animation: float 3s ease infinite;
}

.typing-effect {
    overflow: hidden;
    white-space: nowrap;
    border-right: 2px solid #3b82f6;
    animation: typing 2s steps(30) infinite, blink 0.8s infinite;
}

.candidate-row-hover {
    transition: all 0.25s ease !important;
}
.candidate-row-hover:hover {
    transform: translateX(4px) !important;
    border-color: rgba(59,130,246,0.4) !important;
}

.score-bar-animated {
    transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
</style>
"""