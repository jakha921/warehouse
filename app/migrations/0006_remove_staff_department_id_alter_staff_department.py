# Generated by Django 4.2.7 on 2024-06-18 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_staff_department_id_alter_transmitting_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='department_id',
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.department', verbose_name="Bo'limi"),
        ),
    ]