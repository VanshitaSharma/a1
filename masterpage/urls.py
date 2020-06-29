from django.views.generic.base import RedirectView
from django.urls import path
from .import views
from django.views.generic.list import ListView

urlpatterns = [
    path('home/',views.home,name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('notice/',views.NoticeListView.as_view()),
    path('notice/<int:pk>',views.NoticeDetailView.as_view()),
    path('',RedirectView.as_view(url="notice/")),

]
