from django.contrib import admin

# Register your models here.
from newsfeeds.models import Country, News

admin.site.register(Country)
admin.site.register(News)