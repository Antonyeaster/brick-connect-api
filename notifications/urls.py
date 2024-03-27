from django.urls import path
from notifications import views

urlpatterns = [
    path("notifications/", views.NotificationsList.as_view(), name="notifications_list",),
    path("notifications/<int:pk>", views.NotificationsDetail.as_view(), name="notification_detail",)
]
