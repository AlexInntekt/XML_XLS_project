import re
import requests
import os
import random
import datetime

import xml.etree.ElementTree as ET


from django.conf import settings









def check_if_directory_exists():
	#check if directory data exists, otherwise create it

	if not os.path.exists(settings.MEDIA_ROOT):
	    os.mkdir(settings.MEDIA_ROOT)

	if not os.path.exists(settings.MEDIA_ROOT+'/data'):
	    os.mkdir(settings.MEDIA_ROOT+'/data')

def download_webpage():
	#download raw data from website
	url='https://www.toptools4learning.com/'
	r = requests.get(url)
	open(settings.MEDIA_ROOT+'/data/raw_data.html', 'wb').write(r.content)


def extract_tabelar_data():
	#extract only what we need from the raw data html:
	with open(settings.MEDIA_ROOT+'/data/raw_data.html', 'r') as f:
	    data = f.read()

	reg = r'<tbody>(.|\n)*</tbody>'
	x = re.search(reg, data)
	ret = x.group(0)

	#convert the data to our desired format
	with open(settings.MEDIA_ROOT+'/data/f1.html', 'w') as f:
	    f.write(ret)


def process_data_to_new_format():
	skipping = 2
	i=0

	et = ET.parse(settings.MEDIA_ROOT+'/data/f1.html')
	root = et.getroot()

	new_xml = ET.Element('tools')

	for tr in root.findall('tr'):
		if not i<skipping: #skip first 2 lines
			try:
				item = tr.findall('td')

				category = item[3].text
				name = item[2].find('a').text
				url = item[2].find('a').get('href')

				node = ET.SubElement(new_xml, 'tool')
				node.set('temp_id',str(i))

				cat_n = ET.SubElement(node, 'category')
				cat_n.text = category

				name_n = ET.SubElement(node, 'name')
				name_n.text = name

				url_n = ET.SubElement(node, 'url')
				url_n.text = url

				web_based_n = ET.SubElement(node, 'web_based')
				web_based_n.text = random.choice(['web','desktop'])

				type_n = ET.SubElement(node, 'type')
				type_n.text = random.choice(['teaching','learning'])

				free_n = ET.SubElement(node, 'free')
				free_n.text = random.choice(['free','costs money'])

				description_n = ET.SubElement(node, 'description')
				description_n.text = "No description provided"

				added_on = ET.SubElement(node, 'added_on')
				now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
				added_on.text = now

			except IndexError as e:
				pass
		i+=1


	with open(settings.MEDIA_ROOT+'/data/f2.xml', 'w') as f:
		data_as_str = ET.tostring(new_xml).decode('utf-8')
		f.write(data_as_str)




def process():
	check_if_directory_exists()
	download_webpage()
	extract_tabelar_data()
	process_data_to_new_format()


if __name__ == '__main__':
	process()