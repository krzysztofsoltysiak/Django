from django.urls import path, include
from . import views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.home, name='main-home'),
    path('blog/', include('blog.urls'), name='blog-home')

]