from django.contrib import admin
from .models import Language


# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
