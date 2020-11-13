from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customerdata
from .models.order import Order
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator
from .middlewares.auth import auth_middleware
# Create your views here.





def index(request):

    if request.method=="POST":
        cartvlu=request.POST.get('cart_id')
        decress=request.POST.get('decres')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(cartvlu)
            if quantity:
                if decress:
                    if quantity<=1:
                        cart.pop(cartvlu)
                    else:
                        cart[cartvlu]=quantity-1
                else:
                    cart[cartvlu]=quantity+1
            else:
                cart[cartvlu]=1

        else:
            cart={}
            cart[cartvlu]=1

        request.session['cart'] = cart
        print('cart', request.session['cart'])

    else:
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}

    prods=None
    prodcat=Category.get_all_category()

    categoryid=request.GET.get('category')
    if categoryid:
        prods=Product.get_all_product_by_categoryID(categoryid)
    else:
        prods=Product.get_all_product()



    params={'prod':prods, 'prodcats': prodcat}
    print('email', request.session.get('email'))
    return render(request, 'index.html', params)



def singup(request):

    if request.method=="GET":
        return render(request, 'singup.html')

    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password=make_password(password1)

        value={
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email

        }

        error_message=""
        if not first_name:
            error_message="you have to enter first name"

        elif len(first_name)<4:
            error_message="at least 4 number"

        elif not last_name:
            error_message="you have to enter last name"
        elif not phone:
            error_message="you have to enter a valid phn number"

        elif not email:
            error_message="you have to enter email"
        elif not password:
            error_message="you have to enter password"

        if not error_message:
            customer=Customerdata(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=password
            )
            customer.save()
            return redirect('index')

        else:
            d1={'error': error_message , 'values': value }
            return render(request, 'singup.html' , d1)


def login(request):
    if request.method=="GET":
        return render(request, 'login.html')

    else:
        cus_email=request.POST.get('email')
        cus_password=request.POST.get('password')
        custo=Customerdata.get_customer_email(cus_email)
        error_message=""
        if custo:
            ddd=check_password(cus_password, custo.password)
            if ddd:
                request.session['customer_id'] = custo.id
                request.session['email'] = custo.email
                return redirect('index')
            else:
                error_message="you have enter a wrong password"


        else:
            error_message="you have entered a wrong email or password"

        d1={'error': error_message}
        return render(request, 'login.html', d1)



def logout(request):
    request.session.clear()
    return redirect('login')



def cart(request):

    cartid=list(request.session.get('cart').keys())
    cartproduct=Product.get_all_product_id(cartid)

    print(cartproduct)
    d3={'cartproducts': cartproduct}
    return render(request, 'cart.html', d3)






def checkout(request):
    if request.session.get('customer_id'):

        if request.method=="POST":
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            customer=request.session.get('customer_id')
            cart=request.session.get('cart')
            products=Product.get_all_product_id(list(cart.keys()))
            print(address, phone, customer, cart, products)

            for product in products:
                # print(Customerdata(id=customer))

                customer_order=Order(
                    product=product,
                    customer=customer,
                    #akhane amra cart ar id thaika cart ar quantity ta ver kortasi.. product ar id akta intijer valu but cart ar id akta str valu..tai product ar id k str korte hobe..
                    quantity=cart.get(str(product.id)),
                    address=address,
                    phone=phone,
                    price=product.price,
                    name=product.name

                )
                customer_order.save()

            request.session['cart']={}


            return redirect('cart')

    else:
        return redirect('login')

def order(request):

    if request.method=="GET":
        customer_id=request.session.get('customer_id')
        allproduct=Order.get_product_by_customer_id(customer_id)
        dddddd={'allproddss': allproduct}
        return render(request, 'order.html', dddddd)