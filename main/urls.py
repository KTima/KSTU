from .views import *
from main.views import Homepage
from django.urls import path

urlpatterns = [
    path("",Homepage ,name='homepage'),
    path("login/",LoginUser.as_view(),name='login'),
    path("logout/",logout_user,name='logout'),
    path("newslist/",NewsListView.as_view(),name='News'),
    path("profile/",Profile,name = "profile"),
    path("createnews/",CreateNews,name='createnews'),
    path('updatenews/<int:pk>/',NewsUpdateView.as_view(),name = 'updatenews'),
    path("deletenews/<int:pk>/",NewsDeleteView.as_view(),name = "deletenews"),
    path("programmlist",ProgrammsListView.as_view(), name="programmslist"),
    path("createprogramms/",CreateProgramms,name='createprogramms'),
    path("updateprogramms/<int:pk>/",ProgrammsUpdateView.as_view(),name = 'updateprogramms'),
    path("deleteprogramms/<int:pk>/",ProgrammsDeleteView.as_view(),name = "deleteprogramms"),
]
