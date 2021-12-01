import requests
import json
from dicttoxml import dicttoxml
from xml.dom import minidom
from json2html import *

def laneview(el):
    el = minidom.parseString(el)
    return el.toprettyxml(indent=" ")

url = "https://httpbin.org/anything"
response = requests.get(url)

if response.status_code ==200:
    headers = response.headers
    for header in headers:
        print(f'<{header}>{headers[header]}</{header}>')

    json = json.loads(response.content)

    print("0)xml\n1)html\n")

    if(int(input())):
        html = json2html.convert(json)
        print(laneview(html))
    else:
        xml = dicttoxml(json)
        print(laneview(xml))

