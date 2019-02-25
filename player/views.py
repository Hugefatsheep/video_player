from django.shortcuts import render
from .models import Order, Name


# Create your views here.
def index(request):
    """主页"""
    orders = Order.objects.order_by('date_added')
    names = Name.objects.order_by('date_added')
    context = zip(orders, names)
    return render(request, 'player/index.html', {'context': context})
