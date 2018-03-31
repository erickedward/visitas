from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Visitante
from .models import Departamento
from django.db.models import Q
from .forms import VisitaForm
from .forms import DepartamentoForm


def index(request):
	return render(request, 'aplicacionPrueba/index.html', {'activo':'index'})

def visitas_mostrar(request):
	reg_pagina = 6
	visit = Visitante.objects.all().order_by('-fecha_hora_entrada')[0:reg_pagina]
	cant_visitates = len (Visitante.objects.all())
	cant_paginas = int(cant_visitates/reg_pagina)

	if (int(cant_visitates/reg_pagina)<cant_visitates/reg_pagina):
		cant_paginas = cant_paginas + 1
	
	siguiente=2

	if (siguiente>cant_paginas):
		siguiente=''

	desc_paginacion =['Página 1 de '+str(cant_paginas),'Total de Registros '+str(cant_visitates)]
	
	return render(request, 'aplicacionPrueba/visitas_list.html', {'activo':'visitas', 'visit': visit, 'p_anterior':'', 'p_siguiente':siguiente, 'paginas':range(1,(cant_paginas+1)), 'desc_paginacion':desc_paginacion })


def visitas_list(request,pag):
	pagina = int(pag)
	reg_inicio=0
	reg_fin=6
	if pagina>1:
		reg_inicio = reg_fin*(pagina-1)
		reg_fin = reg_fin*pagina
	if (request.method == "POST" and request.POST.get("buscador")):
		buscar = request.POST.get("buscador")
		query = (Q(p_nombre__icontains=buscar) | Q(p_apellido__icontains=buscar) | Q(cedula__icontains=buscar)) 
		visit = Visitante.objects.filter(query).order_by('-fecha_hora_salida','-fecha_hora_entrada')[reg_inicio:reg_fin]
		cant_visitates = len(visit)
	else:
		visit = Visitante.objects.all().order_by('-fecha_hora_salida','-fecha_hora_entrada')[reg_inicio:reg_fin]
		cant_visitates = len (Visitante.objects.all())
		buscar='';

	cant_paginas = int(cant_visitates/(reg_fin-reg_inicio))

	if (int(cant_visitates/(reg_fin-reg_inicio))<cant_visitates/(reg_fin-reg_inicio)):
		cant_paginas = cant_paginas + 1

	if (pagina>1): 
		pagina = pagina - 1
	else:
		pagina = ''

	if pagina=='':
		siguiente=2
	else:
		siguiente=pagina+2

	if (siguiente>cant_paginas):
		siguiente=''

	if cant_visitates>0:
		desc_paginacion =['Página '+pag+' de '+str(cant_paginas),'Total de Registros '+str(cant_visitates)]
	else:
		desc_paginacion = ''
	return render(request, 'aplicacionPrueba/visitas_list.html', {'activo':'visitas','buscador':buscar,'visit': visit, 'p_anterior':pagina, 'p_siguiente':siguiente, 'paginas':range(1,(cant_paginas+1)), 'desc_paginacion':desc_paginacion})

def visita_add(request):
	if request.method == "POST":
		form = VisitaForm(request.POST)
		if form.is_valid():
			visita = form.save(commit=False)
			visita.fecha_hora_entrada = timezone.now()
			visita.save()
			return redirect('visitas_paginacion',pag=1)
	else:
		form = VisitaForm()
		return render(request, 'aplicacionPrueba/visita_form.html', {'activo':'visitas', 'form': form})

def visita_editar(request, pk):
	visita = get_object_or_404(Visitante, pk=pk)
	if request.method == "POST":
		form = VisitaForm(request.POST, instance=visita)
		if form.is_valid():
			post = form.save(commit=False)
			visita.fecha_hora_entrada = timezone.now()
			post.save()
			return redirect('visitas_paginacion',pag=1)
	else:
		form = VisitaForm(instance=visita)
		return render(request, 'aplicacionPrueba/visita_form.html', {'activo':'visitas', 'form': form})

def visita_salida(request,pk):
	visita = get_object_or_404(Visitante, pk=pk)
	if request.method == "GET":
		vist = Visitante.objects.get(id=pk)
		Visitante.salida(vist)
		visit = Visitante.objects.filter(id=pk)
		return render(request, 'aplicacionPrueba/visitas_list.html', {'activo':'visitas', 'visit': visit})

def visita_eliminar(request,pk):
	visita = get_object_or_404(Visitante, pk=pk)
	vist = Visitante.objects.get(id=pk)
	if request.method == "GET":
		return render(request, 'aplicacionPrueba/visita_eliminar.html', {'activo':'visitas', 'Visitante': vist})
	else:
		vist.delete()
		return redirect('visitas_paginacion',pag=1)

def departamentos(request,pag):
	pagina = int(pag)
	reg_inicio=0
	reg_fin=10
	if pagina>1:
		reg_inicio = reg_fin*(pagina-1)
		reg_fin = reg_fin*pagina

	if (request.method == "POST" and request.POST.get("buscador")):
		buscar = request.POST.get("buscador")
		query = (Q(nombre_dpto__icontains=buscar) | Q(piso__icontains=buscar))
		rs = Departamento.objects.filter(query).order_by('piso','nombre_dpto')[reg_inicio:reg_fin]
		total_reg = len(rs)
	else:
		rs = Departamento.objects.all().order_by('piso','nombre_dpto')[reg_inicio:reg_fin]
		total_reg = len (Departamento.objects.all())
		buscar='';

	cant_paginas = int(total_reg/(reg_fin-reg_inicio))

	if (int(total_reg/(reg_fin-reg_inicio))<total_reg/(reg_fin-reg_inicio)):
		cant_paginas = cant_paginas + 1

	if (pagina>1): 
		pagina = pagina - 1
	else:
		pagina = ''

	if pagina=='':
		siguiente=2
	else:
		siguiente=pagina+2

	if (siguiente>cant_paginas):
		siguiente=''

	if total_reg>0:
		desc_paginacion =['Página '+pag+' de '+str(cant_paginas),'Total de Registros '+str(len(rs))+' de '+str(total_reg)]
	else:
		desc_paginacion = ''
	return render(request, 'aplicacionPrueba/departamento_list.html', {'activo':'departamento','buscador':buscar,'rs': rs, 'p_anterior':pagina, 'p_siguiente':siguiente, 'paginas':range(1,(cant_paginas+1)), 'desc_paginacion':desc_paginacion})

def departamento_add(request):
	if request.method == "POST":
		form = DepartamentoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('departamentos',pag=1)
	else:
		form = DepartamentoForm()

		return render(request, 'aplicacionPrueba/departamento_form.html', {'activo':'departamento', 'form': form})

def departameto_eliminar(request,pk):
	depart= get_object_or_404(Departamento, pk=pk)
	dato = Departamento.objects.get(id=pk)
	if request.method == "GET":
		return render(request, 'aplicacionPrueba/departamento_eliminar.html', {'activo':'departamento', 'rs': dato})
	else:
		dato.delete()
		return redirect('departamentos',pag=1)

def departameto_editar(request, pk):
	formulario = get_object_or_404(Departamento, pk=pk)
	if request.method == "POST":
		form = DepartamentoForm(request.POST, instance=formulario)
		if form.is_valid():
			form.save()
			return redirect('departamentos',pag=1)
	else:
		form = DepartamentoForm(instance=formulario)
		return render(request, 'aplicacionPrueba/departamento_form.html', {'activo':'departamento', 'form': form})