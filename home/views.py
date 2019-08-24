from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home/home.html')

def blogs(request):
    return render(request, 'home/blogs.html')

def login(request):
    if request.method == 'POST':
        return redirect('adminHome')
    else:
        return render(request, 'home/login.html')
