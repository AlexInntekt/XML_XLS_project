import lxml.etree as ET

from django.conf import settings


def xsd_data():
	xml  = settings.MEDIA_ROOT+'/data/f2.xml'
	xsl = settings.STATIC_ROOT+'/tohtml.xsl'
	# with open(settings.MEDIA_ROOT+'/data/f2.xml', 'r') as f:
	# 	xml_data = f.read()

	dom = ET.parse(xml)
	xslt = ET.parse(xsl)
	transform = ET.XSLT(xslt)
	newdom = transform(dom)


	return newdom



def detail_view_querry(temp_id):

	xml  = settings.MEDIA_ROOT+'/data/f2.xml'


	return xml
