from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import Myorder, Customusercreation,Customerlogin
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Product,Orderitem
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

import json
def dash(request):
    
    
    all=Product.objects.all()
    products={}
    for a in all:
        if a.category not in products:
            products[a.category]=[]
            products[a.category].append(a)
        else:
            products[a.category].append(a)

    
            

    return render(request, "shop/home.html", {"all":products})

def category(request, pk=None):
    
    a=Product.objects.values('category')
    cat=[]
   
    for c in a:
        pcat=c['category']
        if pcat not in cat:
            cat.append(pcat)
    allprod=Product.objects.all()
   
    category="All Products"
    if pk is not None:
        mycat=Product.objects.filter(category=pk)
        allprod=mycat
        category=pk
    paginator = Paginator(allprod, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    print(posts)
        
        


   
    
    return render(request, "shop/cat.html", {"allcat":cat, "allprod":posts, 'category':category})

def cart(request):
    cookie=request.session
    
    if "mycart" not in cookie:
        return render(request, "shop/cart.html", {"allprod":False})
    else:
        amount=0
        mycart={}
        
        for key,value in cookie["mycart"].items():
            
            prod=Product.objects.get(id=int(key))
            mycart[prod]=value
            
            amount=amount+(value[0]*value[1])

       
        return render(request, "shop/cart.html", {"allprod":mycart, "amount":amount})

def prodview(request, pk, cat):
    desc=Product.objects.get(id=pk)
   
    similar=Product.objects.filter(category=cat).exclude(p_name=desc.p_name)
    if len(similar)>=1:
        s=similar
    else:
        print("no available")
        s=False
  
    return render(request, "shop/view.html", {"product":desc, "similar":s})

def book(request):
    if request.user.is_authenticated:
        fm=Myorder()
        cookie=request.session["mycart"].items()
        amount=0
    
        for key,value in cookie:
            amount=amount+(value[0]*value[1])
        if request.method=="POST":
            data=Order(user=request.user)
            fm=Myorder(data=request.POST, instance=data)
            if fm.is_valid():
               
                
               
                f=fm.save()
                idorder=Order.objects.get(id=f.id)
                for key,value in request.session["mycart"].items():
                    product=Product.objects.get(id=int(key))
                    
                    oi=Orderitem(order=idorder, product=product, price=value[1], quantity=value[0])
                    oi.save()
               

                

                del request.session["mycart"]
                messages.success(request, f"Your Order has been successfully submitted.Your Order id is {f.id}")
                return redirect('/')
        return render(request, "shop/buyorder.html", {"form":fm, "amount":amount})
    else:
        return redirect("/loginuser")

def signup(request):
    fm = Customusercreation()
    if request.method == "POST":
        fm = Customusercreation(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your have successfully created your account.Now you can login.")
            return redirect("/")
    return render(request, "shop/signup.html", {"form": fm})

def handlelogin(request):
    fm = Customerlogin()
    if request.method == "POST":
        fm = Customerlogin(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            psk = fm.cleaned_data["password"]
            
            user = authenticate(username=uname, password=psk)
            if user is not None:
                login(request, user)
                
                messages.success(request, "Your have been successfully login.")
                print(request.user)
    
                return redirect("/")
    
    return render(request, "shop/login.html", {"form": fm})


def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request, "Your have successfully logout.")
        return redirect('/')
@csrf_exempt
def additem(request):
    if request.method=="POST":
       

        data=json.loads(request.body)
     
        id=data["p_id"]
        action=data["action"]
       
        
        if "mycart" not in request.session:
            request.session["mycart"]={}
            request.session.set_expiry(86400)

        
        
        if str(id) not in request.session["mycart"]:
            
            object=Product.objects.get(id=id)
            
            request.session["mycart"][str(id)]= [1, object.price]
        
            
        else:
            if action == "sub":
                
                a=request.session["mycart"][str(id)]
                z=[a[0]-1, a[1]]
                request.session["mycart"][str(id)]=z
            
               
                
                
            if action == "add":
                
                a=request.session["mycart"][str(id)]
                
                z=[a[0]+1, a[1]]
                request.session["mycart"][str(id)]=z
            
            
                
            
            
        request.session.modified=True
        senddata=request.session["mycart"].items()
       
        mydata=json.dumps(list(senddata,))
        
        return JsonResponse( mydata , safe=False)
    else:
        if "mycart" in request.session:
            cookie=request.session["mycart"].values()
           
            a=[]
            for i in cookie:
               
                a.append(i[0])

            total=sum(a)
            
            return JsonResponse(total, safe=False)
        return JsonResponse("0", safe=False)
    
def managecookie(request, pk):
   
    if pk == "clearall":
        del request.session["mycart"]
        
        
    else:
        
        del request.session["mycart"][pk]
        request.session.modified=True
       
    return redirect("/cart")

def search(request):
    if request.method=="POST":
        query=request.POST.get('searchtext')
        
        prod=Product.objects.all()
        searchlist={}
        for item in prod:
            if (query.lower() in (item.category).lower() or query.lower() in (item.desc).lower() or query.lower()     in (item.p_name).lower()):
                if item.category not in searchlist:
                    searchlist[item.category]=[]
                    searchlist[item.category].append(item)
                else:
                    searchlist[item.category].append(item)

       
        return render(request, "shop/home.html", {"all":searchlist})
        



        # return JsonResponse(serializers.serialize("json", ), safe=False)
# Create your views here.
