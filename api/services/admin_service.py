# services/admin_service.py
from api.repositories.admin_repository import create_admin, get_admin_by_username
from api.schemas.admin_schema import AdminCreate
from api.utils.encryption import hash_password, verify_password

async def create_new_admin(db, admin_data: AdminCreate):
    hashed_password = hash_password(admin_data.password)
    admin_data.password = hashed_password
    return await create_admin(db, admin_data)

async def authenticate_admin(db, username: str, password: str):
    admin = get_admin_by_username(db, username)
    if admin and verify_password(password, admin.password): 
        return admin
    return None