from django.urls import re_path, path
from . import views

urlpatterns = [
    # path(r'', )
    re_path(r'^$', views.posts_index, name='posts_index')
]
