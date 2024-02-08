from django.urls import path

from django.urls import path
from .views import (
    PostAPIView,
    CommentAPIView,
    ConversationAPIView,
    MessageAPIView,
    NotificationAPIView,
)


app_name = 'content'



urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='post-list-create'),
    path('comments/', CommentAPIView.as_view(), name='comment-create'),
    path('conversations/', ConversationAPIView.as_view(), name='conversation-list-create'),
    path('messages/', MessageAPIView.as_view(), name='message-list-create'),
    path('notifications/', NotificationAPIView.as_view(), name='notification-list-create'),
]
