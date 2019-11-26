from django.contrib import admin
from testapp.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'sno', 'name', 'city']

admin.site.register(Person, PersonAdmin)
