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
from company_user.views import home, introduction, waytocome, login, businesCoast, businessHarbor, businessMarEnv, businessMarPhysics,businessGIS, recruit
from board.views import NoticeList,ReferenceList, NoticeboardDetail, ReferenceboardDetail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('com_user/', include('company_user.urls')),
    path('', home),
    path('login/', login),
    path('company/introduction/', introduction),
    path('company/waytocome/', waytocome),
    path('business/coast/', businesCoast),
    path('business/harbor/', businessHarbor),
    path('business/marineenvironment/', businessMarEnv),
    path('business/marinephysics/', businessMarPhysics),
    path('business/gis/', businessGIS),
    path('board/notice/', NoticeList.as_view()),
    path('board/notice/<int:pk>/', NoticeboardDetail.as_view()),
    path('board/reference/<int:pk>/', ReferenceboardDetail.as_view()),
    path('board/reference/', ReferenceList.as_view()),
    path('recruit', recruit),

    # path('comment/modify/question/<int:comment_id>/', comment_modify_question, name='comment_modify_question'),
    # path('comment/delete/question/<int:comment_id>/', comment_delete_question, name='comment_delete_question'),
]
