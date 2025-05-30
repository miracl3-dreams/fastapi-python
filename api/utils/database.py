from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from api.config.config import config

# Database URL from config
DATABASE_URL = config["db"].get("url")

# Create the async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Singleton pattern for database session management
class DatabaseSessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSessionManager, cls).__new__(cls)
            cls._instance.session_factory = async_session_factory
        return cls._instance

    def session(self) -> AsyncSession:
        """Create a new database session."""
        return self.session_factory()

# Export the singleton instance of the session manager
db_session_manager = DatabaseSessionManager()

# Dependency for FastAPI routes
async def get_db():
    """
    Dependency for FastAPI to provide a database session for each request.
    Ensures proper cleanup of the session after usage.
    """
    async with db_session_manager.session() as session:
        yield session
