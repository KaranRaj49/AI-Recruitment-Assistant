from langchain_core.prompts import PromptTemplate

# Single master prompt that returns everything as JSON
master_prompt = PromptTemplate(
    input_variables=["resume_text", "jd_text"],
    template="""
You are an expert HR assistant. Analyze the resume against the job description and return a JSON response.

Resume:
{resume_text}

Job Description:
{jd_text}

Return ONLY a valid JSON object with this exact structure, no extra text, no markdown, no backticks:
{{
    "summary": "Brief candidate summary with name, education, experience, and top skills",
    "matching_skills": ["skill1", "skill2"],
    "missing_skills": ["skill1", "skill2"],
    "extra_skills": ["skill1", "skill2"],
    "score": 85,
    "recommendation": "Hire",
    "justification": "Short reason for recommendation",
    "technical_questions": ["question1", "question2", "question3"],
    "hr_questions": ["question1", "question2", "question3"]
}}

Rules:
- score must be a number between 0 and 100
- recommendation must be exactly one of: Hire, Interview, Reject
- all lists must have at least 2 items
- return ONLY the JSON, nothing else
"""
)