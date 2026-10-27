import streamlit as st
import json
import io
from graph import app_graph
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Job Analyzer & Resume Optimizer | Palwasha Sheikh",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117 !important;
        color: #f0f6fc !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] li {
        color: #e6edf3 !important;
    }
    
    h1, h2, h3, h4, .stMarkdown {
        color: #f0f6fc !important;
    }
    .main-title {
        font-size: 30px !important;
        color: #58a6ff !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }
    
    /* 100% Forceful Bright Styling for Metrics to fix faint text */
    div[data-testid="metric-container"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        padding: 15px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4) !important;
    }
    div[data-testid="metric-container"] label {
        color: #8b949e !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        opacity: 1 !important;
    }
    div[data-testid="metric-container"] [data-testid="stMetricValue"], 
    div[data-testid="metric-container"] [data-testid="stMetricValue"] div,
    div[data-testid="metric-container"] [data-testid="stMetricValue"] span {
        color: #58a6ff !important;
        font-size: 24px !important;
        font-weight: 900 !important;
        opacity: 1 !important;
    }
    
    textarea, div.stTextArea textarea {
        background-color: #161b22 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
    }
    
    div[data-testid="stFileUploader"] {
        background-color: #161b22 !important;
        border: 2px dashed #30363d !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #161b22 !important;
    }
    div[data-testid="stFileUploader"] button {
        background-color: #21262d !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] div {
        color: #c9d1d9 !important;
    }
    
    div[data-testid="stDownloadButton"] button {
        background-color: #21262d !important;
        color: #58a6ff !important;
        border: 1px solid #58a6ff !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    div[data-testid="stDownloadButton"] button:hover {
        background-color: #30363d !important;
        border-color: #79c0ff !important;
        color: #79c0ff !important;
    }
    
    .badge-dev {
        background: linear-gradient(135deg, #1f6feb, #8957e5);
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        color: #ffffff !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(31, 111, 235, 0.3);
    }
    .tech-tag {
        display: inline-block;
        background-color: #238636;
        color: #ffffff !important;
        padding: 6px 14px;
        margin: 4px;
        border-radius: 18px;
        font-weight: 600;
        font-size: 13px;
    }
    .missing-tag {
        display: inline-block;
        background-color: #da3633;
        color: #ffffff !important;
        padding: 6px 14px;
        margin: 4px;
        border-radius: 18px;
        font-weight: 600;
        font-size: 13px;
    }
    .card-box {
        background-color: #161b22;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def generate_recruiter_pdf(state):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor("#1f6feb"), spaceAfter=8)
    heading_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'], fontSize=12, textColor=colors.HexColor("#238636"), spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor("#24292f"))
    
    story = [
        Paragraph(f"Executive Job Description Report - {str(state.get('company_name', 'Company'))}", title_style),
        Paragraph("System Architect: Palwasha Sheikh | AI Hiring Intelligence", body_style),
        Spacer(1, 8),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor("#d0d7de"), spaceAfter=10),
        
        Paragraph("Job Requirements Overview", heading_style),
        Paragraph(f"<b>Job Title:</b> {str(state.get('job_title', 'N/A'))}", body_style),
        Paragraph(f"<b>Target Company:</b> {str(state.get('company_name', 'N/A'))}", body_style),
        Paragraph(f"<b>Experience Requirement:</b> {str(state.get('required_experience', 'N/A'))}", body_style),
        Paragraph(f"<b>Job Category:</b> {str(state.get('job_category', 'N/A'))}", body_style),
        Paragraph(f"<b>Estimated Compensation:</b> {str(state.get('estimated_salary', 'N/A'))}", body_style),
        Paragraph(f"<b>Required Skills:</b> {', '.join([str(x) for x in state.get('required_skills', [])])}", body_style),
    ]
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

def generate_candidate_pdf(state):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor("#1f6feb"), spaceAfter=8)
    heading_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'], fontSize=12, textColor=colors.HexColor("#238636"), spaceBefore=10, spaceAfter=4)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor("#24292f"))
    
    match_txt = state.get('match_analysis', 'N/A')
    if isinstance(match_txt, list):
        match_txt = "<br/>".join([str(x) for x in match_txt])
    else:
        match_txt = str(match_txt)
        
    missing_list = state.get('missing_skills', [])
    missing_str = ", ".join([str(x) for x in missing_list]) if missing_list else "None"

    story = [
        Paragraph(f"Candidate Resume Optimization Report - {str(state.get('job_title', 'Role'))}", title_style),
        Paragraph("Generated via AI Career Optimizer | System Architect: Palwasha Sheikh", body_style),
        Spacer(1, 8),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor("#d0d7de"), spaceAfter=10),
        
        Paragraph("Resume Fit & Gap Analysis", heading_style),
        Paragraph(f"<b>Target Role:</b> {str(state.get('job_title', 'N/A'))} at {str(state.get('company_name', 'Company'))}", body_style),
        Paragraph(f"<b>ATS Compatibility Score:</b> {str(state.get('ats_score', '75'))}/100", body_style),
        Paragraph(f"<b>Missing Skills / Keywords:</b> {missing_str}", body_style),
        Spacer(1, 4),
        Paragraph(f"<b>Tailored Improvement Steps:</b><br/>{match_txt}", body_style),
    ]
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

