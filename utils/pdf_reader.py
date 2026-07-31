import pypdf
import io

def extract_text_from_pdf(uploaded_file):
    """Extract text from a Streamlit uploaded PDF file."""
    try:
        pdf_bytes = uploaded_file.read()
        pdf_reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        text = clean_text(text)
        return text
    
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def clean_text(text):
    """Clean extracted text."""
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(cleaned_lines)