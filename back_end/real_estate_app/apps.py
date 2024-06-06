from django.apps import AppConfig


class RealEstateAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_estate_app'

    def ready(self):
        from . import utils
        from django.db.models.signals import post_migrate

        def initialize_data(sender, **kwargs):
            utils.initializing()
            utils.news_api()
            utils.issues_crawling()
            utils.read_data()

        post_migrate.connect(initialize_data, sender=self)