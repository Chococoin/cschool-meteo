import requests
import xml.etree.ElementTree as ET
import sys
import math

r = requests.get('http://www.lamma.rete.toscana.it/previ/ita/xml/lista_comuni.xml')

context = r.content

#content is a str
context2 = context.decode("UTF-8")

#print(context2)

xml_data = ET.fromstring(context2)

#print(xml_data)

cities = xml_data.findall("link")

city_list = list()

for i in cities:
	city_list.append(i.find("title").text)

city_list = sorted(city_list)

city_list_by_col = list()

#print(city_list)

def list_columns(obj, cols=4, columnwise=True, gap=4):
    """
    Print the given list in evenly-spaced columns.

    Parameters
    ----------
    obj : list
        The list to be printed.
    cols : int
        The number of columns in which the list should be printed.
    columnwise : bool, default=True
        If True, the items in the list will be printed column-wise.
        If False the items in the list will be printed row-wise.
    gap : int
        The number of spaces that should separate the longest column
        item/s from the next column. This is the effective spacing
        between columns based on the maximum len() of the list items.
    """
    global city_list_by_col

    sobj = obj
    if cols > len(sobj): 
    	cols = len(sobj)
    max_len = max([len(item) for item in sobj])
    if columnwise: 
    	cols = int(math.ceil(float(len(sobj)) / float(cols)))
    plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
    if columnwise:
        if not len(plist[-1]) == cols:
            plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
        plist = zip(*plist)
    printer = '\n'.join([''.join([c.ljust(max_len + gap) for c in p]) for p in plist])
    city_list_by_col = printer

list_columns(city_list, cols=6)

print(("_"*60)+"Lista città"+("_"*60))
print(city_list_by_col)