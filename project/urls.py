"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, FormMixin, UpdateView, DeleteView
from earthseed import views
from earthseed.views import event_signup, order_book, post_topic
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookList.as_view(), name='book_list'),
    path('events/', views.EventList.as_view(), name='event_list'),
    path('forums/', views.ForumList.as_view(), name='forum_list'),
    path('post_reply/', views.post_reply, name='post_reply'),
    path('event_signup/', views.event_signup, name='event_signup'),
    path('order/', views.order_book, name='order_book'),
    path('topics/', views.post_topic, name='post_topic'),
    path('edit_topic/<int:pk>/', views.TopicUpdate.as_view(), name='edit_topic'),
    path('edit_reply/<int:pk>/', views.ReplyUpdate.as_view(), name='edit_reply'),
    path('delete_reply/<int:pk>/', views.ReplyDelete.as_view(), name='delete_reply'),
    
    

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

                              