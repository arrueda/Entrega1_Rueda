from django.urls import path
from . import views


urlpatterns = [

    path("", views.inicio),
    path("listapage_tel1", views.listapage_tel1),
    path("listapage_tel2", views.listapage_tel2),
    path("listapage_tel3", views.listapage_tel3),
    path("alta_curso", views.alta_curso),
    path("alta_tel_ter", views.alta_tel_ter),
    path("alta_tel_satel", views.alta_tel_satel),
    path("buscar_nombre", views.buscar_nombre),
    path("buscar", views.buscar)

]