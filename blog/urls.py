from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # index page with all posts
    url(r'^$', views.IndexView.as_view(), name='index'),
    # page with all subscriptions
    url(r'^subscriptions/$', views.SubscriptionsView.as_view(), name='subscriptions_page'),
    # logged user page
    url(r'^my_page/$', views.BlogView.as_view(), name='user_blog'),
    # selected user page
    url(r'^user/(?P<username>\w+)/$', views.UserView.as_view(), name='user_page'),
    # link to subscribe to selected user
    url(r'^user/(?P<username>\w+)/subscribe/$', views.SubscribeToUser.as_view(), name='subscribe_to_user'),
]
