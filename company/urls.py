"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from company_user.views import home, introduction, waytocome, login
from board.views import NoticeList,FreeBoardList,ReferenceList, BoardDetail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('com_user/', include('company_user.urls')),
    path('', home),
    path('login/', login),
    path('company/introduction/', introduction),
    path('company/waytocome/', waytocome),
    path('board/notice/', NoticeList.as_view()),
    path('board/<int:pk>/', BoardDetail.as_view()),
    path('board/freeboard/', FreeBoardList.as_view()),
    path('board/reference/', ReferenceList.as_view()),
]
