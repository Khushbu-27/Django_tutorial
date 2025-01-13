from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from users import userprofile
from users.models import Profile
from .form import UpdateProfileForm, UserRegistraionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form = UserRegistraionForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Your account created sucessfully. you can login now.')
            return redirect('login')
    else:
        form = UserRegistraionForm()
    
    return render(request, 'users/register.html',{'form': form})

@login_required
def profile_update(request):
    
    # Get or create the user's profile
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user_profile)
        form.fields['email'].initial = request.user.email
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = request.user
            user.email = email  
            user.save()

            form.save()  
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  
    else:
        form = UpdateProfileForm(instance=user_profile)
        form.fields['email'].initial = request.user.email

    return render(request, 'users/profile.html', {'form': form, 'user_profile': user_profile})

# def blog_logout(request):
#     logout(request)
#     return redirect('login')


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')
