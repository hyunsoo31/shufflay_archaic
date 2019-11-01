from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
import os


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def summary(self):
        return self.text[:100]

class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length = 255, default='[1,2,3,4,5,6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) +'\n'
        self.update_date = timezone.now()
        self.save()

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    def delete(self):
        os.remove(settings.MEDIA_ROOT+'documents/%Y/%m/%d', self.docfile.name)
        return super(Document, self).delete()


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    schedule = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
