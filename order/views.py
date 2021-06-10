from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from order.forms import ItemInCartForm, OrderForm
from staff.models import *


def index(request):
    return HttpResponse("Order Page")


@login_required(login_url='/login')  # Check login
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    item = Item.objects.get(pk=id)



    cart = Cart.objects.get(user=current_user)
    checkinvariant = ItemInCart.objects.filter(cart=cart,
                                               item=item)  # Check product in shopcart
    if checkinvariant:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ItemInCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = ItemInCart.objects.get(item_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else:  # Inser to Shopcart
                data = ItemInCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            cart = Cart.objects.get(user_id=current_user.id)
            data = ItemInCart.objects.get(item_id=id, cart=cart)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            cart = Cart.objects.get(user_id=current_user.id)
            data = ItemInCart(cart=cart)  # model ile bağlantı kur
            data.user_id = current_user.id
            data.item_id = id
            data.quantity = 1
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


def view_cart(request):
    current_user = request.user  # Access User Session information
    cart = Cart.objects.get(user_id=current_user)
    shopcart = ItemInCart.objects.filter(cart=cart, order=None)
    total = 0
    for rs in shopcart:
        total += rs.item.price * rs.quantity
    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'shopcart_products.html', context)


@login_required(login_url='/login')  # Check login
def delete_item(request, id):
    ItemInCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/shopcart")


def order_item(request):
    current_user = request.user
    cart = Cart.objects.get(user_id=current_user.id)
    shopcart = ItemInCart.objects.filter(cart=cart, order=None)
    total = 0
    for rs in shopcart:
        total += rs.item.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        # return HttpResponse(request.POST.items())
        # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
        # ..............
        payment = Payment(amount=total, additionalFee=0)
        payment.save()
        order = Order(saleOff=0, payment=payment, customer=current_user, status_id=1)
        order.save()  #

        # TODO : Remove from ProductInStock
        messages.success(request, "Your Order has been completed. Thank you ")
        return render(request, 'order_completed.html', {'ordercode': order.id})

    context = {'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'order_Form.html', context)
