from django.shortcuts import render

def news(request):
    return render(request, 'news/news.html', {})
def shipping(request):
    return render(request, 'news/shipping.html', {})
def refund(request):
    return render(request, 'news/refund.html', {})
def privacy(request):
    return render(request, 'news/privacy.html', {})
