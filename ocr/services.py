import easyocr
import os
import re
import time
from typing import List, Dict, Optional

def perform_ocr(image_path: str) -> List[str]:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")
    
    reader = easyocr.Reader(['en'], gpu=False)
    results = reader.readtext(image_path, detail=0, paragraph=True)
    return results

def find_all_sentence_contexts(
    full_text: str,
    search_terms: List[str],
    language: str = 'fr'
) -> Dict[str, List[Dict[str, Optional[str]]]]:
    sentence_endings = r'(?<!\w\.\w.)(?<![A-ZÀ-Ü][a-zà-ü]\.)(?<=\.|\?|\!|\…|\n)\s+'
    sentences = [s.strip() for s in re.split(sentence_endings, full_text) if s.strip()]
    
    patterns = {
        term: re.compile(rf'(?<!\w){re.escape(term)}(?!\w)', re.IGNORECASE)
        for term in search_terms
    }
    
    results = {term: [] for term in search_terms}
    
    for idx, sentence in enumerate(sentences):
        for term, pattern in patterns.items():
            if pattern.search(sentence):
                context = {
                    'prev': sentences[idx-1] if idx > 0 else None,
                    'match': sentence,
                    'next': sentences[idx+1] if idx < len(sentences)-1 else None
                }
                results[term].append(context)
    
    return results