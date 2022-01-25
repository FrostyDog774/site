from django.shortcuts import render

def post_list(request):
    return render(request, 'aboutme/aboutme.html', {})
def shipping(request):
    return render(request, 'aboutme/shipping.html', {})
def refund(request):
    return render(request, 'aboutme/refund.html', {})
def privacy(request):
    return render(request, 'aboutme/privacy.html', {})
