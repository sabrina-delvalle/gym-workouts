from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        # Import and connect signals
        from user import signals  # noqa: F401 (flake8 ignore unused import)
