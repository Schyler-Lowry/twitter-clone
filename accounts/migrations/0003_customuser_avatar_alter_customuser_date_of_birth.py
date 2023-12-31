# Generated by Django 4.0.10 on 2023-07-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(blank=True, help_text='Enter a url for your avatar image', max_length=999),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Enter your date of birth in MM/DD/YYYY format.', null=True),
        ),
    ]
