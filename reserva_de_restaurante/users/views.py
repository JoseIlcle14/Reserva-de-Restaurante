from django.shortcuts import render
from . models import Usuários



def cadastro(request):
    if request.method == 'GET':
       return render(request, 'users/cadastro.html')
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        senha = request.POST.get("senha")

        user = Usuários.objects.filter(cpf = cpf).first()
        if user:
            context = {
                'user' : user,
                'msg' : 'Usuário já cadastrado'
            }
            return render(request, 'users/cadastro.html', context)
        else:
            user = Usuários.objects.create(nome=nome,email=email,cpf=cpf,senha=senha)
            user.save()
            context = {
                'user' : user,
                'msg' : 'Usuário cadastrado com sucesso'
            }
            return render(request, 'users/cadastro.html', context)

def login_users(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:

        cpf = request.POST.get("cpf")
        senha = request.POST.get("senha")
        
        user = Usuários.objects.filter(cpf = cpf, senha= senha).first()

        if user:
            context ={
                'msg' : 'usuário logado',
                'user' : user
            }
            return render(request, 'users/login.html', context)
        else:
            return render(request, 'users/cadastro.html')