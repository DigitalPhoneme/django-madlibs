from django.urls import path
from .views import HomeView, PlayView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('play', PlayView.as_view(), name='play')
]