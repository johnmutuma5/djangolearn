from django.urls import re_path, path
from . import views

urlpatterns = [
    # path(r'', )
    re_path(r'^$', views.index_html, name='posts_index')
]
