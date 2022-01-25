from django.shortcuts import render
from .models import Post

def post_list(request):
    data = Post.objects.all().order_by('-id')
    return render(request, 'hush/hush.html', {'data': data})
def shipping(request):
    return render(request, 'hushshipping.html', {})
def refund(request):
    return render(request, 'hush/refund.html', {})
def privacy(request):
    return render(request, 'hush/privacy.html', {})
