from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Product
# Create your views here.


def index(request):
    latest_product_list = Product.objects.order_by('-product_date')[:5]
    return render(request, 'store/index.html', {'latest_product_list': latest_product_list})


def add_product(request):
    new_product = Product(product_name=request.POST['prod_name'], product_description=request.POST['prod_text'], product_date=timezone.now())
    new_product.save()
    return HttpResponseRedirect(reverse('store:adding'), {'new_product': new_product})


def test(request):
    return render(request, 'store/test.html')


def premium(request):
    return render(request, 'store/premium.html')
    

def adding(request):
    return render(request, 'store/adding.html')


def detail(request, product_id):
    try:
        a = Product.objects.get(id=product_id)
    except:
        raise Http404('Product Not Found')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'store/detail.html', {'product': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, product_id):
    try:
        a = Product.objects.get(id=product_id)
    except:
        raise Http404('Product Not Found')

    a.comment_set.create(auth_name=request.POST['name'], comm_text=request.POST['text'])

    return HttpResponseRedirect(reverse('store:detail', args= (a.id,)))