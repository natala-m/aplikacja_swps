# Generated by Django 4.2.16 on 2025-01-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MojeFinanse', '0003_rename_desc_expenses_description_alter_expenses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
