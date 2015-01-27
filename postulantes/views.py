#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from forms import UploadFileForm 
from models import Postulante 

# Create your views here.




def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #aqui va todo lo que tengo que hacer
            f = request.FILES['f']
            postulantes = f.readlines()
            for chunk in postulantes:
                chunk = chunk.split(';')

                hora = chunk[0].decode('iso-8859-1')
                fecha = chunk[1].decode('iso-8859-1')
                 
        
                try:
                    fecha = '%s-%s-%s %s'%(fecha.split('-')[2], fecha.split('-')[1], fecha.split('-')[0], hora) 

                except:
                    fecha = None 

                rut = chunk[2].decode('iso-8859-1')
                nombres = chunk[3].decode('iso-8859-1').title()
                apellidos = chunk[4].decode('iso-8859-1').title()
                domicilio=chunk[5].decode('iso-8859-1').title()
                comuna =chunk[6].decode('iso-8859-1').title()
                os10 =chunk[7].decode('iso-8859-1')
                if ('NO' or 'no' or 'No') in os10:
                    os10 = False
                elif ('SI' or 'SÍ' or 'sí' or 'si' or 'Sí' or 'Si') in os10:
                    os10 = True

                contratado = False 
              
                sexo =chunk[8].decode('iso-8859-1')
                medio =chunk[9].decode('iso-8859-1')
                cargo =chunk[10].decode('iso-8859-1')
                telefono =chunk[11].decode('iso-8859-1')
                observaciones = chunk[12].decode('iso-8859-1')
                reclutador =  chunk[13].decode('iso-8859-1')
                email = chunk[14].decode('iso-8859-1')
                postulante = Postulante(fecha=fecha, rut=rut, nombres=nombres, apellidos=apellidos, domicilio=domicilio, 
                comuna=comuna, os10=os10, sexo=sexo, medio=medio, cargo=cargo, telefono=telefono, 
                observaciones=observaciones, contratado=contratado, reclutador=reclutador, email=email)
                print rut
                postulante.save()

            return HttpResponse('OK') 
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form':form})
