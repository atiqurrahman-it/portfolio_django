# Generated by Django 4.1 on 2022-09-07 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_portfolio_client_adderss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extera_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('eimage', models.ImageField(blank=True, upload_to='product_pic/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.portfolio')),
            ],
        ),
    ]