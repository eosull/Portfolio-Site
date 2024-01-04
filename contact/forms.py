from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'form-input form-input-short'
        }), required=True, max_length=100)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-input form-input-short'
        }),required=True, max_length=100)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-input form-input-long'
        }), required=True, max_length=100)
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Message',
            'class': 'form-input form-input-long'
        }))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""