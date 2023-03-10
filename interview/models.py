from django.db import models
from accounts.models import CustomUser
from django.contrib.postgres.fields import ArrayField


# Create your models here.



class InterviewTest(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    score = models.IntegerField(default=0, blank=True, null=True)
    confidence = models.IntegerField(default=0, blank=True, null=True)
    report_link = models.CharField(max_length=256, blank=True, null=True)

    '''
    [
        ...
        {
            "question": "abc",
            "expected_answer": "xyz",
            "user_answer": "pqr"
        }
        ...
    ]
    '''
    interview_data = ArrayField(models.JSONField(max_length=3072, blank=True, null=True), size=32, blank=True, null=True)

    


