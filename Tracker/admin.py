from django.contrib import admin
from .models import Tracker

#class Trackertabular(admin.TabularInline):
 #   model = Tracker
 #   fk_name = "title"

class TrackerAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Tracker Information', {'fields': ['admin','cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Cic_Engineer','Activity', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Verify_Status','Final_Comments'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','published_date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade','Cic_Engineer']
    actions = ['download_csv']
    list_display = ('cascade','Technology', 'created_date')
    def some_view(self, request):
        None

    some_view.short_description = "Download CSV file for selected stats."
 #   inlines = [Trackertabular]

admin.site.register(Tracker, TrackerAdmin)

