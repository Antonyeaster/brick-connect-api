from django.urls import path
from comment_like import views

urlpatterns = [
    path('commentlike/', views.CommentLikeList.as_view()),
    path('commentlike/<int:pk>/', views.CommentLikeDetail.as_view()),
]