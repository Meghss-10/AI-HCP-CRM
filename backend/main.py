from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.models.interaction import Interaction
from app.models.chat import Chat

from app.api.interaction_routes import router as interaction_router
#from app.api import ai_routes
from app.api.agent_routes import router as agent_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI-HCP-CRM",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(interaction_router)
#app.include_router(ai_routes.router)
app.include_router(agent_router)


@app.get("/")
def home():
    return {
        "message": "AI CRM Backend Running 🚀"
    }