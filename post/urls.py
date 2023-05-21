from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload_post, name='upload-post'),
    path('delete/<int:id>/', views.delete_post, name='delete-post'),
    path('', views.posts_page, name='posts-page'),
]
