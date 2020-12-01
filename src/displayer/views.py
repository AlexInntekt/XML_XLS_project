from lxml import etree

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data, detail_view_querry, extract_categories
from acquisitioner.utils import process
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render



class Tools(View):

	def get(self, request, **kwargs):

		if 'category' in kwargs:
			category = kwargs['category']
			data_to_display = xsd_data(category)
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

		return render(request, 'display.html', {'data':data_to_display})