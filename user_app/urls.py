from django.urls import path
from .views import user_signup, user_login, user_logout, show_user_profile, edit_user_profile, change_user_password, reset_user_password

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', show_user_profile, name='show_profile'),
    path('edit_profile/', edit_user_profile, name='edit_profile'),
    path('change_password/', change_user_password, name='change_password'),
    path('reset_password/', reset_user_password, name='reset_password'),
]
