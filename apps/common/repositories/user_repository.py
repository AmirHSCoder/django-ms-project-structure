from django.contrib.auth.models import User
from .base import BaseRepository

class UserRepository(BaseRepository[User]):
    """
    A repository for the User model.
    """
    model = User

    def get_by_username(self, username: str) -> Optional[User]:
        """
        Returns a user by their username.
        """
        try:
            return self.model.objects.get(username=username)
        except self.model.DoesNotExist:
            return None