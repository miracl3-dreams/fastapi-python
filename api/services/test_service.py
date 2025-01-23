from api.repositories.test_repository import TestRepository

class TestService:
    """
    Service layer for handling business logic for the test route.
    """

    def __init__(self):
        self.test_repository = TestRepository()

    async def get_hello_world(self) -> str:
        """
        Handles the business logic to fetch the Hello World message.

        Returns:
            str: The Hello World message.
        """
        message = await self.test_repository.fetch_hello_world()
        return message
