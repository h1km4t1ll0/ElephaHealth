from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'signals'

    def ready(self):
        import signals
