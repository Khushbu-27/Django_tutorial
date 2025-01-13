
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from users.models import Profile

class UserRegistraionForm(UserCreationForm):
    
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Phone number must be entered in the format: '+999999999'.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
        
class UpdateProfileForm(forms.ModelForm):
    
    email = forms.EmailField(max_length=254)
    
    class Meta:
        
        model = Profile
        fields = ['profile_image']