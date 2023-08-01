import random
from django.utils.text import slugify
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from home.models import *
from django.db.models import Prefetch

# Create your views here.
def admin_home(request):
    return render(request, 'incs/nav.html')

def admin_categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'categories/categories.html', context)

def create_category(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        name = request.POST["name"]
        random_number = random.randint(100, 9999)
        slug = slugify(name + str(random_number))
        categories = Category(image=image, name=name,slug=slug)
        categories.save()
        return redirect('cadmincategories')
    return render(request,'categories/create_categories.html')

def update_category(request, cat_slug):
    categories = Category.objects.get(slug=cat_slug)
    context={'categories':categories}
    if request.method == "POST":
        image = request.FILES.get("images")
        name = request.POST["name"]
        if not image:
            categories.image=categories.image
        else:   
            categories.image=image
        categories.name=name
        categories.save()
        return redirect('cadmincategories')
    return render(request, 'categories/update_categories.html', context)

def delete_category(request, cat_slug):
    if request.method == 'POST':
        categories = Category.objects.get(slug=cat_slug)
        categories.delete()
        return redirect('cadmincategories')
    return render(request,'categories/categories.html')
    
def admin_products(request):
    products = Product.objects.all().order_by('name')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj}
    # images = ProductImage.objects.filter(product=products).first()
    # context = {'products':products}
    return render (request, 'products/products.html', context)


def create_product(request):
    categories= Category.objects.all()
    context={'categories':categories}
    print(categories)
    if request.method == "POST":
        categoryname = request.POST.get('category','')
        productname = request.POST['productname']
        productdescription = request.POST['productdescription']
        productprice = request.POST['productprice']
        productquantity = request.POST['productquantity']
        productbrand = request.POST['productbrand']
        productimages = request.FILES.getlist('images')
        # product_description = bleach.clean(productdescription, tags=[], strip=True)
        # generate slug
        random_number = random.randint(100, 9999)
        slug = slugify(productname + str(random_number))
        if categoryname and productname and productdescription and productprice and productquantity and productbrand:
            category = Category.objects.get(name=categoryname)
            product= Product(category=category, name=productname, slug=slug, description=productdescription, price=productprice, quantity=productquantity,brand=productbrand)
            product.save()
            for image in productimages:
                product_image=ProductImage(product=product, image=image)
                product_image.save()
            return redirect('cadminproducts')
    return render(request, 'products/create_products.html', context)


def view_product(request,prod_slug):
    products=Product.objects.get(slug=prod_slug)
    productimages = ProductImage.objects.filter(product=products)
    context={'products':products,'productimages':productimages}
    return render(request,'customadmin/view/productview.html',context)

def update_product(request,prod_slug):
    products=Product.objects.get(slug=prod_slug)
    categories = Category.objects.exclude(name=products.category.name)
    product_images= ProductImage.objects.filter(product=products)
    context={'products':products, 'categories':categories,'product_images':product_images}
    if request.method == "POST":
        categoryname = request.POST.get('category','')
        productname = request.POST['productname']
        productdescription = request.POST['productdescription']
        productprice = request.POST['productprice']
        productquantity = request.POST['productquantity']
        productbrand = request.POST['productbrand']
        productimages = request.FILES.getlist('images')
        # product_description = bleach.clean(productdescription, tags=[], strip=True)

        if categoryname:
            category=Category.objects.get(name=categoryname)
            if category:
                products.category=category

        else:
            products.category=products.category

        if productname:
            products.name=productname

        else:
            products.name=products.name

        if productdescription:
            products.description=productdescription

        else:
            products.description=products.description

        if productprice:
            products.price=productprice

        else:
            products.price=products.price

        if productquantity:
            products.quantity=productquantity

        else:
            products.quantity=products.quantity

        if productbrand:
            products.brand=productbrand

        else:
            products.brand=products.brand
        products.save()

        if productimages:
            product_images.delete()
            for image in productimages:
                product_image=ProductImage(product=products, image=image)
                product_image.save()
        else:
            for product_image in product_images:
                product_image.image = product_image.image
                product_image.save()
        return redirect('cadminproducts')

    return render(request, 'products/update_products.html', context)

def delete_product(request, prod_slug):
    if request.method == 'POST':
        products = Product.objects.get(slug=prod_slug)
        products.delete()
        return redirect('cadminproducts')
    return render(request,'products/products.html')

