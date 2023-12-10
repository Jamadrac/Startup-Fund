from django.urls import path
from Base import views

urlpatterns = [
    path('',views.index,name='index'),

    path('choice/',views.s_choice,name='s_choice'),  
    path('signinvestor/',views.s_ininv,name='s_ininv'),  
    path('signowner/',views.s_inowner,name='s_inowner'), 
    path('signupinvestor/',views.s_upinv,name='s_upinv'), 
    path('signupowner/',views.s_upowner,name='s_upowner'), 

    path('checkout/',views.checkout,name='checkout'), 
    path('startupfund/',views.home,name='home'), 
    path('messages/',views.messages,name='messages'), 
    path('overview/',views.overview,name='overview'), 

    path('investorprofile/',views.p_inv,name='p_inv'), 
    path('investorform/',views.p_invform,name='p_invform'), 
    path('ownerprofile/',views.p_owner,name='p_owner'), 

    path('registerstartup/',views.s_form,name='s_form'), 

    # <str:pk> is for patterns that require to be specific in terms of ID's
    # path('delete/<str:pk>/',views.delete,name='delete'), 
]