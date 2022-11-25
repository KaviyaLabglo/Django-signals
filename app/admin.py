from django.contrib import admin
from app.models import Profile

class J(admin.ModelAdmin):
    list_display = ('id','user', 'image')
admin.site.register(Profile,J)
# Register your models here.
