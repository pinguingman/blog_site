from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from blog_site.settings import EMAIL_HOST_USER


class User(AbstractUser):
    """
    Model of user.
    Additionally to AbsctactUser - contains subscriptions list and seen posts list.
    """
    subscriptions = models.ManyToManyField('self', blank=True, default=None, symmetrical=False)
    seen_posts = models.ManyToManyField('Blog_record', blank=True, default=None)


def send_emails(emails, author, title):
    """
    Send emails to given addresses with author and title.
    """
    subject = 'New post by %s' % author.capitalize()
    message = '%s wrote a new post with the title: %s' % (author.capitalize(), title)
    print('Sending emails to ', emails)
    send_mails_count = send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=emails
    )
    print('Successfully sent %s - letters' % send_mails_count)


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
        send_emails(emails, self.author.username, self.title)
        super().save(args, kwargs)
