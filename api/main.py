from fastapi import FastAPI
from api.config.config import config
from fastapi.middleware.cors import CORSMiddleware
from api.utils.app_response import AppResponse
from api.routes import router as api_router
# Determine Swagger visibility based on environment
docs_url = "/docs" if config["app"]["env"] == "development" else None
redoc_url = "/redoc" if config["app"]["env"] == "development" else None

# Initialize FastAPI app
app = FastAPI(
    title="FAST API",
    version="1.0.0",
    description="API BOILERPLATE BY RUPERT CAINGAL",
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


# Registere Endpoints
app.include_router(api_router)

# Root Endpoint
@app.get("/")
async def root():
    return AppResponse.send_success(
        data=None, 
        message="Welcome to the FAST API Boilerplate by Rupert Caingal!",
        code=200
        )
   

# Run the server
if __name__ == "__main__":
    import uvicorn

    # Use config["app"]["port"] dynamically
    uvicorn.run(
        "api.main:app",
        port=int(config["app"]["port"]),  # Pass port from config
        reload=True,  # Use in development
    )
