# 🤖 AI Recruitment Assistant Dashboard
> **Smarter Hiring. Faster Decisions. Powered by AI.**

An intelligent HR automation tool that eliminates manual resume screening. Upload resumes and a job description — the AI analyzes every candidate in seconds and gives you a ranked shortlist with scores, skill gaps, and ready-to-use interview questions.

👤 **Developed by: Karan**

---

## 🌐 Live Demo
👉 **[Click here to try the live app](https://YOUR-USERNAME-ai-recruitment-assistant.streamlit.app)**

---

## ✨ Features
| Feature | Description |
|---|---|
| 📄 Multi-Resume Upload | Upload one or multiple resume PDFs at once |
| 📋 Resume Summary | AI extracts name, education, experience and skills |
| 🎯 Skill Match Analysis | Matching, Missing and Extra skills vs Job Description |
| 📊 Match Score | Scores each candidate from 0 to 100% |
| 💡 HR Recommendation | AI recommends Hire, Interview or Reject with justification |
| ❓ Interview Questions | Auto-generates technical and HR questions per candidate |
| 🏆 Ranking Dashboard | Sorts all candidates by score for easy comparison |
| ⬇️ CSV Export | Download full results as a spreadsheet |
| ✨ Animated UI | Shimmer loading, typing indicators, fade-in effects |
| 🚀 Live Deployment | Hosted on Streamlit Cloud — no setup needed |

---

## 🎨 UI Highlights
- 🌊 **Shimmer loading** while AI processes resumes
- ⌨️ **Typing indicator** with live cursor animation
- 💫 **Floating avatars** with smooth motion
- 🎯 **Animated score** that scales in dramatically
- 📋 **Slide-in questions** one by one
- 🔵 **Glowing borders** that pulse on active elements
- 🖱️ **Hover effects** on all interactive elements
- ✨ **Fade-up animations** on every section load

---

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Frontend | Streamlit + Custom CSS Animations |
| AI Pipeline | LangChain LCEL |
| LLM | LLaMA 3.1 8B via Groq |
| PDF Processing | PyPDF |
| Data Handling | Pandas |
| Deployment | Streamlit Cloud |
| Language | Python 3.10+ |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Recruitment-Assistant.git
cd AI-Recruitment-Assistant

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key — create a .env file
GROQ_API_KEY=your_groq_api_key_here

# 5. Run the app
streamlit run app.py
```

👉 Get your **free** Groq API key at: https://console.groq.com

---

## 📁 Project Structure

AI-Recruitment-Assistant/
├── app.py # Main Streamlit app + animations
├── requirements.txt # Dependencies
├── .env # API keys (never upload to GitHub)
├── .streamlit/
│ └── secrets.toml # Streamlit Cloud secrets (never upload)
├── components/
│ ├── sidebar.py # Animated sidebar UI
│ ├── uploader.py # Upload status cards
│ ├── ranking.py # Animated ranking table + CSV
│ └── styles.py # All CSS animations and styles
├── utils/
│ ├── pdf_reader.py # PDF text extraction
│ ├── prompts.py # LangChain master prompt
│ └── parser.py # Output parser
├── ai/
│ ├── llm.py # LLM setup (Groq + Streamlit secrets)
│ └── chains.py # LangChain LCEL pipeline
├── data/ # Sample resumes and JDs
└── outputs/ # Exported CSV files


---

## 📖 How To Use
1. Open the app at the live URL or `http://localhost:8501`
2. Upload a **Job Description PDF** in the sidebar
3. Upload one or more **Resume PDFs** in the sidebar
4. Click **"🚀 Analyze Resumes"** and wait 20-30 seconds
5. View AI analysis across 5 tabs for each candidate:
   - 📋 Resume Summary
   - 🎯 Skill Match (Matching / Missing / Extra)
   - 📊 Match Score (0-100%)
   - 💡 HR Recommendation (Hire / Interview / Reject)
   - ❓ Interview Questions (Technical + HR)
6. Scroll down to see the **Ranking Dashboard**
7. Click **"Download Results as CSV"** to export

---

## 🔮 Future Enhancements
- 📊 Radar Chart visualization for candidate comparison
- 💬 Chat with Resume using RAG
- 🔊 Voice summary with text-to-speech
- 📧 Auto email draft generator
- 🔐 Authentication system
- 🗄️ Database integration (SQLite / PostgreSQL)

---

## 🙏 Acknowledgements
[LangChain](https://langchain.com) • [Groq](https://groq.com) • [Streamlit](https://streamlit.io)

---

<div align="center">
Made with ❤️ by Karan and Varoon
</div>