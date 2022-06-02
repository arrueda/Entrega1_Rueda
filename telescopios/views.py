from django.shortcuts import render
from telescopios.models import Teles_cur, Teles_satel, Teles_terr
from django.http import HttpResponse
import datetime

# Create your views here.

def inicio(request):
    return render(request, "plantillas.html")


#datos para la rama de curso
def listapage_tel1(request):
    page_tel= Teles_cur.objects.all()
    datos= {"datos": page_tel}

    return render(request, "listapage_tel1.html", datos)


def alta_curso(request):
    dato_curso= Teles_cur(nom_tel_cur="Jose Arce", edad_tel_cur=30, fechalanz_tel_cur="1992-05-14")
    dato_curso.save()
    dato_curso= Teles_cur(nom_tel_cur="Juan Carlos", edad_tel_cur=35, fechalanz_tel_cur="1988-02-04")
    dato_curso.save()
    dato_curso= Teles_cur(nom_tel_cur="Cintia Ali", edad_tel_cur=30, fechalanz_tel_cur="1992-03-12")
    dato_curso.save()

    return HttpResponse("Todo Ok.")
    

def alta_curso(request):
    if request.method == "post":
        dato_curso= Teles_cur(nom_tel_cur=request.post['nom_cur'], edad_tel_cur=request.post['edad_cur'], fechalanz_tel_cur=request.post['fechalanz_cur'])
        dato_curso.save()
        return render(request, "listapage_tel1.html")
    return render(request, "listapage_tel1.html")


#datso para la rama de teles_satel
def listapage_tel2(request):
    page_tel_sat= Teles_satel.objects.all()
    datos2= {"datos2": page_tel_sat}

    return render(request, "listapage_tel2.html", datos2)


def alta_tel_satel(request):
    dato_tel_satel= Teles_satel(nom_tel_sat="Chandra", edad_tel_sat=99, fechalanz_tel_sat="1999-07-23")
    dato_tel_satel.save()
    dato_tel_satel= Teles_satel(nom_tel_sat="XMM-Newton", edad_tel_sat=22, fechalanz_tel_sat="1999-12-10")
    dato_tel_satel.save()
    dato_tel_satel= Teles_satel(nom_tel_sat="Kepler", edad_tel_sat=99, fechalanz_tel_sat="2009-03-07")
    dato_tel_satel.save()
    dato_tel_satel= Teles_satel(nom_tel_sat="Spitzer", edad_tel_sat=99, fechalanz_tel_sat="2003-08-25")
    dato_tel_satel.save()
    

    return HttpResponse("Todo Ok 2.")


def alta_tel_satel(request):
    if request.method == "post":
        dato_tel_satel= Teles_satel(nom_tel_sat=request.post['nom_sat'], edad_tel_sat=request.post['edad_sat'], fechalanz_tel_sat=request.post['fechalanz_sat'])
        dato_tel_satel.save()
        return render(request, "listapage_tel2.html")
    return render(request, "listapage_tel2.html")

    #datso para la rama de teles_terrestres
def listapage_tel3(request):
    page_tel_terr= Teles_terr.objects.all()
    datos3= {"datos3": page_tel_terr}

    return render(request, "listapage_tel3.html", datos3)


def alta_tel_ter(request):
    dato_tel_ter= Teles_terr(nom_tel_ter="Griffith", edad_tel_ter=99, fechalanz_tel_ter="1935-06-20")
    dato_tel_ter.save()
    dato_tel_ter= Teles_terr(nom_tel_ter="Mauna Kea", edad_tel_ter=99, fechalanz_tel_ter="1956-08-10")
    dato_tel_ter.save()
    dato_tel_ter= Teles_terr(nom_tel_ter="Sierra Nevada", edad_tel_ter=99, fechalanz_tel_ter="1981-06-20")
    dato_tel_ter.save()
    dato_tel_ter= Teles_terr(nom_tel_ter="Alma", edad_tel_ter=99, fechalanz_tel_ter="2011-10-03")
    dato_tel_ter.save()
    
    

    return HttpResponse("Todo Ok 3.")


def alta_tel_ter(request):
    if request.method == "post":
        dato_tel_ter= Teles_terr(nom_tel_ter=request.post['nom_ter'], edad_tel_ter=request.post['edad_ter'], fechalanz_tel_ter=request.post['fechalanz_ter'])
        dato_tel_ter.save()
        return render(request, "listapage_tel3.html")
    return render(request, "listapage_tel3.html")



def buscar_nombre(request):
    return render(request, "buscar_nombre.html")


def buscar(request):
    if request.post["nombre"]:

        return HttpResponse(f"Estamos buscando el nombre requerido en listado de curso: { request.post['nombre']}")