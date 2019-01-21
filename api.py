import os, sys

ppath = "/path/to/directory/of/manage/script/"

#pass settings of project to Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChtStore.settings')
sys.path.append(ppath)
os.chdir(ppath)

#load product model from store app within project
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from store.models import Product

def update_item(product_title, price, count):
    p = Product(title=product_title, price=price, inventory_count=count)
    p.save()
    return
    

#returns the product title, price and current inventory_count in a dictionary
def fetch(product_title):
    try:
        p = Product.objects.get(title=product_title)
        return {'title': product_title,'price': p.price, 'inventory_count':p.inventory_count}
    except:
        print("No such product found, please search again")
    return {}

# return an array of all products, with each element being a dictionary
# containing product title, price and inventory_count.  If flag is a
# positive integer, only include those products with an inventory_count of
# at least 1
def fetch_all(flag):
    p_list = []

    products = Product.objects.all()

    for aprod in products:
        p = Product.objects.get(title=aprod)
        if flag:
            if aprod.inventory_count > 0:
                p_list.append({'title': aprod.title, 'price': p.price, "inventory_count": p.inventory_count})
        else:
            p_list.append({'title': aprod.title, 'price': p.price, "inventory_count": p.inventory_count})
    return p_list

# decrement inventory_count of a product and save changes to the database, only
# if there is at least one of an item
# returns 0 on success otherwise -1
def purchase(product_title):
    try:
        p = Product.objects.get(title=product_title)
        if p.inventory_count > 0:
            p.inventory_count -= 1
            p.save()
            return 1
        else:
            print("No inventory remaining")
    except:
        print("No products found, please search again")
    return -1
        
