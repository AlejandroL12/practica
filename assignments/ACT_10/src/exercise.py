def equivalente (horas,minutos,segundos):
    minutosasegundos=minutos*60
    horasasegundos=horas*60*60

    totalsegundos =  segundos + minutosasegundos + horasasegundos
    return totalsegundos

def main():
    #escribe tu código abajo de esta línea
    resultado = equivalente(2,20,8)

    print (resultado)

if __name__=='__main__':
    main()
