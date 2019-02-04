from django import forms

from .models import  Tracker

class TrackerForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Cic_Engineer','Activity', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Verify_Status','Final_Comments')
