from django.urls import path

from . import views

urlpatterns = [
    path('',views.check_login),
    path('login_view',views.login_view,name='login_view'),
    path('sign_up_view',views.sign_up_view,name='sign_up_view'),
    path('create_user',views.create_user,name='create_user'),
    path('user_login',views.user_login,name='user_login'),
    path('home',views.home_view,name='home'),
    path('log_out',views.log_out,name='log_out'),
    path('add_todo_list',views.add_todo_list,name='add_todo_list'),
    path('delete_individual/<int:id>',views.delete_individual,name='delete_individual'),
    path('edit_each',views.edit_each,name='edit_each'),  
]