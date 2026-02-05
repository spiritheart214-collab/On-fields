from django import forms

class MailSendForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    textarea = forms.CharField(widget=forms.Textarea, max_length=300, required=True)
