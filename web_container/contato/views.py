from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
# Create your views here.


def fale_conosco(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # Aqui o corpo da mensagem é construído, com o assunto e a mensagem em si, de acordo com
            # os dados do formulário
            subject = "Fale Conosco da Transportadora"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['emailid'],
                'phonenumber': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            # A mensagem é construida na formatação necessária para o envio da mensagem
            message = "Nome do Remetente: {} {}\n\nEmail: {}\nTelefone: {}\n\nAssunto: {}\n\nMensagem: {}".format(body.get('first_name'), body.get('last_name'), body.get('email'), body.get('phonenumber'), body.get('subject'), body.get('message'))
            sender = form.cleaned_data['emailid']
            recipient = ['transportadoravietna@gmail.com']
            # Faz o envio da mensagem, retornando para a view do 'fale conosco' com uma mensagem de sucesso
            # E retorna uma falha na requisição caso a mensagem falhe ao ser enviada. Caso haja um problema
            # no formulário, ele retorna o formulário com os dados informados e onde está o problema para
            # correção. Caso seja a primeira renderização, retorna o formulário limpo.
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
                messages.success(request, "Mensagem Enviada com sucesso!")
                form = ContactMeForm()
                return render(request, 'email/contato.html', {'form': form, 'msg': True})
            except BadHeaderError:
                return HttpResponse("Houve um erro na requisição.")
        else:
            form = ContactMeForm(request.POST)
            return render(request, 'email/contato.html', {'form': form, 'msg': False})
    else:
        form = ContactMeForm()
        return render(request, 'email/contato.html', {'form': form, 'msg': False})
