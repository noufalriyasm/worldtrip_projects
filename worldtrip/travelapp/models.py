from django.db import models

# Create your models here.
class collegeproject(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()


    def __str__(self):
        return self.name
