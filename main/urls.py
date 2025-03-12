from django.urls import path
from main import views
urlpatterns = [
    path('length',views.length, name="length"),
    path('weight',views.weight, name="weight"),
    path('temperature',views.temperature, name="temperature"),
]
