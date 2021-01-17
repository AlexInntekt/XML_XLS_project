import lxml.etree as etree
from xml.etree.ElementTree import fromstring, ElementTree, tostring
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import os
import sys

from django.conf import settings

# import jaydebeapi
from rdflib import Graph


def get_rfd_data():
    data = []
    dict_data = {}

    placement="http://www.toptools4learning.com/placement"
    category="http://www.toptools4learning.com/Category"

    g = Graph()
    g.parse("/home/alex/repos/ltools/media/data/rfd.rdf", format="xml")

    # print(len(g)) # prints 2

    import pprint
    for s, v, p in g:

        # print(s)
        # print(v)
        # print(p)
        # print()


        if(str(v)==str(placement)):

            name = s.split('\'')[0]

            obj = {}

            if name not in dict_data:
                dict_data[name] = {}

            obj['name'] = name
            obj['rank'] = int(p)

            dict_data[name] = obj
            # data.append(obj)


        if(str(v)==str(category)):

            name = s.split('\'')[0]

            if name not in dict_data:
                dict_data[name] = {}
                # print(name)

        #     dict_data[name]['category'] = str(p)

    
    for key, val in dict_data.items():
        data.append(val)
    data = sorted(data, key=lambda x: x['rank'], reverse=False)
    return data



def xsd_data(category):
    xml  = settings.MEDIA_ROOT+'/data/f2.xml'
    xsl = settings.STATIC_ROOT+'/tohtml.xsl'

    dom = etree.parse(xml)

    if category:
        category = category.replace("'","")
        xpath_querry = "/tools/tool[category='{}']".format(category)
        nodes = dom.xpath(xpath_querry)

        new_xml = ET.Element('tools')

        #combine all nodes fetched with xpath
        for node in nodes:
            n = etree.tostring(node).decode('utf-8')

            n = ET.fromstring(n)
            new_xml.append(n)

        new_xml=ET.tostring(new_xml)
        dom = etree.fromstring(new_xml)


    xslt = etree.parse(xsl)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)


    return newdom


def xsd_data_last_days(last_days):

    xsl = settings.STATIC_ROOT+'/tohtml.xsl'

    date = datetime.today() - timedelta(days=int(last_days))
    date = date.strftime("%Y-%m-%d")
    xpath_querry = "/tools/tool[added_on>'{}']".format(date)
    xidel_command = "xidel {} -e \"{}\" --output-format=xml".format(settings.MEDIA_ROOT+'/data/f2.xml', xpath_querry)
    output = os.popen(xidel_command).read()

    ParseError = ET.ParseError

    try:
        et = ElementTree(fromstring(output.encode('utf-8')))
        root=et.getroot()
        root.tag='tools'

        xml_string = tostring(root, encoding='utf8', method='xml').decode('utf-8')

        # print("break")
        # print(output)

        dom = etree.fromstring(xml_string.encode('utf-8'))

        xslt = etree.parse(xsl)
        transform = etree.XSLT(xslt)
        output = transform(dom)
    except ParseError as e:
        print("\n\n\n")
        print(e)
        return ""

    return output


# def xsd_detail_data(data):
#   xml  = settings.MEDIA_ROOT+'/data/f2.xml'
#   xsl = settings.STATIC_ROOT+'/detail_data.xsl'

#   dom = etree.parse(xml)

#   xslt = etree.parse(xsl)
#   transform = etree.XSLT(xslt)
#   newdom = transform(dom)


#   return newdom


def detail_view_querry(temp_id):

    xml  = settings.MEDIA_ROOT+'/data/f2.xml'
    xsl = settings.STATIC_ROOT+'/detail_data.xsl'

    xpath_querry = "/tools/tool[@temp_id='{}']".format(temp_id)
    tree = etree.parse(xml)
    node = tree.xpath(xpath_querry)[0]

    xslt = etree.parse(xsl)
    transform = etree.XSLT(xslt)
    node = transform(node)

    # node_as_string = tostring(node).decode('utf-8')

    return node




def extract_categories():
    et = ET.parse(settings.MEDIA_ROOT+'/data/f2.xml')
    tools = et.getroot()

    categories = []

    for tool in tools.findall('tool'):
        catg = tool.find('category').text

        categories.append(catg)

    categories = list(set(categories))

    categories.sort()

    return categories


