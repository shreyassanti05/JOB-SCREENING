import pdfplumber
import ollama
from collections import defaultdict
import re
from typing import Dict, List, Tuple

def parse_resume(pdf_path: str) -> str:
    """Extract text from a PDF resume."""
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def analyze_resume(cv_text: str) -> Dict:
    """Analyze resume content using AI to provide personalized feedback."""
    # Prepare prompts for different aspects of analysis
    prompts = {
        "skills": "Analyze this resume and list the key technical and soft skills, with their proficiency levels:\n\n",
        "expertise": "Identify the main areas of expertise and years of experience in each area from this resume:\n\n",
        "career_paths": "Based on the skills and experience in this resume, suggest 3-5 potential career paths or job roles that would be a good fit:\n\n",
        "strengths": "What are the candidate's main strengths and unique selling points based on this resume?\n\n",
        "improvements": "What areas could the candidate improve or develop further based on this resume?\n\n"
    }
    
    analysis = {}
    
    for aspect, prompt in prompts.items():
        response = ollama.chat(
            model="gemma:2b",
            messages=[{"role": "user", "content": prompt + cv_text}]
        )
        analysis[aspect] = response["message"]["content"]
    
    return analysis

def generate_feedback_report(analysis: Dict) -> str:
    """Generate a formatted feedback report from the analysis."""
    report = """
📊 RESUME ANALYSIS REPORT
========================

🎯 Key Skills & Expertise
------------------------
{skills}

💪 Areas of Expertise
--------------------
{expertise}

🚀 Recommended Career Paths
-------------------------
{career_paths}

✨ Strengths & Unique Value
-------------------------
{strengths}

📈 Areas for Development
----------------------
{improvements}
""".format(**analysis)
    
    return report

def analyze_resume_file(pdf_path: str) -> str:
    """Main function to analyze a resume and generate feedback."""
    # Parse the resume
    cv_text = parse_resume(pdf_path)
    
    # Analyze the resume
    analysis = analyze_resume(cv_text)
    
    # Generate and return the feedback report
    return generate_feedback_report(analysis)

if __name__ == "__main__":
    # Example usage
    pdf_path = "../data/CVs1/cv1.pdf"  # Update with actual path
    feedback = analyze_resume_file(pdf_path)
    print(feedback) 