# Generated by Django 4.1 on 2022-09-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_portfolio_category_alter_experience_lavel_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='Client_adderss',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='full_catefory_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
