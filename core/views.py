from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'menuprincipal_wiki.html')
def animales(request):
	return render(request, 'Animales.html')
def armas(request):
	return render(request, 'Armas.html')
def construcciones(request):
	return render(request, 'Construcciones.html')
def consumibles(request):
	return render(request, 'Consumibles.html')
def enemigos(request):
	return render(request, 'Enemigos.html')
def flora(request):
	return render(request, 'Flora.html')
def forowiki(request):
	return render(request, 'forowiki.html')
def historia(request):
	return render(request, 'historia.html')
def inicio_sesion_wiki(request):
	return render(request, 'inicio_sesion_wiki.html')
def logros(request):
	return render(request, 'Logros.html')
def lugarestf(request):
	return render(request, 'Lugarestf.html')
def micuentatf(request):
	return render(request, 'micuentatf.html')
def recuperarcontra(request):
	return render(request, 'recuperarcontra.html')
def registrase_wiki(request):
	return render(request, 'registrase_wiki.html')

def animalescss(request):
	return render(request, 'Animales.css')
def armascss(request):
	return render(request, 'Armas.css')
def construccionescss(request):
	return render(request, 'Construcciones.css')
def consumiblescss(request):
	return render(request, 'Consumibles.css')
def enemigoscss(request):
	return render(request, 'Enemigos.css')
def floracss(request):
	return render(request, 'flora.css')
def historiacss(request):
	return render(request, 'historia.css')
def logroscss(request):
	return render(request, 'Logros.css')
def sliderjs(request):
	return render(request, 'slider.js')
