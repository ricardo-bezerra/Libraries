# Generated by Django 5.1.3 on 2024-11-12 19:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55)),
                ('author', models.CharField(max_length=55)),
                ('release_year', models.DateField()),
                ('state', models.CharField(max_length=15)),
                ('pages', models.IntegerField()),
                ('publishing_company', models.CharField(max_length=55)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
