from blog_site.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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
