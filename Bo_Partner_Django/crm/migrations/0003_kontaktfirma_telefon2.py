# Generated by Django 2.2.1 on 2019-06-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190603_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontaktfirma',
            name='telefon2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
