from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^read/', views.read_blog, name='readblog'),
    url(r'^hi/', views.say_hi, name='hi'),
    url(r'^test/', views.test, name='test'),
    #url(r'^check/', views.check_module_mode, name='check_mode'),

]
