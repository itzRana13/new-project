import email
from urllib import request
from django.shortcuts import render
# from django.http import HttpResponse
from myaap.models import Bookinfo
from myaap.models import continfo
from myaap.models import loginfo

def homepageview(request):
    if request.method=="POST":
        P_n=request.POST.get('Place_n')
        N_p=request.POST.get('Number_p')
        A_d=request.POST.get('Arriv_d')
        L_d=request.POST.get('Leav_d')
        B_now = Bookinfo(P_name=P_n,Num_p=N_p,Arriv_d=A_d,Leav_d=L_d)
        B_now.save()

    if request.method=="POST":
        nm=request.POST.get('Name')
        pn=request.POST.get('P_num')
        email=request.POST.get('email')
        ms=request.POST.get('message')
        C_info=continfo(Name=nm,P_num=pn,email=email,message=ms)
        C_info.save()

    if request.method=="POST":
        C_e=request.POST.get('cli_email')
        ps=request.POST.get('cli_pass')
        log=loginfo(user_email=C_e,user_pass=ps)
        log.save()
    
    return render(request,"index.html")
    
def datapage(request): 
    first=Bookinfo.objects.all()
    second=continfo.objects.all()
    third=loginfo.objects.all()
    return render(request,"Data.html",{"data":first},{"data":second},{"data":third})

