from django.contrib import admin
from .models import Language, State


# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    pass


class StateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(State, StateAdmin)
