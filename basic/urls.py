from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^accounts/login', views.log_in, name="login"),
    url(r'^accounts/auth_view', views.auth_view),
    url(r'^accounts/logout', views.log_out, name="logout"),
    url(r'^accounts/register', views.register, name="register"),
]
