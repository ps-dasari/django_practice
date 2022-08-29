from django.contrib import admin
from .models import workout_model
# Register your models here.
class workout_Admin(admin.ModelAdmin):
    list_display=['day','workout_name']
admin.site.register(workout_model,workout_Admin)
