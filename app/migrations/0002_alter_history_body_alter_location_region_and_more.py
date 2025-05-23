# Generated by Django 4.2.20 on 2025-04-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(choices=[('tashkent', 'TASHKENT'), ('bukhara', 'Bukhara'), ('samarkand', 'Samarkand'), ('fergana', 'Fergana'), ('navoi', 'Navoi'), ('andijon', 'Andijan'), ('namangan', 'NAMANGAN'), ('jizzakh', 'Jizzakh'), ('sirdaryo', 'SIRDARYO'), ('surxandaryo', 'SURXANDARYO'), ('qashqadaryo', 'QASHQADARYO'), ('xorazm', 'XORAZM')], max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='body',
            field=models.TextField(),
        ),
    ]
