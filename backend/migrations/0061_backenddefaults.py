# Generated by Django 3.0.2 on 2021-06-06 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0060_auto_20210605_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackendDefaults',
            fields=[
                ('backend_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Backend')),
            ],
            bases=('backend.backend',),
        ),
    ]
