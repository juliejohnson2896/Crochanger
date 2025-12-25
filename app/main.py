from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.session import engine
from db.base import Base
import datetime
# Import the DB models to be created, otherwise it doesn't fill the table
import db.models  # 👈 THIS IS THE IMPORTANT LINE

# A dictionary to store resources or state
app_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup (before the 'yield')
    app_state["start_time"] = datetime.datetime.now()
    print(f'Server started: {app_state["start_time"]}')
    # Initialize database connections, load models, etc.
    Base.metadata.create_all(bind=engine)

    yield  # The application starts serving requests here

    # Code to run on shutdown (after the 'yield')
    print(f'Server shutdown: {datetime.datetime.now()}')
    # Clean up resources, close database connections, etc.
    app_state.clear()

app = FastAPI(title="Crochet Pattern Manager", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}
