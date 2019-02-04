from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

class Tracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

        cascade = models.CharField(max_length=500, default='')
        Technology_CHOICES1 = (
                ('1', '800 CDMA'),
                ('2', '1900 CDMA'),
                ('3', '800 FDD'),
                ('4', '1900 FDD'),
                ('5', '2.5 TDD'),
                ('6', '1900/800 CDMA'),
                ('7', '1900/800 FDD'),
                ('8', '1900/700 FDD'),
                ('9', '1900/700 CDMA'),
                ('10', '700 FDD'),
                ('11', '700 CDMA'),
                ('12', '800 FDD/CDMA'),
                ('13', '700 FDD/CDMA'),
        )

        Technology = models.CharField(max_length=1, choices=Technology_CHOICES1)

        Type_CHOICES8 = (
                ('1', 'CDU10'),
                ('2', 'CDU20'),
                ('3', 'CDU30'),
                ('4', 'NA'),
        )

        Type = models.CharField(max_length=1, choices=Type_CHOICES8)

        Bandwidth_Checked_From_LSM_CHOICES10 = (
                ('1', '3Mhz'),
                ('2', '5Mhz'),
                ('3', '10Mhz'),
                ('4', '20Mhz'),
                ('5', '5+10Mhz/5Mhz'),
                ('6', '5+10Mhz/3Mhz'),
                ('7', '10+5Mhz/5Mhz'),
                ('8', '10+5Mhz/3Mhz'),
                ('9', 'NA'),
        )

        Bandwidth_Checked_From_LSM = models.CharField(max_length=1, choices=Bandwidth_Checked_From_LSM_CHOICES10)

        Market = models.CharField(max_length=500, default='')
        eNB = models.CharField(max_length=500, default='')
        LSM = models.CharField(max_length=500, default='')
        CSMS = models.CharField(max_length=500, default='')
        FE_Name = models.CharField(max_length=500, default='')


        Mode_of_Communication_CHOICES6 = (
                ('1', 'Whatsapp'),
                ('2', 'Primary Bridge'),
                ('3', 'Secondary Bridge'),
                ('4', 'IM'),
                ('5', 'E-Mail'),
        )

        Mode_of_Communication = models.CharField(max_length=1, choices=Mode_of_Communication_CHOICES6)

        Cic_Engineer_CHOICES5 = (
                ('1', 'Amit Yadav M'),
                ('2', 'Sankalita Banerjee'),
                ('3', 'Gurpreet Yadav'),
                ('4', 'Pradipta Mukherjee'),
                ('5', 'Abhishek Kumar DD'),
                ('6', 'Susheel'),
                ('7', 'P Rama Krishna'),
                ('8', 'Anand chowdhary'),
                ('9', 'Tarunam Mahajan'),
                ('10', 'Prem Prakash Rai'),
                ('11', 'Pravesh Kumar'),
                ('12', 'Shyam Singh Chauhan'),
                ('13', 'Vaibhav Bhatt'),
        )

        Cic_Engineer = models.CharField(max_length=1, choices=Cic_Engineer_CHOICES5)

        Activity_CHOICES2 = (
                ('1', 'C&I'),
                ('2', 'Troubleshoot'),
                ('3', 'LATP Testing'),
                ('4', 'FATP Testing'),
                ('5', 'Pre-Integration'),
                ('6', 'Update to FE'),
                ('7', 'C&I Task in Appian'),
                ('8', 'Review LATP in Appian'),
        )

        Activity = models.CharField(max_length=1, choices=Activity_CHOICES2)

        Activity_status_CHOICES3 = (
                ('1', 'Open'),
                ('2', 'Close'),
                ('3', 'Handover'),
        )

        Activity_status = models.CharField(max_length=1, choices=Activity_status_CHOICES3,)

        Site_Status_pre_Activity_CHOICES4 = (
                ('1', 'Lock'),
                ('2', 'Unlock'),
                ('3', 'N/A'),
        )

        Site_Status_pre_Activity = models.CharField(max_length=1, choices=Site_Status_pre_Activity_CHOICES4)

        Site_Status_post_Activity = models.CharField(max_length=500, default='', blank=True)

        E_Link_Status_of_BH0_for_CDU30_CHOICES12 = (
                ('1', 'On'),
                ('2', 'OFF'),
                ('3', 'NA'),

        )

        E_Link_Status_of_BH0_for_CDU30 = models.CharField(max_length=1, choices=E_Link_Status_of_BH0_for_CDU30_CHOICES12, blank=True)


        MJ_Object_Marked_CHOICES11 = (
                ('1', 'Marked'),
                ('2', 'Not Marked'),
                ('3', 'NA'),

        )

        MJ_Object_Marked = models.CharField(max_length=1, choices=MJ_Object_Marked_CHOICES11,blank=True)

        RET_CHOICES9 = (
                ('1', 'Defined/Matched'),
                ('2', 'Defined/NotMached'),
                ('3', 'Not Define'),
                ('4', 'NA'),
        )

        RET = models.CharField(max_length=1, choices=RET_CHOICES9, blank=True)

        Alarms_Preventing_RET_Config = models.CharField(max_length=500, default='SOME STRING', blank=True)

        Frequency_Earfcn_Checked_from_LSM_BSM_CHOICES7 = (
                ('1', 'Yes'),
                ('2', 'No'),
                ('2', 'Not Required'),
        )

        Frequency_Earfcn_Checked_from_LSM_BSM = models.CharField(max_length=1, choices=Frequency_Earfcn_Checked_from_LSM_BSM_CHOICES7, blank=True)

        IP_Route_or_IP_Address = models.CharField(max_length=500, default='',blank=True)
        Volte_MME_IP_Config = models.CharField(max_length=500, default='',blank=True)
        Review_LATP_Complete = models.CharField(max_length=500, default='',blank=True)
        Remarks = models.CharField(max_length=500, default='',blank=True)
        OAR_Date = models.CharField(max_length=500, default='')
        OAC_Date = models.CharField(max_length=500, default='')
        Lock_Unlock_Verified_By = models.CharField(max_length=500, default='',blank=True)
        Verify_Status = models.CharField(max_length=500, default='',blank=True)
        Final_Comments = models.CharField(max_length=500, default='',blank=True)







        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title


