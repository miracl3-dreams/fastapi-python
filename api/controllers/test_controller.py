from api.utils.app_response import AppResponse
from api.services.test_service import TestService

class TestController:
    """
    Controller for handling the test route logic.
    """

    def __init__(self):
        self.test_service = TestService()

    async def get_hello_world(self):
        """
        Logic for the test route.

        Returns:
            JSONResponse: A standardized response with "Hello World".
        """
        # Call the service to get the message
        message = await self.test_service.get_hello_world()
        return AppResponse.send_success(
            data={"message": message},
            message="Test route executed successfully"
        )
