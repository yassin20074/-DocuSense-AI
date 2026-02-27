#sanadDocuScan AI Pro

**DocuScan AI Pro** is a professional document analysis system that combines **OCR** and **NLP** to extract, analyze, and summarize text from images or scanned documents. The project is designed with a modular architecture suitable for production-level deployments.

---

## 🌟 Key Features

- **Advanced OCR:** Uses OpenCV for preprocessing and `pytesseract` for high-accuracy text extraction.
- **NER & Summarization:** Utilizes HuggingFace Transformers (BERT for NER, BART for summarization) to extract entities and generate concise summaries.
- **FastAPI Integration:** Fully functional API to upload and analyze documents in real-time.
- **Structured Output:** Returns JSON with extracted text, named entities, and a summarized version.
- **Modular Architecture:** Core modules are separated for maintainability and scalability.
- **Production Ready:** Can be easily extended with logging, database storage, and asynchronous processing.

---

## 📁 Project Structure

```text
── ocr_model.py       # OCR pipeline (OpenCV + Tesseract)
── nlp_model.py       # NLP pipeline (NER + Summarization)
├── main.py                # FastAPI server and endpoints
├── requirements.txt       # Python dependencies
└── README.md

## 🛠️ Technical Stack
Language: Python 3.10+
OCR: pytesseract, OpenCV, PIL
NLP: Transformers (BERT & BART)
API: FastAPI
Data Processing: NumPy
Deployment: Compatible with local, Colab, or cloud servers

## 📊 Output Example
{
  "filename": "document.png",
  "extracted_text": "Full text from the document...",
  "entities": [
    {"word": "John Doe", "label": "Person", "score": 0.98},
    {"word": "Google", "label": "Organization", "score": 0.95}
  ],
  "summary": "This document talks about John Doe's work at Google..."
}

## 🏗️ Future Improvements
Add logging for production monitoring.
Integrate database storage for document history.
Support bulk uploads and async processing.
Improve security checks on uploaded files.

# made by: yassin sanad

 aassaassaassaab
