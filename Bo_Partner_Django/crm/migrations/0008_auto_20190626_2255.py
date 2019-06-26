# Generated by Django 2.0.13 on 2019-06-26 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_kontaktfirma_mitarbeiter_uni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontaktfirma',
            old_name='mitarbeiter_uni',
            new_name='hsbo_mitarbeiter',
        ),
        migrations.AlterField(
            model_name='kontaktfirma',
            name='firma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.Firma'),
        ),
    ]
