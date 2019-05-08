from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^subscriptions/$', views.SubscriptionsView.as_view(), name='subscriptions_page'),
    url(r'^my_page/$', views.BlogView.as_view(), name='user_blog'),
    url(r'^user/(?P<username>\w+)/$', views.UserView.as_view(), name='user_page'),
    url(r'^user/(?P<username>\w+)/subscribe/$', views.SubscribeToUser.as_view(), name='subscribe_to_user'),
]
