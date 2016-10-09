from django.conf.urls import url
from userinfo import views
from userinfo.forms import LoginForm


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/list$', views.users_list, name='user_list'),
    url(r'^users/(?P<id>\d+)/$', views.user_page, name='user_page'),
    url(r'^users/create-message.html/$', views.create_message, name='create_message'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LoginForm},
        name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', 
        {'template_name': 'registration/logout.html'},
        name='logout'),
    url(r'^register/$', views.register, name='register'),
]

#
