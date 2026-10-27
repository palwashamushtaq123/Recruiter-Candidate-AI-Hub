# 🚀 Recruiter-Candidate-AI-Hub

An advanced **Dual-Mode Agentic AI Platform** powered by **LangGraph**, **Groq LLM (`openai/gpt-oss-20b`)**, and **Streamlit**. 

This application bridges the gap between hiring managers and job seekers by delivering structured executive recruitment intelligence alongside precision ATS resume optimization and match scoring.

🔗 **Live Demo App:** Click Here to Access the Live Application => [ https://recruiter-candidate-ai-app-y7xpwcqzyypramgaxbd2bi.streamlit.app/ ]

---

## 📌 Application Screenshots

### 1. Main Dashboard & Dual Input Interface
![Main Dashboard](Assets/.Outcome%20-%20Analysis(Dashboard).png)

### 2. Recruiter View: Executive Hiring Report
![Recruiter Executive Report](Assets/Outcome%20-%20Executive-Report(Recruiter).png)

> 💡 **Explore All Outcomes:** Complete visual walkthroughs, skill gap tags, export panels, and sample downloadable PDF reports are available in the [`Assets/`](./Assets/) directory.

---

## 🎯 Project Motivation & Motto

In the modern hiring ecosystem, both recruiters and job candidates face severe bottlenecks:
- **For Recruiters:** Unstructured Job Descriptions (JDs) make it difficult to quickly extract core competencies, experience benchmarks, and compensation bounds.
- **For Candidates:** Applicants apply blind without knowing how well their resume aligns with ATS (Applicant Tracking Systems), leading to rejections without feedback.

**The Motto:** *"Democratize Hiring Intelligence through Agentic Workflows."*

This project provides a clean, dual-purpose ecosystem: **Recruiters** get instant, structured executive summaries for faster decision-making, while **Candidates** receive data-driven ATS match scoring and actionable resume redesign steps.

---

## ✨ Key Features & User Benefits

### 🏢 1. For Recruiters & HR Hiring Managers
* **Instant JD Structuring:** Parses raw job descriptions into precise roles, categories, required experience, and compensation estimates.
* **Independent Executive Reports:** Generates isolated, company-focused PDF and JSON executive reports for candidate shortlisting and internal HR alignment.
* **Skill Extraction:** Automatically tags core technical and soft skill requirements.

### 👤 2. For Job Seekers & Candidates
* **PDF Resume Reader:** Automatically extracts and analyzes uploaded candidate resume PDFs.
* **ATS Compatibility Scoring:** Computes a real-time match score (out of 100) based on JD alignment.
* **Skill Gap Identification:** Highlights missing critical keywords and technical competencies.
* **Actionable Resume Redesign:** Provides direct, step-by-step guidance on how to optimize CV bullet points for the target job.
* **Candidate PDF Export:** Downloads personalized CV optimization reports without cluttering recruiter data.

---

## 🛠️ Tech Stack & System Architecture

* **Framework & UI:** Python, Streamlit (Custom Dark Theme UI)
* **Agentic Framework:** LangGraph (4-Node Orchestrated Pipeline)
* **LLM Engine:** Groq API (`openai/gpt-oss-20b`)
* **PDF Processing & Generation:** PyPDF, ReportLab
* **Deployment:** Deployed live via Streamlit Community Cloud

```
LangGraph 4-Node Pipeline Flow:
┌─────────────────────┐    ┌────────────────────┐    ┌─────────────────────┐    ┌────────────────────┐
│  extract_info_node  │───>│ classify_job_node  │───>│ skill_analysis_node │───>│ hiring_report_node │
└─────────────────────┘    └────────────────────┘    └─────────────────────┘    └────────────────────┘
```

---

## 📁 Project Directory Structure

```text
Recruiter-Candidate-AI-Engine/
├── Assets/                                 # Screenshots, outcomes, and generated sample PDFs
│   ├── Candidate_Resume_Optimization_Report.pdf
│   ├── Job_Report_AI_Technologies.pdf
│   ├──.Outcome - Main Dashboard & Dual Input Interface.png
│   ├── Outcome - Executive-Report(Recruiter).png
│   ├── Outcome - Export option.png
│   ├── Outcome - Resume-Match-Suggestion(candidate).png
│   └── Outcome - Skill-Gap-Tag.png
├── .env                                    # Local environment variables (Git ignored)
├── .env.example                            # Template for API configuration
├── .gitignore                              # Git exclusion file
├── app.py                                  # Main Streamlit interface & PDF handlers
├── graph.py                                # LangGraph workflow compilation
├── nodes.py                                # LangGraph operational state nodes
├── requirements.txt                        # Python dependencies
└── state.py                                # Pydantic/TypedDict state schema
```

---

## 🚀 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Recruiter-Candidate-AI-Engine.git
   cd Recruiter-Candidate-AI-Hub
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Rename `.env.example` to `.env` and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

4. **Run the Streamlit App locally:**
   ```bash
   streamlit run app.py
   ```

---

## 👩‍💻 System Architect & Developer

* **Developer:** Palwasha Sheikh
* **Specialization:** MBA Finance | Data Science & Agentic AI Specialist