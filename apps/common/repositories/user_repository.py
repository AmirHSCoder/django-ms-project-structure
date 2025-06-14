from typing import List, Optional
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

    def get_active_users(self) -> List[User]:
        """Return a list of all active users."""
        return list(self.filter(is_active=True))

    def get_staff_users(self) -> List[User]:
        """Return a list of all staff users."""
        return list(self.filter(is_staff=True))
