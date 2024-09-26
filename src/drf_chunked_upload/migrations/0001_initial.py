# Generated by Django 3.2.3 on 2021-05-17 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import drf_chunked_upload.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChunkedUpload",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=255,
                        null=True,
                        upload_to=drf_chunked_upload.models.generate_filename,
                    ),
                ),
                ("filename", models.CharField(max_length=255)),
                ("offset", models.BigIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Incomplete"), (2, "Complete")], default=1
                    ),
                ),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chunkedupload",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
