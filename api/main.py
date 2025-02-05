from fastapi import FastAPI
from api.config.config import config
from fastapi.middleware.cors import CORSMiddleware
from api.utils.app_response import AppResponse
from api.routes import router as api_router
from api.utils.database import engine, Base
from contextlib import asynccontextmanager

docs_url = "/docs" if config["app"]["env"] == "development" else None
redoc_url = "/redoc" if config["app"]["env"] == "development" else None

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="FAST API",
    version="1.0.0",
    description="FAST API BY DANIELLE LUNAS",
    docs_url=docs_url,
    redoc_url=redoc_url,
    lifespan=lifespan,
)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router)

@app.get("/")
async def root():
    return AppResponse.send_success(
        data=None, 
        message="Welcome to the FAST API by DANIELLE LUNAS!",
        code=200
    )

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(
        "api.main:app",
        port=int(config["app"]["port"]),
        reload=True,
    )
