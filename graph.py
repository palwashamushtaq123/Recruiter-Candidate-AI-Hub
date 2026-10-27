from langgraph.graph import StateGraph, END
from state import JobState
from nodes import extract_info_node, classify_job_node, skill_analysis_node, hiring_report_node

def build_graph():
    workflow = StateGraph(JobState)
    workflow.add_node("extract_info", extract_info_node)
    workflow.add_node("classify_job", classify_job_node)
    workflow.add_node("skill_analysis", skill_analysis_node)
    workflow.add_node("hiring_report", hiring_report_node)

    workflow.set_entry_point("extract_info")
    workflow.add_edge("extract_info", "classify_job")
    workflow.add_edge("classify_job", "skill_analysis")
    workflow.add_edge("skill_analysis", "hiring_report")
    workflow.add_edge("hiring_report", END)

    return workflow.compile()

app_graph = build_graph()