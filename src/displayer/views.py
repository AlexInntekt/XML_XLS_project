from lxml import etree

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data, detail_view_querry, xsd_data_last_days, extract_categories
from acquisitioner.utils import process
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render



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
		return render(request, 'add_tool.html', {"msg":msg})