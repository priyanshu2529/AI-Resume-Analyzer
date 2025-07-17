import streamlit as st
import PyPDF2
import io

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer (Basic)")
st.write("Upload your resume (PDF) and we'll extract the text.")

# File upload
uploaded_file = st.file_uploader("Choose a resume PDF", type="pdf")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

if uploaded_file is not None:
    # Display file name
    st.success(f"Uploaded: {uploaded_file.name}")

    # Extract text
    with st.spinner("Extracting text..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    # Show text output
    st.subheader("📄 Extracted Resume Text:")
    st.text_area("Text Output", resume_text, height=400)

from scoring import load_keywords, find_skills

# Load skill keywords
keywords = load_keywords()
skills_found, resume_score = find_skills(resume_text, keywords)

st.subheader("🎯 Skills Found in Resume:")
for category, skills in skills_found.items():
    st.markdown(f"**{category}**: {', '.join(skills) if skills else '❌ None'}")

st.subheader("📊 Resume Skill Match Score:")
st.progress(resume_score)
st.write(f"Your resume scored **{resume_score}/100** based on skill matching.")
from resume_parser import check_grammar

st.subheader("✏️ Grammar & Writing Suggestions")
grammar_issues = check_grammar(resume_text)

if grammar_issues:
    for i, issue in enumerate(grammar_issues[:10]):  # Show top 10 issues
        st.markdown(f"**Issue {i+1}:** {issue['message']}")
        st.code(issue['error'])
        if issue['suggestion']:
            st.markdown(f"💡 Suggestion: `{issue['suggestion'][0]}`")
        st.markdown("---")
else:
    st.success("No grammar issues found 🎉")
