from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>/', views.single_post_page), #/blog/뒤에 int형태의 값이 붙는 url이면 single_post_page 함수를 적용하라
    path('', views.index),
]
