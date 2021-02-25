from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label='url',
                widget = forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Podaj Url:'})
    )