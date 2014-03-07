#Create by: Tedezed
import webbrowser
import urllib2
from lxml import etree
from jinja2 import Template
ncapital = 0
vdireclist = ['Norte','Noreste','Este','Sureste','Sur','Suroeste','Oeste','Noroeste']
capital = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
list_cent = []
list_centmax = []
list_vspeed = []
list_vdirec = []

fil = open('Plantilla.html','r')
html = ''
for linea in fil:
	html = html + linea
Plantilla = Template(html)

while ncapital <= 7:
	url = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric&lang=es' 
		%capital[ncapital])
	raiz = etree.parse(url)
		
	cent = raiz.find('temperature').attrib['min']
	centmax = raiz.find('temperature').attrib['max']
	vspeed = float(raiz.find('wind/speed').attrib['value'])*1600/1000
	vdirec = float(raiz.find('wind/direction').attrib['value'])

	if vdirec == 0 or vdirec == 360:
		vdirec = vdireclist[0]
	elif vdirec > 0 and vdirec < 90:
		vdirec = vdireclist[1]
	if vdirec == 90:
		vdirec = vdireclist[2]
	elif vdirec > 90 and vdirec < 180:
		vdirec = vdireclist[3]
	if vdirec == 180:
		vdirec = vdireclist[4]
	elif vdirec > 180 and vdirec < 270: 
		vdirec = vdireclist[5]
	if vdirec == 270:
		vdirec = vdireclist[6]
	elif vdirec > 270 and vdirec < 360:
		vdirec = vdireclist[7]

	list_cent.append(cent)
	list_centmax.append(centmax)
	list_vspeed.append(vspeed)
	list_vdirec.append(vdirec)

	ncapital = ncapital + 1

Plantilla_sal = Plantilla.render(capitalh=capital,centh=list_cent,centmaxh=list_centmax,
	vspeedh=list_vspeed,vdirech=list_vdirec)
archi=open('Plantilla_sal.html','w')
archi.write(Plantilla_sal)
archi.close()
webbrowser.open("Plantilla_sal.html")

