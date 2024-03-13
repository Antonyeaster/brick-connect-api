from django.urls import path
from notifications import views

urlpatterns = [
    path("notifications/", views.NotificationsList.as_view()),
    path("notifications//<int:pk>/", views.NotificationsDetail.as_view())
]