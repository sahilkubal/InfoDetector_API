from django.db import models

class InfoModel(models.Model):
    image_name = models.CharField(max_length=255)
    objects_detected = models.CharField(max_length=255)
    timestamp = models.DateField()
    
    class Meta:
        db_table = "InfoModel"
        
    def __str__(self):
        return self.image_name