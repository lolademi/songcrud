# Generated by Django 4.1.2 on 2022-11-02 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=10)),
                ("lastname", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("date_released", models.DateField()),
                ("likes", models.IntegerField()),
                (
                    "artiste",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="musicapp.artise",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lyric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("song_id", models.IntegerField()),
                (
                    "song_title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="musicapp.song"
                    ),
                ),
            ],
        ),
    ]
