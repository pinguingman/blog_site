from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


from .send_emails import send_emails

import threading


class User(AbstractUser):
    """
    Model of user.
    Additionally to AbsctactUser - contains subscriptions list and seen posts list.
    """
    subscriptions = models.ManyToManyField('self', blank=True, default=None, symmetrical=False)
    seen_posts = models.ManyToManyField('Blog_record', blank=True, default=None)


class Blog_record(models.Model):
    """
    Model of blog record.
    Contains record title, text, author (User) and creation date.
    """
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """
        Additionally to save, send email to all subscribers.
        """
        subscribers = User.objects.filter(subscriptions=self.author)
        emails = [x.email for x in subscribers if x.email]
        if emails:
            thread = threading.Thread(target=send_emails, args=(emails, self.author.username, self.title,))
            thread.start()
        super().save(args, kwargs)

    def __str__(self):
        return self.title
