import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def resolve_nested_env(value):
    return value.format(**os.environ) if value else value

config = {
    "app": {
        "port": int(os.getenv("PORT", 8080)),
        "env": os.getenv("PROJECT_ENV", "development"),
    },
    "db": {
        "url": resolve_nested_env(
            "{scheme}://{user}:{password}@{host}:{port}/{name}".format(
                scheme="mysql+asyncmy",
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                host=os.getenv("DB_HOST", "localhost"),
                port=os.getenv("DB_PORT", "3306"),
                name=os.getenv("DB_NAME", "tm_db")
            )
        ),
    },
    "key": {
        "secret": os.getenv("JWT_SECRET_KEY", "default_jwt_secret"),
        "x_key": os.getenv("API_KEY", "default_api_key"),
        "refreshSecret": os.getenv("JWT_REFRESH_SECRET_KEY", "default_refresh_secret"),
        "expiresIn": os.getenv("JWT_EXPIRES_IN", "3600"),  # Default to 1 hour
        "refreshExpiresIn": os.getenv("JWT_REF_EXPIRES_IN", "86400"),  # Default to 24 hours
    },
    "url": {
        "local": f"http://localhost:{os.getenv('PORT', 8000)}/api/v1",
        "forward": f"{os.getenv('PORT_FORWARD_URL', '')}api/v1",
    },
}

# Debugging: Print the DATABASE_URL
print("DATABASE_URL:", config["db"]["url"])