from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in 
            login(request, user)
            return redirect('recipes:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        print(dir(form))
        if form.is_valid():
            # print(dir(form))
            # login the user
            user = form.get_user()
            login(request, user)
            # if the user came from the recipes/create page
            # redirect them back to that page after they login
            # otherwise redirect them to the list of recipes
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('recipes:list') # don't want this     
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form':form })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    
    return redirect('recipes:list')