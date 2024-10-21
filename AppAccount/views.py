from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppEmployee.models import *


# Create your views here.


def LoginView(request):
    if request.user.is_authenticated:
        return redirect("Dashboard")
    else:
        template_name = "Login.html"
        message = ""
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                request.session['is_logged'] = True
                request.session['username'] = user.username
                # request.session['user_role'] = user.profile.user_role

                EmployeeData = list(
                    Employee.objects.select_related('EmployeeInformation').filter(user_id=user.id).values_list(
                        'employee_code',
                        'employeeinformation__title'))[0]
                request.session['emp_code'] = EmployeeData[0]
                request.session['login_name'] = EmployeeData[1]

                return redirect('Dashboard')

                # if user.profile.user_role == "ceo" or user.profile.user_role == "account" or user.profile.user_role == "manager" or user.profile.user_role == "mardo" or user.profile.user_role == "admin":
                #     return redirect('Dashboard')
                #
                # if user.profile.user_role == "cashier" or user.profile.user_role == "salesman":
                #     return redirect('POS/0')

        else:
            return render(request, template_name)


@login_required(login_url='LoginView')
def LogoutView(request):
    logout(request)
    return redirect('LoginView')
