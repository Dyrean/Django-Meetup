from django.contrib import admin
from .models import MeetUp, Location, Participant

# Register your models here.


class MeetUpAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "location")
    list_filter = ("location", "date")


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


admin.site.register(MeetUp, MeetUpAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Participant)
