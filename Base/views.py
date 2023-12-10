from django.shortcuts import render

# Create your views here.

# s for startapp and sign

def index(request):
    return render(request,"Base/Templates/index.html")

# authentication
def s_choice(request):
    return render(request, "Base/Templates/authentication/chosesign.html")

# sign ups and dign ins for startapp owners and invester will be one view

def s_ininv(request):
    return render(request, "Base/Templates/authentication/signininv.html")

def s_inowner(request):
    return render(request, "Base/Templates/authentication/signinowner.html")

def s_upinv(request):
    return render(request, "Base/Templates/authentication/signupinv.html")

def s_upowner(request):
    return render(request, "Base/Templates/authentication/signupowner.html")

# ...end...

def checkout(request):
    return render(request, "Base/Templates/checkout.html")

def home(request):
    return render(request, "Base/Templates/home.html")

def messages(request):
    return render(request, "Base/Templates/messages.html")

def overview(request):
    return render(request, "Base/Templates/overview.html")

# p for profile

def p_inv(request):
    return render(request, "Base/Templates/profileinv.html")

def p_invform(request):
    return render(request, "Base/Templates/profileinvform.html")

def p_owner(request):
    return render(request, "Base/Templates/profileowner.html")



def s_form(request):
    return render(request, "Base/Templates/startappform.html")













