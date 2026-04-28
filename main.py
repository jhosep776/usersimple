from fastapi import FastAPI
from routes.index import router
from config.db import engine, meta 
from fastapi.middleware.cors import CORSMiddleware 
meta.create_all(engine) 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router ,prefix="/api")
 