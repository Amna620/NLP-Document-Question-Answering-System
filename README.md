# NLP-Based Document Question Answering System

A document-based Question Answering System developed using Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG).

## Project Overview

This application allows users to upload multiple PDF and DOCX documents and ask questions based on their content. It retrieves relevant passages using semantic search and generates concise answers using a locally hosted language model.

## Key Features

- Multiple PDF and DOCX document uploads
- Automatic text extraction
- Text chunking with overlap
- Semantic embedding generation
- FAISS-based similarity search
- AI-generated answers using Qwen2.5
- Document source references and similarity scores
- Interactive Streamlit web interface

## Technologies Used

- **Python 3.12** — Programming language
- **Streamlit** — Web interface
- **PyMuPDF** — PDF text extraction
- **python-docx** — Word document processing
- **Sentence Transformers (all-MiniLM-L6-v2)** — Semantic embeddings
- **FAISS** — Similarity search
- **NumPy** — Vector processing
- **Qwen2.5-1.5B-Instruct** — Local answer generation
- **llama.cpp** — Local language model inference server

## NLP Workflow

1. Upload PDF or DOCX documents.
2. Extract readable text from the documents.
3. Split extracted text into chunks of up to 150 words with a 30-word overlap.
4. Generate 384-dimensional semantic embeddings.
5. Retrieve the top relevant passages using FAISS.
6. Generate a concise answer using Qwen2.5 and the retrieved context.
7. Display the answer with source references.

## Installation

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
cd NLP_Document_QA
```

Create and activate a Python virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Local AI Model Setup

Download the Qwen2.5-1.5B-Instruct GGUF model and a compatible llama.cpp Windows build.

Start the local inference server:

```powershell
.\llama-server.exe -m "PATH_TO_MODEL.gguf" --host 127.0.0.1 --port 8081 -c 2048 -ngl 0
```

The local AI server must be running for answer generation to work.

## Run the Application

Open a separate terminal and run:

```powershell
python -m streamlit run app.py
```

Open the application in your browser:

`http://localhost:8501`

## Limitations

- Scanned PDFs may require OCR.
- Answer quality depends on the retrieved document content and the language model.
- Local AI inference depends on available RAM and processing resources.
- Generated answers should be verified for accuracy.

## Future Improvements

- OCR support for scanned documents
- Multilingual question answering
- Improved document retrieval
- Evaluation of answer accuracy and response time

## Project Type

Academic project developed for the Natural Language Processing (NLP) subject.