from django.shortcuts import redirect, render,HttpResponse
from cmath import e
import imp
from tkinter import E
from .forms import CargoForm
from mantenimiento.forms import CargoForm
from .models import Cargo
from .forms import DepartamentoForm
from mantenimiento.forms import DepartamentoForm
from .models import Departamento
from .forms import EmpleadoForm
from mantenimiento.forms import EmpleadoForm
from .models import Empleado

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>BIENVENIDO A MI SITIO WEB</h1>")
    return render(request,"inicio.html")

def NuevoCargo(request):
    return render(request,"pages/crearNuevoCargo.html")

def NuevoDepartamento(request):
    return render(request,"pages/crearNuevoDepartamento.html")

def NuevoEmpleado(request):
    return render(request,"pages/crearNuevoEmpleado.html")

# def cargo(request):
#     return render(request,"pages/cargo.html")
#     # return HttpResponse("<h1>Mantenimiento de Cargos...</h1>")

# def departamento(request):
#     return render(request,"pages/departamento.html")
#     # return HttpResponse("<h1>Mantenimiento de Departamentos</h1>")

def empleado(request):
    return render(request,"pages/empleado.html")
    # return HttpResponse("<h1>Mantenimiento de Empleados</h1>")


def crearCargo(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("entro por post")
        cargo_form= CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            
    else:
        print("entro por get")
        cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion': 'Crear'})

def crearNuevoCargo(request):
    if request.method == "POST":
        print("entro por post")
        cargo_form= CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('cargo')
    else:
        print("entro por get")
        cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/crearNuevoCargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion': 'Crear'})



def editarCargo(request,id):
    error,cargo_form=None,None
    try:
        cargo = Cargo.objects.get(id=id)
        if request.method =="GET":
            cargo_form=CargoForm( instance=cargo)
        else:
            cargo_form=CargoForm(request.POST, instance=cargo)
            if cargo_form.is_valid():
                cargo_form.save()
                return redirect('cargo')
    except Exception as e:
        error=e

    # cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/crearNuevoCargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion': 'Actualizar'})

def eliminarCargo(request,id):

    cargo= Cargo.objects.get(id=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect("cargo")
    return render(request, 'pages/eliminar_cargo.html',{'cargo':cargo})  


def crearDepartamento(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("entro por post")
        departamento_form= DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
    else:
        print("entro por get")
        departamento_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.html", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion': 'Crear'})

def crearNuevoDepartamento(request):
    if request.method == "POST":
        print("entro por post")
        departamento_form= DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('departamento')
    else:
        print("entro por get")
        departamento_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/crearNuevoDepartamento.html", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion': 'Crear'})


def editarDepartamento(request,id):
    error,departamento_form=None,None
    try:
        departamento = Departamento.objects.get(id=id)
        if request.method =="GET":
            departamento_form=DepartamentoForm( instance=departamento)
        else:
            departamento_form=DepartamentoForm(request.POST, instance=departamento)
            if departamento_form.is_valid():
                departamento_form.save()
                return redirect('departamento')
    except Exception as e:
        error=e

    # cargo_form = CargoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/crearNuevoDepartamento.html", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion': 'Actualizar'})

def eliminarDepartamento(request,id):

    departamento= Departamento.objects.get(id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect("departamento")
    return render(request, 'pages/eliminar_departamento.html',{'departamento':departamento}) 


def crearEmpleado(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("entro por post")
        empleado_form= EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
    else:
        print("entro por get")
        empleado_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.html", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion': 'Crear'})

def crearNuevoEmpleado(request):
    if request.method == "POST":
        print("entro por post")
        empleado_form= EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('empleado')
    else:
        print("entro por get")
        empleado_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/crearNuevoEmpleado.html", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion': 'Crear'})


def editarEmpleado(request,id):
    error,empleado_form=None,None
    try:
        empleado = Empleado.objects.get(id=id)
        if request.method =="GET":
            empleado_form=EmpleadoForm( instance=empleado)
        else:
            empleado_form=EmpleadoForm(request.POST, instance=empleado)
            if empleado_form.is_valid():
                empleado_form.save()
                return redirect('empleado')
    except Exception as e:
        error=e

    # cargo_form = CargoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/crearNuevoEmpleado.html", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion': 'Actualizar'})

def eliminarEmpleado(request,id):

    empleado= Empleado.objects.get(id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect("empleado")
    return render(request, 'pages/eliminar_empleado.html',{'empleado':empleado})   