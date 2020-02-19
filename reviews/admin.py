from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Model Admin Definition """

    pass

