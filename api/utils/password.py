import secrets
import string
from passlib.context import CryptContext


# Initialize the password context to use bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordManager:
    """
    Utility class for password management, including hashing, verification,
    and secure random password generation.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using bcrypt.

        Args:
            password (str): The plain text password to hash.

        Returns:
            str: The hashed password.
        """
        if not password or not isinstance(password, str):
            raise ValueError("Password must be a non-empty string.")

        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify if the plain password matches the hashed password.

        Args:
            plain_password (str): The plain text password.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        if not plain_password or not hashed_password:
            raise ValueError("Both plain and hashed passwords must be provided.")

        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def generate_password(
        length: int = 12, use_special_chars: bool = True, exclude_similar: bool = True
    ) -> str:
        """
        Generate a strong, random password.

        Args:
            length (int): The length of the password. Must be at least 8 characters. Defaults to 12.
            use_special_chars (bool): Whether to include special characters in the password. Defaults to True.
            exclude_similar (bool): Whether to exclude visually similar characters (e.g., 'O' and '0'). Defaults to True.

        Returns:
            str: The generated password.
        """
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        # Define character sets
        alphabet = string.ascii_letters + string.digits
        if use_special_chars:
            alphabet += string.punctuation

        if exclude_similar:
            similar_chars = "O0Il1|"
            alphabet = ''.join(c for c in alphabet if c not in similar_chars)

        # Generate a secure random password
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password
