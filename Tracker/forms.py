from django import forms

from .models import  Tracker

class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Cic_Engineer', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity')