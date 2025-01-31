# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from fastapi import HTTPException
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import SQLAlchemyError
# from api.config.config import config  
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # Access the DATABASE_URL from the nested "db" key
# try:
#     DATABASE_URL = config["db"]["url"]
#     if not DATABASE_URL:
#         raise ValueError("DATABASE_URL is empty or not set in the environment variables.")
#     print("Loaded DATABASE_URL:", DATABASE_URL)  # Debugging line
# except KeyError:
#     raise ValueError("DATABASE_URL is missing from the configuration. Please check your .env file.")

# # Create the async database engine
# engine = create_async_engine(DATABASE_URL, echo=True)

# # Create a session factory
# async_session_factory = sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# # Singleton pattern for database session management
# class DatabaseSessionManager:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(DatabaseSessionManager, cls).__new__(cls)
#             cls._instance.session_factory = async_session_factory
#         return cls._instance

#     def session(self) -> AsyncSession:
#         """Create a new database session."""
#         return self.session_factory()

# # Export the singleton instance of the session manager
# db_session_manager = DatabaseSessionManager()

# # Dependency for FastAPI routes
# async def get_db():
#     """
#     Dependency for FastAPI to provide a database session for each request.
#     Ensures proper cleanup of the session after usage.
#     """
#     try:
#         async with db_session_manager.session() as session:
#             yield session
#     except SQLAlchemyError as e:
#         # Log the error (optional) and raise an HTTPException
#         print(f"Database error: {e}")
#         raise HTTPException(status_code=500, detail="Database connection error")

# utils/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+asyncmy://root:@localhost:3306/tm_db"  # Replace with your credentials

engine = create_async_engine(DATABASE_URL, echo=True)  # Set `echo=True` for debugging SQL queries

# Define an asynchronous session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()