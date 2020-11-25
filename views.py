from django.shortcuts import render, redirect
from .forms import SolicitarForm
from .entidades.sol import Sol
from .services import sol_service

def consultar(request):
    return render(request, 'solicitar_extras/consultar_extras.html')

def cadastrar_sol(request):
    if request.method == "POST":
        form_sol = SolicitarForm(request.POST or None)
        if form_sol.is_valid():
           startdate = form_sol.cleaned_data["startdate"]

           endate = form_sol.cleaned_data["endate"]

           justificate = form_sol.cleaned_data["justificate"]
           nova_sol = Sol(startdate=startdate, endate=endate, justificate=justificate)
           sol_service.cadastrar_sol(nova_sol)
           return redirect('consultar')
    else:
        form_sol = SolicitarForm()
        return render(request, 'solicitar_extras/form_sol.html', {"form_sol": form_sol})

"""def retornaDadosTemp(request):
    form = SolicitarForm(request.GET or None)
    if form.is_valid():
        var = form.cleaned_data["startdate"]
    return render(request, 'solicitar_extras/form_sol.html', {"form": form})"""