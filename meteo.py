import requests
import xml.etree.ElementTree as ET
import sys

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

print(city_list)


