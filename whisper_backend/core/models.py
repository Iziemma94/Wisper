from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class AnonymousUser(models.Model):
    session_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return f"Anon {str(self.session_id)[:8]}"


class Confession(models.Model):
    user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}"


class Comment(models.Model):
    user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    confession = models.ForeignKey(Confession, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    reporter = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
