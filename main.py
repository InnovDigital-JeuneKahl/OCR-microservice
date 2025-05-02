from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from ocr.schemas import (
    SearchResponse,
    TextResponse,
    SearchRequestForm,
    TextContext
)
from ocr.services import perform_ocr, find_all_sentence_contexts
import os
import tempfile

app = FastAPI()

@app.post("/search", response_model=SearchResponse)
async def search_text(
    file: UploadFile = File(...),
    search_terms: str = Form("")
):
    try:
        # Create temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name
        
        # Perform OCR
        ocr_results = perform_ocr(temp_path)
        
        # Combine paragraphs into single text
        full_text = " ".join(ocr_results)
        
        # Parse search terms
        terms = [term.strip() for term in search_terms.split(",") if term.strip()]
        
        # Find contexts for search terms
        contexts = find_all_sentence_contexts(full_text, terms)
        
        # Clean up temp file
        os.unlink(temp_path)
        
        # Convert to Pydantic model
        response_data = {
            "results": {
                term: [
                    TextContext(**context) for context in term_contexts
                ]
                for term, term_contexts in contexts.items()
            }
        }
        
        return response_data
        
    except Exception as e:
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

@app.post("/get-text", response_model=TextResponse)
async def get_text(file: UploadFile = File(...)):
    try:
        # Create temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name
        
        # Perform OCR
        ocr_results = perform_ocr(temp_path)
        
        # Clean up temp file
        os.unlink(temp_path)
        
        return {"text": ocr_results}
        
    except Exception as e:
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.unlink(temp_path)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)