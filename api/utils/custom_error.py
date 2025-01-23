class CustomError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.name = self.__class__.__name__  # Equivalent to `this.constructor.name`
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return f"{self.name}: {self.message} (Status Code: {self.status_code})"


class ValidationError(CustomError):
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, 400)


class AuthError(CustomError):
    def __init__(self, message: str = "Invalid Credentials"):
        super().__init__(message, 401)


class NotFoundError(CustomError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


class ForbiddenError(CustomError):
    def __init__(self, message: str = "Forbidden Request"):
        super().__init__(message, 403)


class ServerError(CustomError):
    def __init__(self, message: str = "Internal server error"):
        super().__init__(message, 500)