with st.sidebar:
    st.markdown("""
        <div class="badge-dev">
            <p style="margin:0; font-size:11px; text-transform:uppercase; letter-spacing:1px; color:#ffffff;">Created By</p>
            <h2 style="margin:4px 0 0 0; font-size:21px; font-weight:800; color:#ffffff;">Palwasha Sheikh</h2>
            <p style="margin:4px 0 0 0; font-size:12px; color:#ffffff; opacity:0.9;">MBA Finance | Data Science & Agentic AI Specialist</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚡ Dual-Mode System")
    st.markdown("""
    - **Recruiter View:** Pure Job Description Insights & Hiring Report
    - **Candidate View:** Separate ATS Match & Resume Optimization
    """)
    st.markdown("---")
    st.caption("🚀 Recruiter-Ready Portfolio App")

st.markdown("<h1 class='main-title'>📄 AI Job Description & Resume Optimizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#c9d1d9; font-size:15px;'>Independent modules: Recruiter mode generates hiring reports for companies, while Candidate mode provides personalized CV matching.</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    sample_jd = """We are seeking a Senior Data & AI Engineer at ABC Technologies with 3+ years experience in Python, LangGraph, FastAPI, Docker, and Agentic Workflows. Strong analytical and communication skills required."""
    user_jd = st.text_area("📋 Paste Job Description Here:", value=sample_jd, height=140)

with col2:
    st.markdown("👤 **Candidate Resume Upload (PDF) [For Candidate Mode]:**")
    uploaded_file = st.file_uploader("Upload your resume PDF file here:", type=["pdf"])
    
    resume_text = ""
    if uploaded_file is not None:
        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                resume_text += page.extract_text()
            st.success("✅ Resume PDF Uploaded & Read Successfully!")
        except Exception:
            st.error("Error reading PDF file.")
            
    manual_resume = st.text_area("Or Paste Resume Summary:", value="MBA Finance background transitioning to Data Science & Agentic AI. Skilled in Python, SQL, and LangGraph.", height=60)
    
    final_resume_input = resume_text if resume_text else manual_resume

if st.button("🚀 Run Advanced LangGraph Analysis", type="primary", use_container_width=True):
    if not user_jd.strip():
        st.warning("Please provide a valid job description.")
    else:
        with st.spinner("Executing 4-Node LangGraph State Pipeline via Groq..."):
            initial_state = {
                "job_description": user_jd,
                "user_resume": final_resume_input,
                "job_title": None,
                "company_name": None,
                "required_experience": None,
                "required_skills": [],
                "job_category": None,
                "employment_type": None,
                "technical_skills": [],
                "soft_skills": [],
                "top_skills": [],
                "ats_score": 0,
                "estimated_salary": None,
                "missing_skills": [],
                "match_analysis": None,
                "hiring_report": None,
                "current_step": "Started"
            }
            
            final_state = app_graph.invoke(initial_state)
            
        st.success("✅ Analysis Successfully Compiled!")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Job Title", final_state.get("job_title", "N/A"))
        m2.metric("Est. Salary", final_state.get("estimated_salary", "N/A"))
        m3.metric("Job Domain", final_state.get("job_category", "N/A"))
        m4.metric("ATS Match Score", f"{final_state.get('ats_score', 75)}/100")
        
        st.markdown("---")
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Executive Report (Recruiter View)", 
            "🎯 Resume Match & Suggestions (Candidate View)", 
            "🏷️ Skill Gap & Tags", 
            "📥 Export Options"
        ])
        
        with tab1:
            st.subheader(f"📌 Job Report: {final_state.get('company_name', 'Company')} Hiring")
            st.markdown("<div class='card-box'>", unsafe_allow_html=True)
            st.markdown(final_state.get("hiring_report", "No report generated."))
            st.markdown("</div>", unsafe_allow_html=True)
            
        with tab2:
            st.subheader("🎯 Candidate Resume Fit & Optimization")
            st.markdown("<div class='card-box'>", unsafe_allow_html=True)
            st.markdown(f"### 📊 ATS Compatibility Score: {final_state.get('ats_score', 75)} / 100")
            st.markdown("---")
            st.markdown("### 💡 Tailored Recommendations to Redesign Your Resume:")
            match_data = final_state.get("match_analysis", "No resume provided.")
            if isinstance(match_data, list):
                for item in match_data:
                    st.write(f"- {str(item)}")
            else:
                st.write(str(match_data))
            st.markdown("</div>", unsafe_allow_html=True)
            
        with tab3:
            st.subheader("🚨 Missing Keywords / Skills in Your CV")
            missing_list = final_state.get("missing_skills", [])
            if missing_list:
                st.markdown("".join([f"<span class='missing-tag'>❌ {str(s)}</span>" for s in missing_list]), unsafe_allow_html=True)
            else:
                st.success("🎉 No major skills missing! Your resume matches the job requirements well.")
                
            st.subheader("🔥 Top Priority Core Skills")
            st.markdown("".join([f"<span class='tech-tag top-tag'>🔥 {str(s)}</span>" for s in final_state.get("top_skills", [])]), unsafe_allow_html=True)
            
            st.subheader("🛠️ Required Technical Skills")
            st.markdown("".join([f"<span class='tech-tag'>{str(s)}</span>" for s in final_state.get("technical_skills", [])]), unsafe_allow_html=True)
            
        with tab4:
            st.subheader("📥 Export Independent Reports")
            col_exp1, col_exp2 = st.columns(2)
            
            company_slug = str(final_state.get('company_name', 'Company')).replace(" ", "_")
            
            with col_exp1:
                st.markdown("#### 🏢 Recruiter Report (Company View)")
                recruiter_pdf = generate_recruiter_pdf(final_state)
                st.download_button(
                    label="📥 Download Recruiter PDF",
                    data=recruiter_pdf,
                    file_name=f"Job_Report_{company_slug}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
                st.markdown("#### ⚙️ Recruiter JSON Data")
                st.download_button(
                    label="📥 Download Recruiter JSON",
                    data=json.dumps({
                        "job_title": final_state.get("job_title"),
                        "company_name": final_state.get("company_name"),
                        "required_experience": final_state.get("required_experience"),
                        "job_category": final_state.get("job_category"),
                        "estimated_salary": final_state.get("estimated_salary"),
                        "required_skills": final_state.get("required_skills")
                    }, indent=4),
                    file_name=f"Job_Data_{company_slug}.json",
                    mime="application/json",
                    use_container_width=True
                )
                
            with col_exp2:
                st.markdown("#### 👤 Candidate Optimization Report")
                candidate_pdf = generate_candidate_pdf(final_state)
                st.download_button(
                    label="📥 Download Candidate PDF",
                    data=candidate_pdf,
                    file_name="Candidate_Resume_Optimization_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
                st.markdown("#### ⚙️ Candidate JSON Data")
                st.download_button(
                    label="📥 Download Candidate JSON",
                    data=json.dumps({
                        "ats_score": final_state.get("ats_score"),
                        "missing_skills": final_state.get("missing_skills"),
                        "recommendations": final_state.get("match_analysis")
                    }, indent=4),
                    file_name="Candidate_Match_Data.json",
                    mime="application/json",
                    use_container_width=True
                )