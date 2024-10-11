from django.db import models

class eventdata(models.Model):
    org_id = models.IntegerField()
    event_name = models.CharField(max_length=255)
    event_organizer = models.CharField(max_length=255)
    event_date = models.DateField()
    event_location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = "eventdata"  # Custom database table name (usually snake_case is preferred)
