# Generated by Django 4.2.2 on 2023-07-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('INCOMPLETED', 'Incompleted'), ('COMPLETED', 'Completed'), ('PENDING', 'Pending'), ('HOLD', 'Hold'), ('PROCESSING', 'Processing')], max_length=50, null=True),
        ),
    ]
