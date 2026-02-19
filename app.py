# app.py
import streamlit as st
import requests
import os

# -----------------------------
# Get your API key and workflow URL from environment variables
# -----------------------------
API_KEY = os.environ.get("OPENAI_KEY")  # Store your key in Streamlit Secrets
WORKFLOW_URL = os.environ.get("WORKFLOW_URL")  # Optional: store your workflow URL as a secret too

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Resume Screening Tool")
st.markdown("Enter the job description and screening parameters:")

# Input fields
jd = st.text_area("Job Description")
topN = st.number_input("Top N candidates", min_value=1, max_value=50, value=5)
threshold = st.slider("Threshold", 0.0, 1.0, 0.75)

# Button to run the screening
if st.button("Run Screening"):
    if not jd.strip():
        st.warning("Please enter a job description.")
    else:
        # Ensure API key and URL are set
        if not API_KEY or not WORKFLOW_URL:
            st.error("API key or workflow URL is not set. Please check your environment variables.")
        else:
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "jobDescription": jd,
                "topN": int(topN),
                "threshold": float(threshold)
            }

            try:
                resp = requests.post(WORKFLOW_URL, headers=headers, json=payload)
                if resp.status_code == 200:
                    result = resp.json()
                    st.success("Screening completed!")
                    st.json(result)
                else:
                    st.error(f"Error {resp.status_code}: {resp.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
