from django.shortcuts import render

def orders(request):
    return render(request, 'orders/orders.html', {})
def shipping(request):
    return render(request, 'orders/shipping.html', {})
def refund(request):
    return render(request, 'orders/refund.html', {})
def privacy(request):
    return render(request, 'orders/privacy.html', {})
