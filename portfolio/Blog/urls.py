from django.urls import path
from .views import all_blogs, details, titled_url

urlpatterns = [
    path('', all_blogs, name='allblogs'),
    path('<int:blog_id>/', details, name='details'),
    path('<str:slog>', titled_url, name='titled')
]
