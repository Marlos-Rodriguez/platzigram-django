from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.singup_view, name='signup'),
    path('me/profile/', views.update_profile, name='update_profile')
]
