# blogs/

try:
    from django.urls import path
except Exception:
    # Fallback for environments where django.urls.path isn't available
    # Convert simple '<int:name>' path converters into regex groups for django.conf.urls.url
    from django.conf.urls import url as _url
    import re

    def path(route, view, kwargs=None, name=None):
        pattern = re.sub(r'<int:(\w+)>', r'(?P<\1>\\d+)', route)
        pattern = r'^%s$' % pattern
        return _url(pattern, view, kwargs, name=name)

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
