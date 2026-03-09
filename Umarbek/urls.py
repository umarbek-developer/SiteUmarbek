from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]