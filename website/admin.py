from django.contrib import admin
from .models import HomePage, Article, Service


# Register your models here.
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HomePage.objects.exists():
            return False  # Prevent adding more instances.
        else:
            return super().has_add_permission(request)  # Allow adding a single instance.
        

admin.site.register(HomePage, HomePageAdmin)

admin.site.register(Article)

admin.site.register(Service)