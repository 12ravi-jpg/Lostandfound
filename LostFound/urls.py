from django.contrib import admin
from django.urls import path, include  # <-- CORRECTED LINE 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finder.urls')),  # This line tells Django to look at your 'finder' app
]