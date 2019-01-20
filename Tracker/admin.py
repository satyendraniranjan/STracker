from django.contrib import admin
from .models import Tracker

#class Trackertabular(admin.TabularInline):
 #   model = Tracker
 #   fk_name = "title"

class TrackerAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title',     {'fields':['title']}),
        ('Other Information', {'fields': ['admin','cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Cic_Engineer', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','published_date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']
    list_display = ('title','cascade','Technology', 'created_date')
    def some_view(self, request):
        None

    some_view.short_description = "Download CSV file for selected stats."
 #   inlines = [Trackertabular]

admin.site.register(Tracker, TrackerAdmin)
