<p align="center">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="250" alt="FastAPI Logo" />
</p>

# 🖼️ Image OCR Microservice

**Image OCR Microservice** is a high-performance FastAPI service that extracts text from images and scanned documents using EasyOCR. It provides RESTful endpoints for text extraction and contextual search within documents.

## Features

### Core Capabilities

- ✨ Accurate text extraction from images (PNG, JPG) and scanned PDFs
- 🔍 Contextual search with surrounding sentences
- 🚀 Fast processing with GPU acceleration support
- 📂 Batch processing of multiple files

### Advanced Functionality

- 🌍 Multi-language support (English + French by default)
- 🔄 Automatic image preprocessing for better OCR results
- 📊 JSON responses with structured text data
- 🖼️ Integrated image handling (extraction and saving)

## Getting Started

### Prerequisites

- Python 3+

### Installation

1. Clone the repository:

```bash
git clone <https://github.com/InnovDigital-JeuneKahl/OCR-microservice.git>
cd OCR-microservice
```

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\\Scripts\\activate     # Windows
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```


## API Endpoints

### `POST /get-text`

Extracts raw text from uploaded image

- **Request**:
    - `file`: Image file (PNG/JPG/PDF)
- **Response**:
    
    ```json
    {
      "text": ["paragraph1", "paragraph2"],
      "images": ["extracted_image1.png"]
    }
    
    ```
    

### `POST /search`

Searches for terms in document with context

- **Request**:
    - `file`: Image file
    - `search_terms`: Comma-separated terms
- **Response**:
    
    ```json
    {
      "results": {
        "term1": [
          {
            "prev": "Previous sentence",
            "match": "Sentence containing term1",
            "next": "Next sentence"
          }
        ]
      }
    }
    
    ```
    

## Running the Service

```bash
uvicorn main:app --reload

```

Access docs at: http://localhost:8000/docs

## Deployment

### Docker

```bash
docker build -t image-ocr .
docker run -p 8000:8000 image-ocr

```

## License

Apache 2.0 - See [LICENSE](./LICENSE)