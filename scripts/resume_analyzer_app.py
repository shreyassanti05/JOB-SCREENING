import streamlit as st
import tempfile
import os
from resume_analyzer import analyze_resume_file

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .upload-box {
        border: 2px dashed #4CAF50;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
    }
    .report-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("📊 Resume Analyzer")
st.markdown("""
    Upload a resume to get personalized feedback, including:
    - Key skills and expertise
    - Areas of specialization
    - Recommended career paths
    - Strengths and unique value
    - Areas for development
""")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF resume", type=['pdf'])

if uploaded_file is not None:
    # Create a temporary file to store the uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Add a analyze button
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume... This may take a minute."):
            try:
                # Analyze the resume
                feedback = analyze_resume_file(tmp_file_path)
                
                # Display the results in a nice format
                st.markdown("""
                    <div class="report-box">
                        {}
                    </div>
                """.format(feedback.replace("\n", "<br>")), unsafe_allow_html=True)
                
                # Add download button for the report
                st.download_button(
                    label="Download Analysis Report",
                    data=feedback,
                    file_name="resume_analysis_report.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred while analyzing the resume: {str(e)}")
            finally:
                # Clean up the temporary file
                os.unlink(tmp_file_path)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Powered by AI - Providing intelligent resume analysis and career guidance</p>
    </div>
""", unsafe_allow_html=True) 