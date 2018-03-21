#TShirt

import types
import importlib

def make_shirt(size, msg):
    print('size o shirt is' , size, 'and message is', msg)

def city_country(city,country):
    print (city.title(), ',' , country.title())
    
def inp(**args):
    t = list(args.keys())[0]
    print (args.get(t, '6'))

    
