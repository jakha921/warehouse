# Generated by Django 4.2.7 on 2024-06-05 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_product_count_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='FIO')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name="Bo'limi")),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lavozimi')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefon raqami')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Xodim',
                'verbose_name_plural': 'Xodimlar',
                'db_table': 'staff',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='transmitting',
            name='receiver',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Qabul qiluvchi'),
        ),
        migrations.AddField(
            model_name='transmitting',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.staff', verbose_name='Qabul qiluvchi xodim'),
        ),
    ]
