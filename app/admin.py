from django.contrib import admin

from app.models import JobPost, Location, Author, Skills


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'date')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    search_help_text = "Search in title and description"
    fieldsets = (
        ('Basic information:', {
            'fields': ('title', 'description')
        }),
        ('More information:', {
            'classes': ('collapse',),
            'fields': (('expiry', 'salary'), 'slug', 'location', 'author')
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class SkillsAdmin(admin.ModelAdmin):
    pass


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
