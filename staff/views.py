from django.shortcuts import render, redirect

from .models import StorageStaff, Fullname, Product


# Create your views here.
def list_staff(request):
    staffs = StorageStaff.objects.all()
    return render(request, 'staffs.html', {'staffs': staffs})


# def search_products(request, **kwargs):
#     if request.method != 'POST':
#         product = Product.objects.all()
#         return render(request, 'products.html', {'products': product})
#     else:
#         products = Product.objects.filter(**kwargs)
#         return render(request, 'products.html', {'products': products})


def get_products(request):
    if request.method != 'POST':
        product = Product.objects.all()
        return render(request, 'products.html', {'products': product})
    else:
        products = Product.objects.filter(name__icontains=request.POST['product_search'])
        return render(request, 'products.html', {'products': products})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('search_products')
