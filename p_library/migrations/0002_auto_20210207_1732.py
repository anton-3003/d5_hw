# Generated by Django 3.1.6 on 2021-02-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='e_mail',
            field=models.CharField(max_length=50, verbose_name='Эл.почта'),
        ),
    ]
