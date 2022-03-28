from django import forms
from .models import Cargo
from .models import Departamento
from .models import Empleado
class CargoForm(forms.ModelForm):
    
    class Meta:
        model = Cargo
        fields = ['descripcion' ,'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Ingrese un cargo', 
                'class': 'form_group', 
                'required': True
            })#se le pone la coma 
            # 'descripcion': forms.TextInput(attrs={
            #     'placeholder': 'Ingrese un cargo', 
            #     'class': 'form_group', 
            #     'required': True
            # })
            # }
        }
class DepartamentoForm(forms.ModelForm):
    
    class Meta:
        model = Departamento
        fields = ['descripcion' ,'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Ingrese un departamento', 
                'class': 'form_group', 
                'required': True 
            }) 
        }
class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = ['nombre','cedula','cargo','departamento','sueldo' ]
        # 'cedula',
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese Nombre del Empleado', 
                'class': 'form-group', 
                'required': True 
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder': 'Ingrese su número de cédula',
                'class': 'form-group',
                'required':True
            }),
            'cargo': forms.Select(attrs={
                'class': 'form-group',
                'required':True
            }),
            'departamento': forms.Select(attrs={
                'class': 'form-group',
                'required':True
            }),    
            'sueldo': forms.TextInput(attrs={
                'placeholder': 'Ingrese sueldo del Empleado',
                'class': 'form-group',
                'required':True
            }) 
        }                    