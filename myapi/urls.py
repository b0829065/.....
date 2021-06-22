# from createdata.models import Numbers
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloAPIView.as_view(),name='index'),
    path('user',views.List_User.as_view(),name='list_user'),
    path('adduser',views.Add_user.as_view(),name='add_post'),
    path('deleteuser',views.Delete_user.as_view(),name='add_post'),
    path('list',views.List_post.as_view(),name='list_post'),
    path('updateuser',views.Update_user.as_view(),name='list_post'),
    path('login',views.Login.as_view(),name='login'),
]