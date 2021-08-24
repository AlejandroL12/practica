def equivalente (horas,minutos,segundos):
    minutosasegundos=minutos*60
    horasasegundos=horas*60*60

    totalsegundos =  segundos + minutosasegundos + horasasegundos
    return totalsegundos


def tiempoProceso (proceso,horas,minutos,segundos):
    print(proceso)

    horas=int(input("Dame las horas del "+proceso+": ")
    minutos=int(input("Dame las minutos del "+proceso+": ")
    segundos=int(input("Dame las segundos del "+proceso+": ")

    print("Total de segundos del "+procesos+"= "+str(equivalente (horas,minutos,segundos)))

def main():
    #escribe tu código abajo de esta línea

    tiempoProceso("Proceso-1")
    tiempoProceso("Proceso-2")

if __name__=='__main__':
    main()
