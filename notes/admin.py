from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
from .models import Note

admin.site.register(Note, NoteAdmin)