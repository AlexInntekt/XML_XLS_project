import datetime

from lxml import etree
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data, detail_view_querry, xsd_data_last_days, extract_categories
from acquisitioner.utils import process
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.conf import settings



class Tools(View):

	def get(self, request, **kwargs):

		if 'category' in kwargs:
			category = kwargs['category']
			data_to_display = xsd_data(category)
		elif 'last_days' in kwargs:
			last_days = kwargs['last_days']
			data_to_display = xsd_data_last_days(last_days)
		else:
			data_to_display = xsd_data(None)

		categories = extract_categories()

		return render(request, 'display.html', {'data':data_to_display, 'categories':categories})


class Refresher(View):

	def get(self, request):

		process()

		return HttpResponse("Refreshed!")


class DetailView(View):

	def get(self, request, **kwargs):

		temp_id = kwargs['id']

		data_to_display = detail_view_querry(temp_id)

		return render(request, 'detail_display.html', {'data':data_to_display})


class AddTool(View):

	def get(self, request, **kwargs):

		return render(request, 'add_tool.html', {"msg":""})


	def post(self, request, **kwargs):

		data = request.POST
		msg="I received your data"
		msg=data

		category = data["category"]
		name = data["name"]
		url = data["url"]
		web_based = data["web_based"]
		type_n = data["type"]
		free = data["free"]
		description = data["description"]
		logo = data["logo"]


		et = ET.parse(settings.MEDIA_ROOT+'/data/f2.xml')
		root = et.getroot()

		# for tool in root.findall('tool'):
		# 	print(tool.find('name').text)

		node = ET.SubElement(root, 'tool')
		node.set('temp_id',"USER_ADDED")

		cat_n = ET.SubElement(node, 'category')
		cat_n.text = category

		name_n = ET.SubElement(node, 'name')
		name_n.text = name

		url_n = ET.SubElement(node, 'url')
		url_n.text = url

		web_based_n = ET.SubElement(node, 'web_based')
		web_based_n.text = web_based

		type_n = ET.SubElement(node, 'type')
		type_n.text = type_n

		free_n = ET.SubElement(node, 'free')
		free_n.text = free

		description_n = ET.SubElement(node, 'description')
		description_n.text = description

		added_on = ET.SubElement(node, 'added_on')
		now = datetime.datetime.now().strftime("%Y-%m-%d")
		added_on.text = now

		logo_n = ET.SubElement(node, 'image_logo')
		logo_n.text = logo

		with open(settings.MEDIA_ROOT+'/data/added_by_client.xml', 'w') as f:
			data_as_str = ET.tostring(root).decode('utf-8')
			f.write(data_as_str)

		return render(request, 'add_tool.html', {"msg":msg})