import PyPDF2

def get_pdf_text(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
        return None
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    return text


def split_text_into_chunks(text, chunk_size=500, chunk_overlap=50):
    """Splits text into chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - chunk_overlap  # Move the starting point
    return chunks