from django.contrib import admin
from django.apps import apps
# Register your models here.

app_models = apps.get_app_config("app").get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass