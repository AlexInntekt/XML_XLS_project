Validate from bash:
xmllint --noout --dtdvalid data.dtd ../media/data/f2.xml

#install xidel from binaries https://www.videlibri.de/xidel.html#downloads

How to run project:
python3 -m venv env
source env/bin/activate
pip3 install -r req.txt
python3 src/manage.py migrate
python3 src/manage.py runserver

