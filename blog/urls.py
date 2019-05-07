from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^subscriptions$', views.SubscriptionsView.as_view(), name='subscriptions_page'),
    url(r'^user/(?P<username>\w+)/$', views.UserView.as_view(), name='user_page'),
]
