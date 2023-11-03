from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-submit/', views.contact_async, name='contact-submit'),
    path('success/', views.success, name='success'),
    path('career-guidance/', views.career, name='careerguidance'),
    path('vocation-blog/', views.vocation, name='vocationblog'),
    path('training/', views.training, name='training'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:slug>/', views.article_post, name='article-post'),
    path('services/<slug:slug>/', views.service_page, name='service-page')
]

