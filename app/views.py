from django.shortcuts import render
from django.views import View
from app.models import Brand,Product
import datetime
import time
# Create your views here.

class Index(View):
    def get(self, request ):

        #getting brand
        Brands = Brand.objects.all()
        return render(request, 'index.html', {"Brands": Brands})



class Prod(View):
    def get(self,request):
        Brand1 = Product.objects.all()
        Brand_ID=request.GET.get('Brand')
        if Brand_ID:
            Products= Product.get_all_products_by_Brandid(Brand_ID)
        else:
            Products=Product.objects.all()
        return render(request,"products.html",{"Products":Products})
    def date_productpage(self,request):
        Brands = Brand.objects.all()

        return render(request, "products.html", {"Brands": Brands})


class Prod(View):
    def get(self,request):
        Products=Product.objects.all()

        return render(request,"products.html",{"Products":Products})

def brand_product_list(request,brand_id):
    brand = Brand.objects.get(id=brand_id)
    Products = Product.objects.filter(Product_Brand=brand)
    return render(request,'products.html',
                  {'Products':Products,
                   }
                  )
def stock_date(request):

    dt = datetime.datetime.today()
    day = dt.day
    # print("Day is :",day)
    # expire =

    # stock_date_available = Brand.objects.all()
    stock_date_available = Brand.objects.all().first()
    leftdays = stock_date_available.remaining_days
    print("stock_date_available is: ",stock_date_available)
    till_date = day + stock_date_available
    # print("Till Date is: ",till_date)
    if day != till_date and day < till_date:

        print("Product is Available")
    else:
        print("Sorry Out of Stock")

    return render(request, 'index.html',{'stock_date_available': stock_date_available,
                                         'leftdays':leftdays})


def timer(requset):
    date = Brand.objects.all()
    last_date = date.day_left
    # counter = 1
    # print(counter)
    print(last_date)
    while True:

        time.sleep(5)
    # counter += 1
    # print(counter)
        last_date=-1
        print(last_date)
    #this adds one to the counter every 60 seconds
    return render(request,"index.html",{"date":date})