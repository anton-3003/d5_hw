# Generated by Django 3.1.6 on 2021-02-04 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20210202_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='Год рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=13, verbose_name='Международный код'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='p_library.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(verbose_name='Количество экз.'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_release',
            field=models.SmallIntegerField(verbose_name='Год издания'),
        ),
    ]