from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Union
from fastapi import UploadFile
from fastapi import Form, File

class TextContext(BaseModel):
    prev: Optional[str] = Field(None, example="The previous sentence")
    match: str = Field(..., example="The matching sentence")
    next: Optional[str] = Field(None, example="The next sentence")

class SearchResponse(BaseModel):
    results: Dict[str, List[TextContext]] = Field(
        ...,
        example={
            "example": [
                {
                    "prev": "This is the previous sentence",
                    "match": "This contains the example word",
                    "next": "This is the next sentence"
                }
            ]
        }
    )

class TextResponse(BaseModel):
    text: List[str] = Field(
        ...,
        example=["First paragraph of text", "Second paragraph of text"]
    )

class SearchRequestForm:
    def __init__(
        self,
        file: UploadFile = File(...),
        search_terms: str = Form("")
    ):
        self.file = file
        self.search_terms = search_terms