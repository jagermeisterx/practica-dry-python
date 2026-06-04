from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm


def inicio(request):
    return render(request, "core/inicio.html")


def acerca(request):
    return render(request, "core/acerca.html")


def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():          # aquí corre toda la validación del backend
            form.save()
            messages.success(request, "¡Gracias! Tu mensaje fue enviado.")
            return redirect("contacto")   # patrón Post-Redirect-Get
    else:
        form = ContactoForm()
    return render(request, "core/contacto.html", {"form": form})