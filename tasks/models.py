from django.db import models
from django.conf import settings


class Task(models.Model):
    STATUS_CHOICES = [
        ("NEW", "Nowe"),
        ("IN_PROGRESS", "W trakcie"),
        ("DONE", "Zrobione"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NEW",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # powiązanie zadania z użytkownikiem
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
