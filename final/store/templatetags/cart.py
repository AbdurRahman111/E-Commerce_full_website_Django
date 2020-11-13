from django import template

register=template.Library()

@register.filter(name="in_cart")
def in_cart(i, cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==i.id:
            return True

    return False

@register.filter(name="quantity")
def quantity(i, cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==i.id:
            return cart.get(id)

    return 0

@register.filter(name="sub_total_price")
def sub_total_price(i, cart):
    return quantity(i, cart)*i.price

@register.filter(name="total_price")
def total_price(cartproducts, cart):
    sum=0
    for j in cartproducts:
        sum += sub_total_price(j, cart)

    return sum

@register.filter(name="currency")
def currency(number):
    return "Tk " + str(number)







