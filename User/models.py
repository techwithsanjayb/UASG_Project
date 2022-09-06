from django.db import models

# Create your models here.



# USER_REGISTRATION TABLES MODEL

class UserRegistration(models.Model):
    userregistration_user_id = models.AutoField(primary_key=True)
    userregistration_email_field = models.EmailField(max_length=60, unique=True)
    userregistration_password = models.CharField(max_length=500)
    userregistration_confirm_password = models.CharField(max_length=500)
    CHOICES = [('Individual', 'Individual'),
               ('Organization', 'Organization'),
               ('DomainExpert', 'DomainExpert')]
    registration_User_Type = models.CharField(max_length=50, choices=CHOICES, default='Individual')

    class Meta:
        verbose_name_plural = "User Registration"
        ordering = ['userregistration_email_field']

    def __str__(self):
        return self.userregistration_email_field