# AI-First CRM – HCP Interaction Module

An AI-powered Customer Relationship Management application designed for pharmaceutical field representatives to log and manage interactions with Healthcare Professionals (HCPs) through both a structured form and a conversational AI assistant.

## Project Overview

The objective of this project is to build an AI-first CRM experience for life-science field representatives. Users can describe an interaction with a Healthcare Professional in natural language, and the AI agent automatically extracts structured information and updates the CRM form.

The system also supports editing interactions, generating summaries, suggesting follow-up actions, and providing meeting insights.

## Features

- AI-powered natural-language interaction logging
- Automatic extraction of HCP interaction details
- Automatic CRM form population using Redux
- Edit existing interaction details through conversational commands
- Generate professional interaction summaries
- Suggest appropriate follow-up actions
- Generate meeting insights and recommendations
- Save interaction records to a SQL database
- Split-screen CRM interface with structured form and AI assistant

## Tech Stack

### Frontend

- React
- Redux Toolkit
- Axios
- Vite
- CSS
- Google Inter Font

### Backend

- Python
- FastAPI
- LangGraph
- Groq LLM
- SQLAlchemy
- SQLite

## LangGraph AI Agent Tools

The AI agent supports five core tools:

### 1. Log Interaction

Extracts structured CRM information from natural-language input, including:

- HCP name
- Interaction type
- Date and time
- Attendees
- Topics discussed
- Materials shared
- Samples distributed
- Sentiment
- Outcomes
- Follow-up actions

### 2. Edit Interaction

Allows users to modify previously logged interaction details using natural-language commands while preserving existing information.

Example:

```text
Change the sentiment to neutral.
```

### 3. Summarize Interaction

Generates a short professional summary based on the currently logged HCP interaction.

Example:

```text
Summarize the interaction.
```

### 4. Suggest Follow-up

Analyzes the current interaction and recommends an appropriate next action for the field representative.

Example:

```text
Suggest follow up.
```

### 5. Meeting Insights

Provides:

- A key observation
- A potential opportunity
- A recommended next action

Example:

```text
Meeting insights.
```

## Project Structure

```text
AI-HCP-CRM/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── graph/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── tools/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── services/
│   │   └── styles/
│   └── package.json
│
├── .gitignore
└── README.md
```

## How to Run the Project

### Backend Setup

Open a terminal and navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### Frontend Setup

Open another terminal and navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend will run at:

```text
http://localhost:5173
```

## Demo Workflow

1. Enter a natural-language HCP interaction in the AI CRM Assistant.
2. The LangGraph-powered AI agent processes the request.
3. The LLM extracts structured interaction information.
4. Redux automatically updates the CRM form.
5. The user can edit the interaction through conversational commands.
6. The AI can summarize the interaction, suggest follow-ups, and generate meeting insights.
7. The interaction can be saved to the database.

## Example Interaction

```text
Today I met Dr. Ramesh regarding Product X.
```

The AI extracts and automatically populates information such as the HCP name, interaction type, date, topics discussed, and sentiment.

## Security

API keys and local environment files are excluded from version control through `.gitignore`. Users should create their own `.env` file and provide their own Groq API key.

## Author

**Maroju Meghana**
