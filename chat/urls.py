from django.urls import path

from .views import chat_page, chat_response, clear_chat

urlpatterns = [
    path("", chat_page, name="chat_page"),
    path("chat/", chat_response, name="chat_response"),
    path("clear-chat/", clear_chat, name="clear_chat"),
]