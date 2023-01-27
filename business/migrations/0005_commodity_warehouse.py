# Generated by Django 4.1.5 on 2023-01-27 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_alter_business_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.warehouse'),
            preserve_default=False,
        ),
    ]
