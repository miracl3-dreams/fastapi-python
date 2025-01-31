from fastapi import FastAPI
from api.config.config import config
from fastapi.middleware.cors import CORSMiddleware
from api.utils.app_response import AppResponse
from api.routes.v1.admin_router import admin_router
from api.routes.v1.user_router import user_router
from api.routes import router as api_router
from api.utils.database import engine, Base

# Determine Swagger visibility based on environment
docs_url = "/docs" if config["app"]["env"] == "development" else None
redoc_url = "/redoc" if config["app"]["env"] == "development" else None

# Initialize FastAPI app
app = FastAPI(
    title="FAST API",
    version="1.0.0",
    description="FAST API BY DANIELLE LUNAS",
    docs_url=docs_url,
    redoc_url=redoc_url,
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
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(api_router)

# Root Endpoint
@app.get("/")
async def root():
    return AppResponse.send_success(
        data=None, 
        message="Welcome to the FAST API by DANIELLE LUNAS!",
        code=200
    )

# Asynchronous database initialization
@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Run the server
if __name__ == "__main__": 
    import uvicorn
    # Use config["app"]["port"] dynamically
    uvicorn.run(
        "api.main:app",
        port=int(config["app"]["port"]),  # Pass port from config
        reload=True,  # Use in development
    )