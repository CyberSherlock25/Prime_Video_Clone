from django.db import migrations


def seed_movies(apps, schema_editor):
    Movie = apps.get_model("App", "Movie")

    from App.movies import movies_data

    Movie.objects.bulk_create(
        [
            Movie(
                title=movie["name"],
                genre=movie["genre"],
                release_year=movie["releaseYear"],
                poster_url=movie["bannerUrl"],
                is_featured=movie["id"] == 1,
            )
            for movie in movies_data
        ]
    )


def remove_movies(apps, schema_editor):
    Movie = apps.get_model("App", "Movie")

    from App.movies import movies_data

    Movie.objects.filter(
        title__in=[movie["name"] for movie in movies_data]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_movies, remove_movies),
    ]