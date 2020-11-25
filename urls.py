from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('solicitar_extras/', cadastrar_sol, name='solicitar_extras'),
    path('consultas/', consultar, name='consultar'),

]
