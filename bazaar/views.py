from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db.models import Max

# importing models
from .models import Firm
from .models import Trader
from .models import Update


# Create your views here.


def index(request):
    return render(request,'bazaar/index.html')

def loginsignup(request):
    return render(request,'bazaar/loginsignup.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/bazaar/profile/")
        else:

            return render(request,"bazaar/loginsignup.html")

def logoutuser(request):
    logout(request)
    return redirect("/bazaar/")


def signup(request):
    print("inside")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=User.objects.create_user(username=username, password=password)
        user.save()
        trader = Trader(username=username, password=password)
        trader.save()
        login(request, user)
        return redirect("/bazaar/profile/")


def profile(request):
    if request.user.is_anonymous:
        return redirect("/bazaar/loginsignup/")

    firms = Firm.objects.all()
    params = {"firm": firms}
    return render(request,'bazaar/profile.html', params)

def buy(request):
    if request.user.is_anonymous:
        return redirect("/bazaar/loginsignup/")

    firms = Firm.objects.all()
    trader = Trader.objects.filter(username=request.user.username)
    inst = trader[0]


    if request.method == "POST":
        firm = request.POST['firm']
        nstocks = int(request.POST['nstocks'])

        if firm==firms[0].firm_name and (inst.mb - (nstocks*firms[0].firm_price))>=0:
            inst.f1 = inst.f1 + nstocks
            inst.mb = inst.mb - (nstocks*firms[0].firm_price)
            inst.mi = inst.mi + (nstocks*firms[0].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[1].firm_name and (inst.mb - (nstocks*firms[1].firm_price))>=0:
            inst.f2 = inst.f2 + nstocks
            inst.mb = inst.mb - (nstocks*firms[1].firm_price)
            inst.mi = inst.mi + (nstocks * firms[1].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[2].firm_name and (inst.mb - (nstocks*firms[2].firm_price))>=0:
            inst.f3 = inst.f3 + nstocks
            inst.mb = inst.mb - (nstocks*firms[2].firm_price)
            inst.mi = inst.mi + (nstocks * firms[2].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[3].firm_name and (inst.mb - (nstocks*firms[3].firm_price))>=0:
            inst.f4 = inst.f4 + nstocks
            inst.mb = inst.mb - (nstocks*firms[3].firm_price)
            inst.mi = inst.mi + (nstocks * firms[3].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[4].firm_name and (inst.mb - (nstocks*firms[4].firm_price))>=0:
            inst.f5 = inst.f5 + nstocks
            inst.mb = inst.mb - (nstocks*firms[4].firm_price)
            inst.mi = inst.mi + (nstocks * firms[4].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[5].firm_name and (inst.mb - (nstocks*firms[5].firm_price))>=0:
            inst.f6 = inst.f6 + nstocks
            inst.mb = inst.mb - (nstocks*firms[5].firm_price)
            inst.mi = inst.mi + (nstocks * firms[5].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[6].firm_name and (inst.mb - (nstocks*firms[6].firm_price))>=0:
            inst.f7 = inst.f7 + nstocks
            inst.mb = inst.mb - (nstocks*firms[6].firm_price)
            inst.mi = inst.mi + (nstocks * firms[6].firm_price)
            inst.mt = inst.mb + inst.mi



        elif firm == firms[7].firm_name and (inst.mb - (nstocks*firms[7].firm_price))>=0:
            inst.f8 = inst.f8 + nstocks
            inst.mb = inst.mb - (nstocks*firms[7].firm_price)
            inst.mi = inst.mi + (nstocks * firms[7].firm_price)
            inst.mt = inst.mb + inst.mi

        """
        elif firm == firms[8].firm_name:
            inst.f9 = inst.f9 + nstocks
            inst.mb = inst.mb - (nstocks*firms[8].firm_price)
            inst.mi = inst.mi + (nstocks * firms[8].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[9].firm_name:
            inst.f10 = inst.f10 + nstocks
            inst.mb = inst.mb - (nstocks*firms[9].firm_price)
            inst.mi = inst.mi + (nstocks * firms[9].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[10].firm_name:
            inst.f11 = inst.f11 + nstocks
            inst.mb = inst.mb - (nstocks*firms[10].firm_price)
            inst.mi = inst.mi + (nstocks * firms[10].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[11].firm_name:
            inst.f12 = inst.f12 + nstocks
            inst.mb = inst.mb - (nstocks*firms[11].firm_price)
            inst.mi = inst.mi + (nstocks * firms[11].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[12].firm_name:
            inst.f13 = inst.f13 + nstocks
            inst.mb = inst.mb - (nstocks*firms[12].firm_price)
            inst.mi = inst.mi + (nstocks * firms[12].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[13].firm_name:
            inst.f14 = inst.f14 + nstocks
            inst.mb = inst.mb - (nstocks*firms[13].firm_price)
            inst.mi = inst.mi + (nstocks * firms[13].firm_price)
            inst.mt = inst.mb + inst.mi

        elif firm == firms[14].firm_name:
            inst.f15 = inst.f15 + nstocks
            inst.mb = inst.mb - (nstocks*firms[14].firm_price)
            inst.mi = inst.mi + (nstocks * firms[14].firm_price)
            inst.mt = inst.mb + inst.mi
        """

        inst.save()
        

        return redirect("/bazaar/profile/")
    inst2=trader[0]
    firms2 = Firm.objects.all()
    inst2.mi=(inst2.f1*firms2[0].firm_price)+(inst2.f2*firms2[1].firm_price)+(inst2.f3*firms2[2].firm_price)+(inst2.f4*firms2[3].firm_price)+(inst2.f5*firms2[4].firm_price)+(inst2.f6*firms2[5].firm_price)+(inst2.f7*firms2[6].firm_price)+(inst2.f8*firms2[7].firm_price) #+(inst2.f9*firms2[8].firm_price)+(inst2.f10*firms2[9].firm_price)+(inst2.f11*firms2[10].firm_price)+(inst2.f12*firms2[11].firm_price)+(inst2.f13*firms2[12].firm_price)+(inst2.f14*firms2[13].firm_price)+(inst2.f15*firms2[14].firm_price)
    inst2.mt=inst2.mi + inst2.mb

    params = {"firm":firms}
    inst2.save()
    return render(request, 'bazaar/buy.html', params)


def sell(request):
    if request.user.is_anonymous:
        return redirect("/bazaar/loginsignup/")

    firms = Firm.objects.all()
    trader = Trader.objects.filter(username=request.user.username)
    inst = trader[0]

    if request.method == "POST":
        firm = request.POST['firm']
        nstocks = int(request.POST['nstocks'])

        if firm == firms[0].firm_name and ((inst.f1 - nstocks)>=0):
            inst.f1 = inst.f1 - nstocks
            inst.mb = inst.mb + (nstocks * firms[0].firm_price)
            inst.mi = inst.mi - (nstocks * firms[0].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[1].firm_name and ((inst.f2 - nstocks)>=0):
            inst.f2 = inst.f2 - nstocks
            inst.mb = inst.mb + (nstocks * firms[1].firm_price)
            inst.mi = inst.mi - (nstocks * firms[1].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[2].firm_name and ((inst.f3 - nstocks)>=0):
            inst.f3 = inst.f3 - nstocks
            inst.mb = inst.mb + (nstocks * firms[2].firm_price)
            inst.mi = inst.mi - (nstocks * firms[2].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[3].firm_name and ((inst.f4 - nstocks)>=0):
            inst.f4 = inst.f4 - nstocks
            inst.mb = inst.mb + (nstocks * firms[3].firm_price)
            inst.mi = inst.mi - (nstocks * firms[3].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[4].firm_name and ((inst.f5 - nstocks)>=0):
            inst.f5 = inst.f5 - nstocks
            inst.mb = inst.mb + (nstocks * firms[4].firm_price)
            inst.mi = inst.mi - (nstocks * firms[4].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[5].firm_name and ((inst.f6 - nstocks)>=0):
            inst.f6 = inst.f6 - nstocks
            inst.mb = inst.mb + (nstocks * firms[5].firm_price)
            inst.mi = inst.mi - (nstocks * firms[5].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[6].firm_name and ((inst.f7 - nstocks)>=0):
            inst.f7 = inst.f7 - nstocks
            inst.mb = inst.mb + (nstocks * firms[6].firm_price)
            inst.mi = inst.mi - (nstocks * firms[6].firm_price)
            inst.mt = inst.mb - inst.mi



        elif firm == firms[7].firm_name and ((inst.f8 - nstocks)>=0):
            inst.f8 = inst.f8 - nstocks
            inst.mb = inst.mb + (nstocks * firms[7].firm_price)
            inst.mi = inst.mi - (nstocks * firms[7].firm_price)
            inst.mt = inst.mb - inst.mi

        """
        elif firm == firms[8].firm_name:
            inst.f9 = inst.f9 - nstocks
            inst.mb = inst.mb + (nstocks * firms[8].firm_price)
            inst.mi = inst.mi - (nstocks * firms[8].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[9].firm_name:
            inst.f10 = inst.f10 - nstocks
            inst.mb = inst.mb + (nstocks * firms[9].firm_price)
            inst.mi = inst.mi - (nstocks * firms[9].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[10].firm_name:
            inst.f11 = inst.f11 - nstocks
            inst.mb = inst.mb + (nstocks * firms[10].firm_price)
            inst.mi = inst.mi - (nstocks * firms[10].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[11].firm_name:
            inst.f12 = inst.f12 - nstocks
            inst.mb = inst.mb + (nstocks * firms[11].firm_price)
            inst.mi = inst.mi - (nstocks * firms[11].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[12].firm_name:
            inst.f13 = inst.f13 - nstocks
            inst.mb = inst.mb + (nstocks * firms[12].firm_price)
            inst.mi = inst.mi - (nstocks * firms[12].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[13].firm_name:
            inst.f14 = inst.f14 - nstocks
            inst.mb = inst.mb + (nstocks * firms[13].firm_price)
            inst.mi = inst.mi - (nstocks * firms[13].firm_price)
            inst.mt = inst.mb - inst.mi

        elif firm == firms[14].firm_name:
            inst.f15 = inst.f15 - nstocks
            inst.mb = inst.mb + (nstocks * firms[14].firm_price)
            inst.mi = inst.mi - (nstocks * firms[14].firm_price)
            inst.mt = inst.mb - inst.mi
        """
        inst.save()
        


        return redirect("/bazaar/profile/")
    inst2 = trader[0]
    firms2 = Firm.objects.all()
    inst2.mi = (inst2.f1*firms2[0].firm_price)+(inst2.f2*firms2[1].firm_price)+(inst2.f3*firms2[2].firm_price)+(inst2.f4*firms2[3].firm_price)+(inst2.f5*firms2[4].firm_price)+(inst2.f6*firms2[5].firm_price)+(inst2.f7*firms2[6].firm_price)+(inst2.f8*firms2[7].firm_price) #+(inst2.f9*firms2[8].firm_price)+(inst2.f10*firms2[9].firm_price)+(inst2.f11*firms2[10].firm_price)+(inst2.f12*firms2[11].firm_price)+(inst2.f13*firms2[12].firm_price)+(inst2.f14*firms2[13].firm_price)+(inst2.f15*firms2[14].firm_price)
    inst2.mt = inst2.mi + inst2.mb

    params = {"firm": firms}
    inst2.save()
    return render(request,'bazaar/sell.html', params)


def news(request):
    if request.user.is_anonymous:
        return redirect("/bazaar/loginsignup/")

    return render(request,'bazaar/news.html')



def winner1(request):
    params = {}
    traders = Trader.objects.all().order_by('-mt')
    print(traders[0].username, traders[0].mt)
    params["name1"]= traders[0].username
    params["money1"] = traders[0].mt
    params["name2"] = traders[1].username
    params["money2"] = traders[1].mt
    params["name3"] = traders[2].username
    params["money3"] = traders[2].mt

    return render(request,'bazaar/winner1.html',params)


def winner2(request):
    params = {}
    traders = Trader.objects.all().order_by('-mt')
    print(traders[0].username, traders[0].mt)
    params["name1"]= traders[0].username
    params["money1"] = traders[0].mt
    params["name2"] = traders[1].username
    params["money2"] = traders[1].mt
    params["name3"] = traders[2].username
    params["money3"] = traders[2].mt

    return render(request,'bazaar/winner2.html',params)


def winner3(request):
    params = {}
    traders = Trader.objects.all().order_by('-mt')
    print(traders[0].username, traders[0].mt)
    params["name1"]= traders[0].username
    params["money1"] = traders[0].mt
    params["name2"] = traders[1].username
    params["money2"] = traders[1].mt
    params["name3"] = traders[2].username
    params["money3"] = traders[2].mt

    return render(request,'bazaar/winner3.html',params)


def letsprofile(request):
    firms = Firm.objects.all()
    trader = Trader.objects.filter(username=request.user.username)[0]
    trader.mi = trader.f1*firms[0].firm_price + trader.f2*firms[1].firm_price + trader.f3*firms[2].firm_price + trader.f4*firms[3].firm_price + trader.f5*firms[4].firm_price + trader.f6*firms[5].firm_price + trader.f7*firms[6].firm_price + trader.f8*firms[7].firm_price #+ trader.f9*firms[8].firm_price + trader.f10*firms[9].firm_price + trader.f11*firms[10].firm_price + trader.f12*firms[11].firm_price + trader.f13*firms[12].firm_price + trader.f14*firms[13].firm_price + trader.f15*firms[14].firm_price
    trader.mt = trader.mb + trader.mi
    trader.save()
    return JsonResponse([trader.f1, trader.f2, trader.f3, trader.f4, trader.f5, trader.f6, trader.f7, trader.f8 , trader.mb, trader.mi],safe=False)


def letsbuy(request):
    firms = Firm.objects.all()
    fname=request.GET["firmName"]
    f = Firm.objects.get(firm_name=fname)
    return HttpResponse(f.firm_price)

def letssell(request):
    fname = request.GET["firmName"]
    f = Firm.objects.get(firm_name=fname)
    trader = Trader.objects.filter(username=request.user.username)[0]
    firms = Firm.objects.all()
    if firms[0].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f1], safe=False)

    if firms[1].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f2], safe=False)

    if firms[2].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f3], safe=False)

    if firms[3].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f4], safe=False)

    if firms[4].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f5], safe=False)

    if firms[5].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f6], safe=False)

    if firms[6].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f7], safe=False)

    if firms[7].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f8], safe=False)
    """
    if firms[8].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f9], safe=False)

    if firms[9].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f10], safe=False)

    if firms[10].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f11], safe=False)

    if firms[11].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f12], safe=False)

    if firms[12].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f13], safe=False)

    if firms[13].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f14], safe=False)

    if firms[14].firm_name==fname:

        return JsonResponse([f.firm_price, trader.f15], safe=False)

    """

def letsbuymb(request):
    trader = Trader.objects.filter(username=request.user.username)[0]
    return HttpResponse(trader.mb)

def letsupdatetime(request):
    update = Update.objects.all().last()
    return HttpResponse(str(update.update_time)[:5])

def letsupdatetext(request):
    update = Update.objects.all().last()
    return HttpResponse(update.news)
