from django.shortcuts import render

def shop(request):
    return render(request, 'shop/shop.html', {})
def inoske(request):
    return render(request, 'shop/inoske.html', {})
def zenitsu(request):
    return render(request, 'shop/zenitsu.html', {})
def rengoku(request):
    return render(request, 'shop/rengoku.html', {})
def muichiro(request):
    return render(request, 'shop/muichiro.html', {})
def shinobu(request):
    return render(request, 'shop/shinobu.html', {})
def expl(request):
    return render(request, 'shop/expl.html', {})
def shipping(request):
    return render(request, 'shop/shipping.html', {})
def refund(request):
    return render(request, 'shop/refund.html', {})
def privacy(request):
    return render(request, 'shop/privacy.html', {})
