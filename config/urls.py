"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", registration_page, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_user, name="logout"),
    path("profile/", profileView, name="profile"),
    path("dating/", dating_profile_register, name="dating"),
    path("personality/", personality_register, name="personality"),
    path("matchmaking/", matchmakingView, name="matchmaking"),
    path("messages/<int:id>", messagesView, name="messages"),
    path('send_message/<int:recipient_id>/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('message/<int:message_id>/', message_detail, name='message_detail'),
    path("partner_profile/<int:id>", partner_profile_view, name="partner"),
    path("", home_page, name="home"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
