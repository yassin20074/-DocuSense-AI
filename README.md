# 📄 DocuSense AI: Intelligent Document Processing

**DocuSense AI** is a high-performance pipeline that converts unstructured document images into structured data using **Computer Vision (OpenCV)** and **Transformers (NLP)**.



## 🎯 Key Capabilities
- **In-Memory Logic:** Processing via `io.BytesIO` for maximum speed and security (RAM-only).
- **Advanced OCR Tuning:** OpenCV-based noise reduction and thresholding for high-accuracy text extraction.
- **Deep NLP Analysis:** - **Entity Extraction:** Named Entity Recognition (NER) mapped to human-readable labels.
  - **Abstractive Summarization:** Condensing long documents into key insights using BART.

## 🛠️ Tech Stack
- **Backend:** FastAPI (Asynchronous)
- **Vision & OCR:** OpenCV, Tesseract, Pillow
- **NLP Models:** HuggingFace Transformers (BERT, BART)

# Output Example
{
  "filename": "document.png",
  "extracted_text": "Full text from the document...",
  "entities": [
    {"word": "John Doe", "label": "Person", "score": 0.98},
    {"word": "Google", "label": "Organization", "score": 0.95}
  ],
  "summary": "This document talks about John Doe's work at Google..."
}


# Future Improvements
Add logging for production monitoring.
Integrate database storage for document history.
Support bulk uploads and async processing.
Improve security checks on uploaded files.

# made by: eng.yassin sanad 

