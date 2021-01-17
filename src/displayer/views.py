import datetime
import os
import subprocess

from lxml import etree
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data, detail_view_querry, xsd_data_last_days, extract_categories, get_rfd_data
from acquisitioner.utils import process
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.conf import settings



class RFDView(View):
	def get(self, request, **kwargs):

		data_to_display = []
		data = get_rfd_data()

		categories = extract_categories()

		return render(request, 'display.html', {'data':data_to_display, 'categories':categories})

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
		categories = extract_categories()

		return render(request, 'detail_display.html', {'data':data_to_display, 'categories':categories})


class AddTool(View):

	def get(self, request, **kwargs):

		categories = extract_categories()
		
		return render(request, 'add_tool.html', {"msg":"", 'categories':categories})


	def post(self, request, **kwargs):

		data = request.POST
		msg="I received your data"
		msg=data

		category = data["category"]
		name = data["name"]
		url = data["url"]
		web_based = data["web_based"]
		type_t = data["type"]
		free = data["free"]
		description = data["description"]
		logo = data["logo"]

		et = ET.parse(settings.MEDIA_ROOT+'/data/f2.xml')
		root = et.getroot()

		node = ET.SubElement(root, 'tool')
		max_id=0
		for tool in root:
			try:
				tmpid = int(tool.attrib["temp_id"])+1
				if max_id < tmpid:
					max_id = tmpid
			except KeyError as e:
				pass

		node.set('temp_id',str(max_id))

		cat_n = ET.SubElement(node, 'category')
		cat_n.text = category

		name_n = ET.SubElement(node, 'name')
		name_n.text = name

		url_n = ET.SubElement(node, 'url')
		url_n.text = url

		web_based_n = ET.SubElement(node, 'web_based')
		web_based_n.text = web_based

		type_n = ET.SubElement(node, 'type')
		type_n.text = type_t

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

		root_path = os.path.dirname(settings.BASE_DIR)
		validation_command = "xmllint --noout --dtdvalid {}/static/data.dtd {}/media/data/added_by_client.xml".format(root_path, root_path)

		# output = os.popen(validation_command).read()
		# print("output: {}".format(output))

		# proc = subprocess.Popen([validation_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		# output, error = proc.communicate()
		output, error = subprocess.Popen(validation_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		output = output.decode('utf-8')
		error = error.decode('utf-8')

		valid_dtd = False
		if error=='':
			valid_dtd = True

		web_based_cond = web_based=='web_based' or web_based=='desktop' 
		type_cond = type_t=='learning' or type_t=='teaching'
		no_empty_field = category!='' and name!='' and url!='' and web_based!='' and type_t!='' and free!='' and logo!='' and description!=''
		all_validation_passed = valid_dtd and web_based_cond and type_cond and no_empty_field

		if not all_validation_passed:
			if not no_empty_field:
				msg = "Fields should not be empty!"
			elif not web_based_cond:
				msg = "The web based value should be whether 'web_based' or 'desktop'"
			elif not type_cond:
				msg = "The field 'type' should have as value 'learning' or 'teaching'"
			elif not valid_dtd:
				msg="The instance could not be added to the database because the DTD validation failed."
			else:
				msg="For some unknown reason the validation failed."
		
		else:
			msg="The instance was succesfully added in the XML database!"

			with open(settings.MEDIA_ROOT+'/data/f2.xml', 'w') as f:
				data_as_str = ET.tostring(root).decode('utf-8')
				f.write(data_as_str)
			
		
		categories = extract_categories()

		return render(request, 'add_tool.html', {"msg":msg, 'categories':categories})