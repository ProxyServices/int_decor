from django.conf.urls import path,re_path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog_details/' views.post_detail, name='post_detail'),
]
