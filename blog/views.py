from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View

from blog.models import Blog_record


class IndexView(View):
    def get(self, request):
        records = Blog_record.objects.all().order_by('-creation_date')
        return render(request, 'blog/index.html', {
            'records': records
        })


class UserView(View):
    def get(self, request, username):
        records = Blog_record.objects.filter(author__username=username).order_by('-creation_date')
        return render(request, 'blog/user_page.html', {
            'records': records
        })


class SubscriptionsView(View):
    def get(self, request):
        return HttpResponse('Current user subscriptions')


def index(request):
    return HttpResponse('index')
