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



class DocumentHub_Category(models.Model):
    DocumentHub_CategoryType = models.CharField(max_length=100)
    DocumentHub_Cat_Status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Document Hub Category"
        ordering = ['DocumentHub_CategoryType']

    def __str__(self):
        return self.DocumentHub_CategoryType

class DocumentHub_Languages(models.Model):
    DocumentHub_LanguagesType = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "DocumentHub LanguagesType"
        ordering = ['DocumentHub_LanguagesType']

    def __str__(self):
        return self.DocumentHub_LanguagesType


class DocumentHubData(models.Model):
    DocumentHubData_Title = models.CharField(max_length=100)
    DocumentHubData_CategoryType = models.ForeignKey(
        DocumentHub_Category, on_delete=models.CASCADE)
    DocumentHubData_Tags = models.SlugField()
    DocumentHubData_PublishedDate = models.DateTimeField(
        auto_now_add=True,  blank=True)
    DocumentHubData_CreationDate = models.DateTimeField(
        auto_now_add=True,  blank=True, null=True)
    DocumentHubData_FileSize = models.CharField(max_length=30)
    DocumentHubData_LastUpdatedDate = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    DocumentHubData_UploadSupportDocument = models.FileField(
        upload_to="User/Documenthub")
    DocumentHubData_DownloadCounter = models.IntegerField()
    DocumentHubData_PublishedChoices = (
        ('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED'))
    DocumentHubData_PublishedStatus = models.CharField(
        max_length=20, choices=DocumentHubData_PublishedChoices, default="published")
    DocumentHubData_Languages =  models.ForeignKey(
        DocumentHub_Languages, on_delete=models.CASCADE)
    DocumentHubData_Author = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Document Hub Data"
        ordering = ['DocumentHubData_Title']

    def __str__(self):
        return self.DocumentHubData_Title

    def get_DocumentHubData_slug_splited(self):
        return self.DocumentHubData_Tags.split('-')
