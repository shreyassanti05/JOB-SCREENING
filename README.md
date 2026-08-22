# Job Screening API

An AI-powered tool that automates resume screening and candidate evaluation.

## Overview
This project uses Natural Language Processing (NLP) to parse resumes and compare them against job descriptions. It automates the tedious process of manual resume screening, highlighting candidates who match the required skills and experience, and generating personalized cover letters.

## Key Features
- **Resume Parsing:** Extracts key information from candidate resumes.
- **Job Matching:** Compares candidate profiles against job descriptions to score fit.
- **Cover Letter Generation:** Uses Generative AI to automatically draft personalized cover letters for candidates based on their match.

## Technologies Used
- **Programming Language:** Python
- **AI/ML:** NLP, Generative AI (AIML API - Gemma)
- **Libraries:** Requests, Pandas

## Project Structure
```text
JOB-SCREENING/
│
├── data/
│   ├── jd_summaries.json        # Precomputed summaries
│   └── job_description.csv      # Dataset of job descriptions
├── scripts/
│   ├── app.py                   # Main application script
│   ├── cover_letter_generator.py# Logic for cover letter creation
│   ├── generate_cover_letter.py # API integration script for generation
│   ├── job_screening.py         # Screening logic and scoring
│   ├── resume_analyzer.py       # Parsing resumes
│   └── resume_analyzer_app.py   # Frontend/App for the analyzer
├── .env.example                 # Environment variables template
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyassanti05/JOB-SCREENING.git
   cd JOB-SCREENING
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Copy `.env.example` to `.env` and add your `AIML_API_KEY`.

## Usage

Run the main application script:
```bash
cd scripts
python app.py
```

## Interview Talking Points
- **Why did you build this?** To solve a real-world HR problem: the time-consuming process of manually reviewing hundreds of resumes for a single job posting.
- **How does the matching work?** It processes the text of the resume and the job description, extracting keywords and semantic meaning to compute a similarity or match score.
- **How is the cover letter generated?** It uses the Gemma 2B model via the AIML API, passing the parsed resume and job description as a prompt to generate a confident, tailored cover letter.