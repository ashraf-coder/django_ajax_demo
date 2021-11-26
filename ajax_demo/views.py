from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from ajax_demo.models import Post


def home(request):
    context = {
        "products_count": Post.objects.count(),
    }
    return render(request, "ajax_demo/home.html", context)


def create_product(request):
    return render(request, "ajax_demo/create_product.html")


def ajax_add_product(request):
    posted_by = request.POST['posted_by']
    caption = request.POST['caption']
    post = Post.objects.create(posted_by=posted_by, caption=caption)
    post.save()

    new_products_count = Post.objects.count()

    data = {
        'success_message': "products added successfully",
        'new_products_count': new_products_count,
    }
    return JsonResponse(data=data, safe=False)
