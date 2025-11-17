from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),
    
    # Registration
    path('register/user/', views.register_user, name='register_user'),
    path('register/admin/', views.register_admin, name='register_admin'),
    
    # Login / Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Main Dashboard (after login)
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Report Forms
    path('report/lost/', views.report_lost_item, name='report_lost'), 
    path('report/found/', views.report_found_item, name='report_found'),
]