from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
import os  # To fetch environment variables
from api.utils.database import Base  # Import your shared Base

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Load the database URL from environment variables
from dotenv import load_dotenv
load_dotenv()
raw_db_url = os.getenv("DATABASE_URL")  # Fetch from environment
if not raw_db_url:
    raise ValueError("DATABASE_URL is not set in the environment!")

# Ensure the database URL uses the correct async MySQL dialect
DB_URL = raw_db_url.replace("mysql://", "mysql+asyncmy://", 1) if raw_db_url.startswith("mysql://") else raw_db_url

# Dynamically update the SQLAlchemy URL
config.set_main_option("sqlalchemy.url", DB_URL)

# Import models and shared Base
from api.models import Base  # Import shared Base from models/__init__.py
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    # Create an async engine
    connectable = create_async_engine(DB_URL)

    # Run migrations in an async context
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )
    # Run migrations without starting an extra transaction block
    context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
