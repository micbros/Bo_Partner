# Generated by Django 2.0.13 on 2019-06-26 20:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20190626_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontaktfirma',
            name='hsbo_mitarbeiter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]