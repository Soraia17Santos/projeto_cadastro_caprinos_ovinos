from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.cobertura = request.POST.get('cobertura')
    novo_usuario.raca = request.POST.get('raca')
    novo_usuario.brinco = request.POST.get('brinco')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.data = request.POST.get('data')
    novo_usuario.reprodutor = request.POST.get('reprodutor')
    novo_usuario.peso = request.POST.get('peso')
    novo_usuario.ecc = request.POST.get('ecc')
    novo_usuario.tipo_acasalamento = request.POST.get('tipo_acasalamento')
    novo_usuario.tipo_estro = request.POST.get('tipo_estro')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': Usuario.objects.all()
        
    }
    
    return render(request,'usuarios/usuarios.html',usuarios)