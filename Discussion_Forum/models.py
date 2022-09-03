from django.db import models

# Create your models here.


class Test(models.Model):
    Name=models.CharField(max_length=200)
    Image1 = models.ImageField(
        upload_to="Discussion_Forum/upload_img", height_field=None, width_field=None, max_length=None, null=True)
   

    class Meta:
        verbose_name_plural = "Test"
        ordering = ['Name']

    def __str__(self):
        return self.Name