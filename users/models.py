from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Rozszerzony model użytkownika.
    Dodajemy rolę, aby w przyszłości umożliwić rozróżnienie uprawnień.
    """

    ROLE_CHOICES = (
        ("USER", "Użytkownik"),
        ("ADMIN", "Administrator"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="USER")

    def __str__(self):
        return self.username
