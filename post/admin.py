from django.contrib import admin
from .models import File, FileDetail, Tag, FileTag

class FileDetailsInline(admin.TabularInline):
    model = FileDetail
    extra = 1

@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    def filesize(self, obj):
        return obj.filedetail.filesize if hasattr(obj, 'filedetail') else 'N/A'

    list_display = ('filename', 'filepath', 'filesize')

    fieldsets = [
        ("Basic", {
            "fields": ['filename', 'filepath']
        }),
    ]

    inlines = [
        FileDetailsInline
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tagname',)

    fieldsets = [
        ("Basic", {
            "fields": ['tagname']
        }),
    ]

@admin.register(FileTag)
class FileTagAdmin(admin.ModelAdmin):
    list_display = ('file', 'tag')

    fieldsets = [
        ("Basic", {
            "fields": ['file', 'tag']
        }),
    ]
