from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.query_service import ask_question
import os
import shutil
from pathlib import Path

router = APIRouter()

# Define data folder path
DATA_FOLDER = Path(__file__).parent.parent.parent / "data"

@router.get("/")
def home():
    return {"message": "AI Knowledge Base API"}

@router.post("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {"answer": answer}

@router.post("/upload-documents")
async def upload_documents(file: UploadFile = File(...)):
    """
    Upload PDF documents to the data folder
    """
    # Validate file type
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        # Create data folder if it doesn't exist
        DATA_FOLDER.mkdir(parents=True, exist_ok=True)
        
        # Define file path
        file_path = DATA_FOLDER/ file.filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "filepath": str(file_path)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
    finally:
        await file.close()



