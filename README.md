# 📊 PowerPoint Generator AI Agent

An AI-powered tool to generate professional PowerPoint presentations from text prompts using LLMs.

## 🚀 Features
- Generate slide content with LLMs
- Predefined PowerPoint templates
- CLI, API, and Web UI (Streamlit)
- Save and download `.pptx` files

## add your .env file which should contain gemini api and pexels api

code you have to add in .env file:-
GEMINI_API_KEY=
PEXELS_API_KEY=

## 📂 Project Structure


ppt-generator-ai/
│── README.md                # Project overview
│── requirements.txt         # Python dependencies (add pinecone-client, langchain etc.)
│── .env                     # API keys (OpenAI, Pinecone, etc.)
│
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point (CLI/Streamlit/FastAPI UI)
│   │
│   ├── config/
│   │   └── settings.py      # Configurations (env, constants, Pinecone index name)
│   │
│   ├── agents/
│   │   ├── prompt_engineer.py   # Prompt templates for LLM
│   │   ├── content_agent.py     # LLM-based content generator
│   │   └── design_agent.py      # Suggests slide layouts & styles
│   │
│   ├── services/
│   │   ├── llm_service.py       # Wrapper for LLM APIs (OpenAI, local LLMs)
│   │   ├── ppt_service.py       # Handles PowerPoint creation (python-pptx)
│   │   └── research_service.py  # Optional: fetch info from web (search APIs)
│   │
│   ├── vector_db/
│   │   ├── pinecone_service.py  # Pinecone client setup, CRUD ops
│   │   ├── embedder.py          # Embedding generator (OpenAI/HuggingFace)
│   │   └── retriever.py         # Retrieve relevant chunks for grounding
│   │
│   ├── utils/
│   │   ├── logger.py            # Logging setup
│   │   ├── file_handler.py      # Save/load PPT, temp files
│   │   └── text_utils.py        # Cleaning & formatting text
│   │
│   ├── templates/
│   │   ├── corporate.pptx       # Predefined design template
│   │   ├── modern.pptx
│   │   └── minimal.pptx
│   │
│   └── ui/
│       ├── cli.py               # Command-line interface
│       ├── streamlit_app.py     # Web app frontend (optional)
│       └── api.py               # REST API with FastAPI/Flask
│
├── tests/
│   ├── test_content_agent.py
│   ├── test_ppt_service.py
│   ├── test_pinecone_service.py # Tests for vector DB integration
│   └── test_end_to_end.py
│
└── docs/
    └── architecture.md          # Documentation + architecture diagrams
