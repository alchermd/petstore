from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out

from iam import signals


class IamConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "iam"

    def ready(self):
        user_logged_out.connect(signals.logout_message)
        user_logged_in.connect(signals.login_message)
