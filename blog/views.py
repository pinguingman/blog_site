from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, View

from blog.models import Blog_record, User


class IndexView(View):
    def get(self, request):
        records = Blog_record.objects.all().order_by('-creation_date')
        return render(request, 'blog/index.html', {
            'records': records,
        })


class UserView(View):
    def get(self, request, username):
        records = Blog_record.objects.filter(author__username=username).order_by('-creation_date')
        return render(request, 'blog/user_page.html', {
            'records': records,
        })


class SubscriptionsView(LoginRequiredMixin, View):
    def get(self, request):
        current_user = User.objects.get(username=request.user.get_username())
        users = current_user.subscriptions.all()
        records = Blog_record.objects.filter(author__in=users)
        return render(request, 'blog/subscriptions_page.html', {
            'records': records,
        })


class BlogView(LoginRequiredMixin, View):
    def get(self, request):
        current_user = User.objects.get(username=request.user.get_username())
        records = Blog_record.objects.filter(author=current_user)
        return render(request, 'blog/blog.html', {
            'records': records,
        })


def index(request):
    return HttpResponse('index')
