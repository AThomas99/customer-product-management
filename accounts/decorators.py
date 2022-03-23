from ssl import wrap_socket
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect, render

# A decorator is a function that takes in another function as a parameter and add a functionality before the original functionality is called.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            else:
                return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            print(allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not allowed here..')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            print(group)
        if group == 'customer':
            return redirect('user-page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
            
    return wrapper_func