class TestRepository:
    """
    Repository for handling data-related logic for the test route.
    """

    async def fetch_hello_world(self) -> str:
        """
        Fetches the Hello World message.

        Returns:
            str: The "Hello World" message.
        """
        return "Hello World"
