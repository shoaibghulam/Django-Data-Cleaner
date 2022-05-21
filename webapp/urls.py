
from django.urls import path
from .views import *
urlpatterns = [
   path('',DashboardView.as_view(),name="DashboardView"),
   path('upload',UploadView.as_view(),name="DashboardView"),
   path('data-view/<int:id>',DataView.as_view(),name="DashboardView"),
   path('delete-sheet/<int:id>',SheetDeleteView.as_view(),name="deletesheet"),
   path('login',LoginView.as_view(),name="login"),
   path('logout',LogOut.as_view(),name="logout"),
  
]
