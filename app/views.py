from django.shortcuts import render
from django.views import View
from app.models import Brand, Product
import datetime
import time
# Create your views here.


class Index(View):
    def get(self, request):

        Brands = Brand.objects.all()
        return render(request, 'index.html', {"Brands": Brands})


def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    Products = Product.objects.filter(Product_Brand=brand)
    expiry_date = brand.expiry_date
    remaining_date = (datetime.datetime.now().date() - expiry_date.date()).days

    return render(request, 'products.html',
                  {'Products': Products,
                   "remaining_date": remaining_date})

def stock_date(request):

    dt = datetime.datetime.today()
    day = dt.day

    stock_date_available = Brand.objects.all().first()
    leftdays = stock_date_available.remaining_days
    print("stock_date_available is: ", stock_date_available)
    till_date = day + stock_date_available

    if day != till_date and day < till_date:

        print("Product is Available")
    else:
        print("Sorry Out of Stock")

    return render(request, 'index.html', {'stock_date_available': stock_date_available, 'leftdays': leftdays})
