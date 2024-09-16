from django.urls import path
from . import views  

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('get-all-data/',views.get_all_data, name="get-all-data"),
    path('get-single-data/<str:email>/',views.single_user_data, name="get-single-data")
]
