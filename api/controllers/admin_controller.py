from api.utils.app_response import AppResponse
from api.services.admin_service import AdminService

class AdminController:
    def __init__(self):
        self.admin_service = AdminService()  # Corrected the attribute

    async def create_admin(self, lastname: str, firstname: str, username: str, password: str):
        message = await self.admin_service.create_admin(lastname, firstname, username, password)
        return AppResponse.send_success(
            data={"message": message},
            message="Admin route executed successfully"
        )
