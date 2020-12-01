from django.conf import settings


def xsd_data():
	with open(settings.MEDIA_ROOT+'/data/f2.xml', 'r') as f:
		data = f.read()


	print(data)