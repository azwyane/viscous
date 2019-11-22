from django.contrib import admin
from .models import post,profile,Comment

class postAdmin(admin.ModelAdmin):
    list_display=["title","author","published_date"]
    list_display_links=["author"]
    list_filter=["published_date","created_date"]
    fieldsets = [
        ("Title/date", {'fields': ["title","author","created_date","published_date"]}),
        ("Content", {"fields": ["text","images"]})
    ]
    
    class meta:
        model=post



admin.site.register(post,postAdmin)
admin.site.register(profile)
admin.site.register(Comment)