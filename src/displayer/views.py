from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .utils import xsd_data

from django.views.generic import TemplateView
from django.views import View


class Tools(View):

	def get(self, request):

		xsd_data()

		html = """

		<html><body>

		hey 

		</body></html>

		"""

		return HttpResponse(html)