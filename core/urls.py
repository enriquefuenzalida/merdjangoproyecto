from django.urls import path
from .views import home, animales, armas, construcciones, consumibles, enemigos, flora, forowiki, historia, inicio_sesion_wiki, logros, lugarestf, micuentatf, recuperarcontra, registrase_wiki, animalescss, armascss, construccionescss, consumiblescss, enemigoscss, floracss, historiacss, logroscss, sliderjs

urlpatterns = [
	path('',home,name="home"),
	path('Animales.html',animales,name="animales"),
	path('Armas.html',armas,name="armas"),
	path('Construcciones.html',construcciones,name="construcciones"),
	path('Consumibles.html',consumibles,name="consumibles"),
	path('Enemigos.html',enemigos,name="enemigos"),
	path('Flora.html',flora,name="flora"),
	path('forowiki.html',forowiki,name="forowiki"),
	path('historia.html',historia,name="historia"),
	path('inicio_sesion_wiki.html',inicio_sesion_wiki,name="inicio_sesion_wiki"),
	path('Logros.html',logros,name="logros"),
	path('Lugarestf.html',lugarestf,name="lugarestf"),
	path('micuentatf.html',micuentatf,name="micuentatf"),
	path('recuperarcontra.html',recuperarcontra,name="recuperarcontra"),
	path('registrase_wiki.html',registrase_wiki,name="registrase_wiki"),
	
	path('Animales.css',animalescss,name="animalescss"),	
	path('Armas.css',armascss,name="armascss"),	
	path('Construcciones.css',construccionescss,name="construccionescss"),	
	path('Consumibles.css',consumiblescss,name="consumiblescss"),	
	path('Enemigos.css',enemigoscss,name="enemigoscss"),	
	path('flora.css',floracss,name="floracss"),	
	path('historia.css',historiacss,name="historiacss"),
	path('Logros.css',logroscss,name="logroscss"),
	path('slider.js',sliderjs,name="sliderjs"),

]

