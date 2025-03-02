# Generated by Django 5.0.7 on 2024-07-25 15:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_alter_usertodolink_id_alter_todo_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["status"]},
        ),
        migrations.AlterField(
            model_name="usertodolink",
            name="id",
            field=models.CharField(
                default=uuid.UUID("f8ade226-342f-4f3c-aea4-43e01bb23dde"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
