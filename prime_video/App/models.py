from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=120)
    release_year = models.PositiveIntegerField()
    poster_url = models.URLField()
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-release_year", "title"]
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title
