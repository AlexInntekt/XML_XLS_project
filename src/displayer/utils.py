import lxml.etree as etree
import xml.etree.ElementTree as ET

from django.conf import settings


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



def detail_view_querry(temp_id):

	xml  = settings.MEDIA_ROOT+'/data/f2.xml'
	xsl = settings.STATIC_ROOT+'/detail_tohtml.xsl'

	xpath_querry = "/tools/tool[@temp_id='{}']".format(temp_id)
	tree = etree.parse(xml)
	node = tree.xpath(xpath_querry)[0]
	node_as_string = etree.tostring(node).decode('utf-8')
	# transform = etree.XSLT(xslt)
	# res = transform(node_as_string)
	print(node_as_string)
	return node_as_string
