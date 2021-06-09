from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    Nome = forms.CharField(label = 'Nome', max_length=100)
    Email = forms.CharField(label = 'Email', max_length=100)
    Mensagem = forms.CharField(label= 'Mensagem', widget=forms.Textarea())

    def send_main(self):
        nome = self.cleaned_data['Nome']
        email = self.cleaned_data['Email']
        mensagem = self.cleaned_data['Mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject=mensagem,
            body=conteudo,
            from_email='agustavo20151@gmail.com',
            to={'agustavo20151@gmail.com',},
            headers={'Replay-to': email}
        )

        mail.send()
