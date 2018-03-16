from django import forms
from django.forms.widgets import HiddenInput
from django.core import validators
class FormDetails(forms.Form):
    first_name =forms.CharField()
    last_name = forms.CharField()
    email_id = forms.EmailField()
    botcatcher =forms.CharField(required=False,widget=HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatch = self.cleaned_data['botcatcher']
    #     if len(botcatch)>0:
    #         raise forms.ValidationError("Bot Detected")
    #     return botcatch
    #
    # def clean_first_name(self):
    #      first = self.cleaned_data['first_name']
    #      if first[0].lower() !='s':
    #             raise forms.ValidationError('It should start with s')
    #      return first