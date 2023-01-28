# Generated by Django 4.1.5 on 2023-01-27 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_business_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='category',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='category',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='commodity',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commodity',
            name='quantity',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commodity',
            name='volume',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
