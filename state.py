from typing import List, TypedDict, Optional

class JobState(TypedDict):
    job_description: str
    user_resume: Optional[str]
    job_title: Optional[str]
    company_name: Optional[str]
    required_experience: Optional[str]
    required_skills: List[str]
    job_category: Optional[str]
    employment_type: Optional[str]
    technical_skills: List[str]
    soft_skills: List[str]
    top_skills: List[str]
    ats_score: Optional[int]
    estimated_salary: Optional[str]
    match_analysis: Optional[str]
    hiring_report: Optional[str]
    current_step: Optional[str]