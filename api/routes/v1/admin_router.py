# admin_router.py
from fastapi import APIRouter
from api.controllers.admin_controller import AdminController

admin_router = APIRouter()

# Instantiate the AdminController
admin_controller = AdminController()

# Example routes
@admin_router.post("/admin/create")
async def create_admin():
    return await admin_controller.create_admin()

# You can add more routes related to admin here
