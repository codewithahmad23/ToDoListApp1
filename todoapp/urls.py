from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('task_delete/<int:id>/',views.task_delete,name='task_delete'),
    path('task_add/',views.task_add,name='task_add'),
    path('task_update/<int:id>/',views.task_update,name='task_update'),
    #path('base/',views.base,name='base'),
]