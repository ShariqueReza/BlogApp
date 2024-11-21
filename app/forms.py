from django import forms
from app.models import Comments,Subscribe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields={'content','name','email','website'}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder']='Type your comment....'
        self.fields['name'].widget.attrs['placeholder']='Name'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['website'].widget.attrs['placeholder']='Website'

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={'email':_('')}
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder']='Type your email....'
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields={'username','email','password1','password2'}

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Type your username....'
        self.fields['email'].widget.attrs['placeholder']='Type your email....'
        self.fields['password1'].widget.attrs['placeholder']='Type your password....'
        self.fields['password2'].widget.attrs['placeholder']='Repeat your password....'