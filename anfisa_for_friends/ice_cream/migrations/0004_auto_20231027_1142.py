# Generated by Django 3.2.16 on 2023-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0003_auto_20231026_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'Обёртка', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ice_creams', to='ice_cream.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='Топпинги'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='wrapper',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ice_cream', to='ice_cream.wrapper', verbose_name='Обёртка'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]
