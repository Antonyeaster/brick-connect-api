from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        from .signals import create_follow_notification, create_comment_notification
        
        from django.db.models.signals import post_save
        from followers.models import Follower  
        from comments.models import Comment 
        
        post_save.connect(create_follow_notification, sender=Follower)
        
        post_save.connect(create_comment_notification, sender=Comment)
