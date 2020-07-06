from django import forms

from apps.core.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    name = forms.CharField(max_length=10, label='first name', required=True)
    message = forms.CharField(widget=forms.Textarea({'cols': 20, 'rows': 2}))

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message')
        # fields = '__all__'
        # exclude = ('name', )
