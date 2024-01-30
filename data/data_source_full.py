from data_source_1 import data_1
from data_source_2 import data_2
from data_source_3 import data_3

def data_full():
    # From data source 1
    city_df = data_1()
    
    # From data source 2
    country_df = data_2()
    
    # From data source 3
    actor_df = data_3('actor')
    store_df = data_3('store')
    address_df = data_3('address')
    category_df = data_3('category')
    customer_df = data_3('customer')
    film_actor_df = data_3('film_actor')
    film_category_df = data_3('film_category')
    inventory_df = data_3('inventory')
    language_df = data_3('language')
    rental_df = data_3('rental')
    staff_df = data_3('staff')
    payment_df = data_3('payment')
    film_df = data_3('film')
    
    table_dict = {'actor': actor_df, 
              'store' : store_df, 
              'address' : address_df, 
              'category' :category_df, 
              'customer' : customer_df, 
              'film_actor' : film_actor_df, 
              'film_category' : film_category_df, 
              'inventory' : inventory_df, 
              'language' : language_df, 
              'rental' : rental_df, 
              'staff' : staff_df, 
              'payment' : payment_df, 
              'film' : film_df, 
              'city' : city_df, 
              'country' : country_df}
    
    return table_dict