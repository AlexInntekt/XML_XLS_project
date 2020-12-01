import lxml.etree as etree

from django.conf import settings


def xsd_data():
	xml  = settings.MEDIA_ROOT+'/data/f2.xml'
	xsl = settings.STATIC_ROOT+'/tohtml.xsl'
	# with open(settings.MEDIA_ROOT+'/data/f2.xml', 'r') as f:
	# 	xml_data = f.read()

	dom = etree.parse(xml)
	xslt = etree.parse(xsl)
	transform = etree.XSLT(xslt)
	newdom = transform(dom)


	return newdom



def detail_view_querry(temp_id):

	xml  = settings.MEDIA_ROOT+'/data/f2.xml'
	xpath_querry = "/tools/tool[@temp_id='{}']".format(temp_id)
	tree = etree.parse(xml)
	node = tree.xpath(xpath_querry)[0]
	res = etree.tostring(node).decode('utf-8')

	return res
