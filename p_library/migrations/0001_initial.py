# Generated by Django 4.0.6 on 2022-07-15 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField(verbose_name='Название')),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('copy_count', models.SmallIntegerField(default=1, editable=False, verbose_name='Число копий')),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=12, verbose_name='Цена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.author')),
            ],
        ),
    ]
