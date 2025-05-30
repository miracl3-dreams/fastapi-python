# env.py for alembic migration
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from alembic import context
from api.config.config import config  # ✅ Import from config.py
from api.models import Base  # ✅ Import shared Base from models/__init__.py

# Alembic Config object, provides access to .ini file values
config_alembic = context.config

# Interpret the config file for Python logging.
if config_alembic.config_file_name is not None:
    fileConfig(config_alembic.config_file_name)

# ✅ Fetch the database URL from config.py
DB_URL = config["db"].get("url")

if not DB_URL:
    raise ValueError("DATABASE_URL is not set in the config!")

# Dynamically update the SQLAlchemy URL in Alembic config
config_alembic.set_main_option("sqlalchemy.url", DB_URL)

# Target metadata for Alembic migrations
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using async engine."""
    connectable: AsyncEngine = create_async_engine(DB_URL, pool_pre_ping=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection):
    """Helper function to run migrations."""
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

    with context.begin_transaction():
        context.run_migrations()

# Run migrations in the appropriate mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())  # ✅ Fixes async handling
