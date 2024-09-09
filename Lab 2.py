import streamlit as st
import openai

# Load the LLM key from secrets
llm_api_key = st.secrets["llm_api_key"]

# Initialize the OpenAI API
openai.api_key = llm_api_key

# Test to confirm the key is loaded successfully
st.title("LLM API Key Loaded")
st.write("API key loaded successfully from Streamlit Secrets.")

# Load the LLM key from secrets
llm_api_key = st.secrets["llm_api_key"]

# Initialize the OpenAI API
openai.api_key = llm_api_key

# Sidebar with options for summary type
st.sidebar.title("Summary Options")

# Select the summary type (this stays the same)
summary_type = st.sidebar.radio(
    "Select summary type:",
    ("100 words", "2 paragraphs", "5 bullet points")
)

# Checkbox for model selection: "Use Advanced Model"
use_advanced_model = st.sidebar.checkbox("Use Advanced Model")

# Determine the model based on the checkbox
model = "gpt-4o" if use_advanced_model else "gpt-4o-mini"

# File uploader widget to upload a document
uploaded_file = st.file_uploader("Upload a file", type=["txt", "md", "csv", "docx", "pdf"])

# Function to read the content of the uploaded file (for different file types)
def read_uploaded_file(file):
    if file is not None:
        if file.type == "text/plain":
            return file.read().decode("utf-8")
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            import docx
            doc = docx.Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        elif file.type == "text/csv":
            import pandas as pd
            df = pd.read_csv(file)
            return df.to_string()
        elif file.type == "application/pdf":
            import fitz
            pdf_text = ""
            with fitz.open(stream=file.read(), filetype="pdf") as doc:
                for page in doc:
                    pdf_text += page.get_text()
            return pdf_text
    return None

# Read the uploaded document content
document_text = read_uploaded_file(uploaded_file)

# If a document is uploaded, let the user generate the summary
if document_text:
    # Generate a summary based on the selected options
    def generate_summary(model, summary_type, document_text):
        # Customize prompt based on summary type
        if summary_type == "100 words":
            prompt = f"Summarize this document in 100 words:\n\n{document_text}"
        elif summary_type == "2 paragraphs":
            prompt = f"Summarize this document in 2 connecting paragraphs:\n\n{document_text}"
        elif summary_type == "5 bullet points":
            prompt = f"Summarize this document in 5 bullet points:\n\n{document_text}"

        # Make the actual API call to OpenAI (or your LLM provider)
        stream = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": prompt}],
            stream=True  # Enable streaming
        )

        # Collect and return the streamed response
        full_response = ""
        for chunk in stream:
            full_response += chunk.choices[0].delta.get('content', '')
            st.write(chunk.choices[0].delta.get('content', ''))  # Display streamed response

        return full_response

    # Display the selected model and summary type
    st.title("Document Summarizer")
    st.write(f"Using model: {model}")
    st.write(f"Summary type: {summary_type}")

    # Button to generate the summary
    if st.button("Generate Summary"):
        summary = generate_summary(model, summary_type, document_text)
        st.write("Generated Summary:")
        st.write(summary)
else:
    st.warning("Please upload a file to summarize.")
