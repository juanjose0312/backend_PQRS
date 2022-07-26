from django.urls import path
from .views import Pqrs_view

urlpatterns = [
    path('pqrs/',Pqrs_view.as_view(), name="pqrs_list"),
    path('pqrs/<int:id>',Pqrs_view.as_view(), name="pqrs_process"),
]
