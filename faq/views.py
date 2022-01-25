from django.shortcuts import render

def post_list(request):
    return render(request, 'faq/faq.html', {})
def shipping(request):
    return render(request, 'faq/shipping.html', {})
def refund(request):
    return render(request, 'faq/refund.html', {})
def privacy(request):
    return render(request, 'faq/privacy.html', {})
