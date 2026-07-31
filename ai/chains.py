import json
from ai.llm import get_llm
from utils.prompts import master_prompt
from langchain_core.output_parsers import StrOutputParser

# Initialize LLM and chain
llm = get_llm()
parser = StrOutputParser()

# Single master chain
master_chain = master_prompt | llm | parser


def analyze_resume(resume_text, jd_text):
    """Run master chain and return structured JSON result."""

    print("Running AI analysis...")

    raw_output = master_chain.invoke({
        "resume_text": resume_text,
        "jd_text": jd_text
    })

    # Clean output - remove markdown if present
    cleaned = raw_output.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]
        if cleaned.startswith("json"):
            cleaned = cleaned[4:]
    cleaned = cleaned.strip()

    # Parse JSON
    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        result = {
            "summary": raw_output,
            "matching_skills": [],
            "missing_skills": [],
            "extra_skills": [],
            "score": 0,
            "recommendation": "Interview",
            "justification": "Could not parse AI response",
            "technical_questions": [],
            "hr_questions": []
        }

    print(f"Analysis complete! Score: {result.get('score', 0)}")
    return result