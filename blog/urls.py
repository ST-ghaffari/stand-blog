from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path("article-detail/<slug:slug>", views.article_detail, name="article-detail"),
    path("article-list", views.ArticleListView.as_view(), name="article_list"),
    path("category-detail/<slug:slug>", views.category_detail, name="category_detail"),
    path("search", views.search, name="search_articles"),
    path("contact-us", views.ContactUsView.as_view(), name="contact_us"),
    path("users", views.UserList.as_view(), name="user_list"),
    path("messages", views.MessageListView.as_view(), name="messages"),
    path("message/edit/<int:pk>", views.MessageUpdateView.as_view(), name="message_edit"),
    path("message/delete/<int:pk>", views.MessageDeleteView.as_view(), name="message_delete"),
    path("like/<slug:slug>/<int:pk>", views.like, name="like"),
]
