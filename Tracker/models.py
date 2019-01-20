from django.conf import settings
from django.db import models
from django.utils import timezone

class Tracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=200, default='SOME STRING')
        cascade = models.CharField(max_length=500, default='SOME STRING')
        Technology = models.CharField(max_length=500, default='SOME STRING')
        Type = models.CharField(max_length=500, default='SOME STRING')
        Bandwidth_Checked_From_LSM = models.CharField(max_length=500, default='SOME STRING')
        Market = models.CharField(max_length=500, default='SOME STRING')
        eNB = models.CharField(max_length=500, default='SOME STRING')
        LSM = models.CharField(max_length=500, default='SOME STRING')
        CSMS = models.CharField(max_length=500, default='SOME STRING')
        FE_Name = models.CharField(max_length=500, default='SOME STRING')
        Mode_of_Communication = models.CharField(max_length=500, default='SOME STRING')
        Cic_Engineer = models.CharField(max_length=500, default='SOME STRING')
        Activity_status = models.CharField(max_length=500, default='SOME STRING')
        Site_Status_pre_Activity = models.CharField(max_length=500, default='SOME STRING')
        Site_Status_post_Activity = models.CharField(max_length=500, default='SOME STRING')

        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title