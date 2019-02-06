from django import forms
from django.contrib.auth.models import User
from .models import Post1, Profile

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post1
        fields =(
            'title',
            'body',
            'status',
        )
class UserLoginForm(forms.Form):
    username = forms.CharField(label= "")
    password = forms.CharField(label="",widget=forms.PasswordInput)




class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Entrer Password Here...'}))
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = (
          'username',
          'first_name',
          'last_name',
          'email',
        )
def clean_confirm_password(self):
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')
    if password != confirm_password:
        raise forms.ValidationError("Password Mismatch")
    return confirm_password



class UserEditForm(forms.ModelForm):
        class Meta:
            model = User
            fields = (
                'username',
                'first_name',
                'last_name',
                'email',
            )
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)