from django.urls import path
from website import views as website_view
from my_app import views as test_my_app


urlpatterns = [
    # path('list_staff', list_staff, name='list_staff'),
    # path('create_staff', create_staff, name='create_staff'),
    # path('products', get_products, name='search_products'),
    # path('products', get_products, name='search_products_by_name'),
    # path('create_product', create_product, name='create_product'),
    # path('delete_product/<int:product_id>', delete_product, name='delete_product'),
    # path('update_product/<int:product_id>', update_product, name='update_product'),
    path('test', test_my_app.index, name='test'),
    path('get-product', test_my_app.getProduct, name='getProduct'),
    path('', website_view.home, name='home'),
    path('productDetail/<int:product_id>',website_view.detailProduct,name='productDetail'),
    path('add-to-cart/<int:id>',website_view.add_to_cart,name='add-to-cart'),
    path('shopping-cart',website_view.shoppingCart,name='shopping-cart'),
    path('check-out',website_view.order_item,name='check-out'),
    path('commnet/<int:id>',website_view.commnet,name="comment")
]