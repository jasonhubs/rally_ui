from django.db import models

# Create your models here.

class RallyJob(models.Model):
    rally_job_text = models.CharField(max_length=200)
    rally_job_description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.rally_job_text


class Scenario(models.Model):
    rally_job = models.ForeignKey(RallyJob)
    rally_scenario = models.CharField(max_length=200)
    
    def __str__(self):
        return self.rally_scenario