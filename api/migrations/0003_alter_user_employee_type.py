# Generated by Django 4.1.5 on 2023-01-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_department_user_employee_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_type',
            field=models.CharField(choices=[(1, ' External'), (0, 'Internal')], max_length=10),
        ),
    ]
