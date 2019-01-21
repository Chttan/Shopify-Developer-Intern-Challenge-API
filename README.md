# Shopify-Developer-Intern-Challenge-API
The Summer 2019 Backend Developer Intern Challenge - Create an API for a basic online store

[The Summer 2019 Challenge](https://docs.google.com/document/d/1J49NAOIoWYOumaoQCKopPfudWI_jsQWVKlXmw1f1r-4/preview) 

## Environment/Setup
  Created using Python 3.6 and Django 2.1.5
  
  It is best to create a virtual environment so that you can isolate any libraries and packages you will need for this project from the rest of your system.  To do so, you will need to install **virtualenv**.
  
  Then, navigate to where you would like the virtual environment to be created and run:
  
      $ virtualenv ENV    
      
  This will create the environment.  To activate or "enter" the environment:
  
      $ source /path/to/ENV/bin/activate
  
  When you are done, to exit the environement:
  
      $ deactivate
  
  Once the environment has been activated, install the official release of Django. It is easiest to use pip:
  
      $ pip install Django
  
## How to import/include the API
   **api.py** will load the Product model and database from the store app within the ChtStore Django project.    
   **You must update ppath within api.py to point to the absolute path of the ChtStore Django project (where manage.py is)**.  
   To any python3 script which requires the api, simply add:
 
    import api
  
   (Make sure you use the relative path to **api.py** from your script)
  

## Using the API

  **update_item(product_title, price, count)**
  
   - Add a new item to the database or update an existing item
    
  **fetch(product_title)**
    
   - Returns a dictionary of format {title, price, inventory_count} of the desired product passed by title
   - If no such item exists, returns an empty dictionary
    
  **fetch_all(flag)**
    
   - Returns an array of dictionaries of format {title, price, inventory_count} for all products in the database if flag > 0
   - If flag is not a positive integer, products with an inventory_count < 1 will not be included
    
  **purchase(product_name)**
    
   - Will check if the desired product has an inventory of at least 1
   - If at least 1 of the desired product is available, the inventory_count is decremented by 1 and the database is updated
   - returns 1 if there was at least 1 inventory_count, returns -1 otherwise
   
   For some examples and test cases, see **test.py**.
 
## Approach 
For this project, I wanted to try learning and using a web framework.  As I was already familiar with Python, I chose to use Django.  

After creating my project, **ChtStore**, I moved on to creating an app, called **store**.  Django comes with the ability to use "object-relational mappers".  What this allows the developer to do is describe the layout of a database using Python code in a "model" (ours is found in **/store/models.py**).  After the mapper and database are created, the developer can now update and interact with the database using a simple Python API.  

With an a way to interact with the database created, the next step is to write our API for the basic online store.  Using the Django API, the **update_item**, **fetch**, **fetch_all** and **purchase** functions were created in a standalone script.  These functions follow the rules of the store such as the restrictions on purchasing products with no inventory.

This was not so simple, as there needs to be a way for the standalone script to access the **store** app, its model and its database.  After experimenting and searching, I found a way to load the model such that I could access the database and the Django Python API so that my own API could work.

With everything working, I created a simple test script, **test.py**, to debug and demonstrate my new API.  I tested some edge cases, mainly adding items that exist already, purchasing items that have no inventory and purchasing items that do not exist, to name a few. At the moment, there is nothing in the model that prevents negative prices or inventory counts.  This would not cause any exceptions but may make a few customers happy ;). In the future, I would like to explore the Django models in order to use those restrictions.

The next improvements I would like to make beyond the challenge suggestions are to add a frontend so that data can be visualised easier.  I would like to create a way for a customer to join a waiting list on items that have no inventory left.

Overall, this was a fun experience and I am looking forward to creating more projects in Django!

## References
The following were referenced to create this project:

  [How to install Django](https://docs.djangoproject.com/en/2.1/topics/install/)
  
  [virtualenv](https://virtualenv.pypa.io/en/latest/)
  
  [Django at a glance](https://docs.djangoproject.com/en/2.1/intro/overview/)
  
  [Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
  
  [Standalone Django scripts](https://www.stavros.io/posts/standalone-django-scripts-definitive-guide/)
