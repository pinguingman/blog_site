from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from blog.models import Blog_record, User
from .forms import MessageForm


class IndexView(View):
    """
    Index page view.
    Return all posts in reverse chronological order.
    """

    def get(self, request):
        records = Blog_record.objects.all().order_by('-creation_date')
        return render(request, 'blog/index.html', {
            'records': records,
        })


class UserView(View):
    """
    Selected user page.
    Return all posts in reverse chronological order.
    """

    def get(self, request, username):
        records = Blog_record.objects.filter(author__username=username).order_by('-creation_date')
        # 404 if user does not exist
        selected_user = get_object_or_404(User, username=username)
        # redirect to 'blog:user_blog' if user try to get own page.
        if request.user.is_authenticated() and username == request.user.get_username():
            return HttpResponseRedirect(reverse('blog:user_blog'))
        # check subscription
        if request.user.is_authenticated():
            current_user = User.objects.get(username=request.user.get_username())
            is_subscribed = bool(not current_user.subscriptions.filter(username=username))
        else:
            is_subscribed = False
        return render(request, 'blog/user_page.html', {
            'records': records,
            'is_subscribed': is_subscribed
        })


class SubscribeToUser(LoginRequiredMixin, View):
    """
    Subscribe/unsubscribe logged user to selected user.
    Redirect to selected user page.
    """

    def get(self, request, username):
        current_user = User.objects.get(username=request.user.get_username())
        user_to_subscribe = User.objects.get(username=username)
        if user_to_subscribe == current_user:
            return HttpResponseRedirect(reverse('blog:user_blog'))
        if current_user.subscriptions.filter(username=username):
            # Unsubscribe and remove seen posts.
            all_user_posts = Blog_record.objects.filter(author=user_to_subscribe)
            current_user.seen_posts.remove(*all_user_posts)
            current_user.subscriptions.remove(user_to_subscribe)
        else:
            # Subscribe.
            current_user.subscriptions.add(user_to_subscribe)
        return HttpResponseRedirect(reverse(
            'blog:user_page',
            kwargs={'username': username}
        ))


class SubscriptionsView(LoginRequiredMixin, View):
    """
    Subscriptions page.
    Return all subscribed users posts in reverse chronological order.
    """

    def get(self, request):
        current_user = User.objects.get(username=request.user.get_username())
        users = current_user.subscriptions.all()
        records = Blog_record.objects.filter(author__in=users).order_by('-creation_date')
        return render(request, 'blog/subscriptions_page.html', {
            'records': records,
        })


class BlogView(LoginRequiredMixin, View):
    """
    Logged user page.
    GET - return logged user posts and new post form.
    POST - create new post and redirect to GET.
    """

    def get(self, request):
        current_user = User.objects.get(username=request.user.get_username())
        records = Blog_record.objects.filter(author=current_user).order_by('-creation_date')
        form = MessageForm()
        return render(request, 'blog/blog.html', {
            'records': records,
            'form': form
        })

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            author = User.objects.get(username=request.user.get_username())
            new_blog_record = Blog_record(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                author=author
            )
            new_blog_record.save()
            return HttpResponseRedirect(reverse('blog:user_blog'))
        else:
            current_user = User.objects.get(username=request.user.get_username())
            records = Blog_record.objects.filter(author=current_user).order_by('-creation_date')
            return render(request, 'blog/blog.html', {
                'records': records,
                'form': form
            })


class MarkRecord(View):
    """
    Mark record as seen by current user.
    """

    def get(self, request, username, record_id):
        current_user = User.objects.get(username=username)
        current_record = Blog_record.objects.get(pk=record_id)
        if current_record.user_set.filter(username=username):
            current_record.user_set.remove(current_user)
        else:
            current_record.user_set.add(current_user)
        return HttpResponse('Ok')
