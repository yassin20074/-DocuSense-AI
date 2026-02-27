#Calling the libraries 
from fastapi import FastAPI, UploadFile, File
from ocr_model import extract_text_from_image
from nlp_model import extract_entities, summarize_text

app = FastAPI(title="DocuScan AI Pro")

#Endpoint POST is for receiving and analyzing files
@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    # Read the file directly into memory (RAM) 
    file_bytes = await file.read()

    #Text extraction using enhanced OpenCV 
    text = extract_text_from_image(file_bytes)

    #If there is no image return the message
    if not text.strip():
        return {"error": "Could not extract text. Please check image quality."}

    # Word processing 
    entities = extract_entities(text)
    summary = summarize_text(text)

 # Return the result
    return {
        "filename": file.filename,
        "extracted_text": text,
        "entities": entities,
        "summary": summary
    }
