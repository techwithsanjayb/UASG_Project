# Generated by Django 4.1 on 2022-09-07 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenthubdata',
            name='DocumentHubData_CategoryType',
        ),
        migrations.DeleteModel(
            name='DocumentHub_Category',
        ),
        migrations.DeleteModel(
            name='DocumentHubData',
        ),
    ]
