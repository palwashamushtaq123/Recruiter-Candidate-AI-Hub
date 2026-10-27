import os
import json
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from state import JobState
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_info_node(state: JobState):
    jd = state["job_description"]
    system_prompt = "You are an expert HR Data Extractor. Respond ONLY in JSON format."
    user_prompt = f"""
    Extract details from this Job Description:
    {jd}

    Return JSON with fields:
    "job_title": string,
    "company_name": string,
    "required_experience": string,
    "required_skills": list of strings,
    "estimated_salary": string
    """
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)])
        content = response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
            
        parsed = json.loads(content)
        return {
            "job_title": parsed.get("job_title", "Data & AI Specialist"),
            "company_name": parsed.get("company_name", "Leading Tech Firm"),
            "required_experience": parsed.get("required_experience", "2+ Years"),
            "required_skills": parsed.get("required_skills", []),
            "estimated_salary": parsed.get("estimated_salary", "$90,000 - $130,000"),
            "current_step": "Information Extracted"
        }
    except Exception:
        return {
            "job_title": "AI & Data Engineer",
            "company_name": "Tech Enterprise",
            "required_experience": "2-4 Years",
            "required_skills": ["Python", "LangGraph", "SQL"],
            "estimated_salary": "$90,000 - $130,000",
            "current_step": "Extraction Fallback"
        }

def classify_job_node(state: JobState):
    jd = state["job_description"]
    system_prompt = "You are a Tech Career Classifier. Respond ONLY in JSON."
    user_prompt = f"""
    Classify this job description:
    {jd}
    Return JSON:
    "job_category": string,
    "employment_type": string
    """
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)])
        content = response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        parsed = json.loads(content)
        return {
            "job_category": parsed.get("job_category", "Artificial Intelligence & Data"),
            "employment_type": parsed.get("employment_type", "Full-time / Hybrid"),
            "current_step": "Job Classified"
        }
    except Exception:
        return {
            "job_category": "Agentic AI & Data Science",
            "employment_type": "Full-time",
            "current_step": "Classification Fallback"
        }

def skill_analysis_node(state: JobState):
    jd = state["job_description"]
    resume = state.get("user_resume", "")
    system_prompt = "You are an expert ATS & Resume Optimization Specialist. Respond ONLY in JSON format."
    user_prompt = f"""
    Compare the Job Description against the Candidate Resume.
    Job Description: {jd}
    Candidate Resume Text: {resume if resume else 'Not Provided'}

    Return JSON with fields:
    "technical_skills": list of technical skills required in JD,
    "soft_skills": list of soft skills required in JD,
    "top_skills": list of 3 crucial skills,
    "ats_score": integer match score out of 100,
    "missing_skills": list of missing skills in resume compared to JD,
    "recommendations": string containing clear instructions on how to improve and redesign the resume for this job.
    """
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=user_prompt)])
        content = response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        parsed = json.loads(content)
        
        rec_val = parsed.get("recommendations", "Tailor your resume by adding specific keywords and highlighting relevant projects.")
        if isinstance(rec_val, list):
            rec_val = "\n".join([str(item) for item in rec_val])
            
        return {
            "technical_skills": parsed.get("technical_skills", []),
            "soft_skills": parsed.get("soft_skills", []),
            "top_skills": parsed.get("top_skills", [])[:3],
            "ats_score": parsed.get("ats_score", 75),
            "missing_skills": parsed.get("missing_skills", []),
            "match_analysis": str(rec_val),
            "current_step": "Skill Matrix & Match Generated"
        }
    except Exception:
        return {
            "technical_skills": ["Python", "LangGraph", "SQL"],
            "soft_skills": ["Communication", "Problem Solving"],
            "top_skills": ["Python", "LangGraph", "FastAPI"],
            "ats_score": 70,
            "missing_skills": ["Docker", "FastAPI"],
            "match_analysis": "Your profile shows strong foundational skills. To improve compatibility for this role, explicitly highlight your hands-on experience with FastAPI and containerization tools like Docker.",
            "current_step": "Fallback Analysis"
        }

def hiring_report_node(state: JobState):
    report = f"""
# 📋 Executive Job Description Report (Recruiter View)

- **Job Title:** {state.get('job_title')}
- **Target Organization:** {state.get('company_name')}
- **Experience Requirement:** {state.get('required_experience')}
- **Job Category:** {state.get('job_category')}
- **Estimated Compensation:** 💰 **{state.get('estimated_salary')}**

---
*Generated via AI Job Analyzer | System Architect: Palwasha Sheikh*
    """
    return {
        "hiring_report": report,
        "current_step": "Complete"
    }