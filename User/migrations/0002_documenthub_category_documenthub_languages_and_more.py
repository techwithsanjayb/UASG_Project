# Generated by Django 4.1 on 2022-09-08 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentHub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentHub_CategoryType', models.CharField(max_length=100)),
                ('DocumentHub_Cat_Status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Document Hub Category',
                'ordering': ['DocumentHub_CategoryType'],
            },
        ),
        migrations.CreateModel(
            name='DocumentHub_Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentHub_LanguagesType', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'DocumentHub LanguagesType',
                'ordering': ['DocumentHub_LanguagesType'],
            },
        ),
        migrations.CreateModel(
            name='DocumentHubData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentHubData_Title', models.CharField(max_length=100)),
                ('DocumentHubData_Tags', models.SlugField()),
                ('DocumentHubData_PublishedDate', models.DateTimeField(auto_now_add=True)),
                ('DocumentHubData_CreationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('DocumentHubData_FileSize', models.CharField(max_length=30)),
                ('DocumentHubData_LastUpdatedDate', models.DateTimeField(auto_now=True, null=True)),
                ('DocumentHubData_UploadSupportDocument', models.FileField(upload_to='User/Documenthub')),
                ('DocumentHubData_DownloadCounter', models.IntegerField()),
                ('DocumentHubData_PublishedStatus', models.CharField(choices=[('Published', 'PUBLISHED'), ('Unpublished', 'UNPUBLISHED')], default='published', max_length=20)),
                ('DocumentHubData_Author', models.CharField(max_length=100)),
                ('DocumentHubData_Author2', models.CharField(max_length=100)),
                ('DocumentHubData_CategoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.documenthub_category')),
                ('DocumentHubData_Languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.documenthub_languages')),
            ],
            options={
                'verbose_name_plural': 'Document Hub Data',
                'ordering': ['DocumentHubData_Title'],
            },
        ),
    ]
