from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data

from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render


class Tools(View):

	def get(self, request):

		data_to_display = xsd_data()

		return render(request, 'display.html', {'data':data_to_display})