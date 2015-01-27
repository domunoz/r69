from models import Postulante

words = ('ANOTACIONES', 'anotaciones', 'Anotaciones', 'Hurto', 'hurto', 'HURTO', 'Faltas', 'faltas', 'FALTAS', 'ROBO',
'robo', 'Robo', 'Trafico ', 'TRAFICO', 'trafico', 'usurpacion', 'Usurpacion', 'USURPACION', 'INDEBIDA', 'indebida', 
'Indebida', 'ALCOHOL', 'alcohol', 'Alcohol', 'Homicidio', 'HOMICIDIO', 'homicidio', 'VIOLENCIA', 'Violencia', 'violencia',
'Estafa', 'ESTAFA', 'estafa', 'FRAUDE', 'fraude', 'Fraude', 'SEXUAL', 'sexual', 'Sexual', 'AMENAZA', 'Amenaza', 'amenaza',
'ABUSO', 'abuso', 'Abuso', 'DELITO', 'Delito', 'delito', 'DESORDEN', 'desorden', 'Desorden', 'DROGA', 'Droga', 'droga', 
'DENUNCIA', 'Denuncia', 'denuncia', 'PORTE DE ARMA')



def add_anotaciones():
    
    postulantes = Postulante.objects.all()
    
    for word in words:
        for p in postulantes:
            if word in p.observaciones:
                p.ha_sido_condenado_o_detenido = True
                p.save()


words2 = ('RETAIL', 'Retail', 'retail', 'INDUST', 'Indust', 'indust')
def add_industrial():
    
    postulantes = Postulante.objects.all()
    
    for word in words2:
        for p in postulantes:
            if word in p.observaciones:
                p.industrial = True
                p.save()





if __name__ == '__main__':
    add_anotaciones()
