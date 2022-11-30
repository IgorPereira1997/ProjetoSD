from django import forms


class ContactMeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entre com seu primeiro nome'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entre com o seu sobrenome'}), required=True)
    emailid = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu email'}), required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu número'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o assunto da mensagem'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite sua mensagem'}), required=True)
