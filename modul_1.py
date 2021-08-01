import datetime
from dateutil.relativedelta import relativedelta
from tabulate import tabulate

def arch1(ruta):
    data = []
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    for person_claves in lineas:
        #print(person)
        data.append(person_claves.replace("\n","").split("\t"))
        #print(data)
    data.pop(0) #Eliminar head
    #print(data)
    return data

def pagos(list1,list2):
    """Aquí van la lista de empleados y los puestos"""
    pago = []
    for empleado in list1:
        for clave in list2:
            if empleado[4] == clave[0]:
                curp = empleado[3]
                Fecha_N= datetime.datetime.strptime(empleado[3][4:10],"%y%m%d").strftime("%d de %b del %Y")
                Sexo = empleado[3][10]
                dias_tra = empleado[5]
                claves = empleado[4]
                neto = str(int(empleado[5])*int(clave[1]))
                Edad = str((datetime.datetime.now() - datetime.datetime.strptime(empleado[3][4:10],"%y%m%d"))/360)
                emp=[curp, Fecha_N, Sexo, dias_tra, claves, neto, Edad]
                
                pago.append(emp)

            else:
                continue    
    return pago

def escribir(lista1):
    head = ["CURP", "FEC.NACIMIENTO", "SEXO", "DÍAS_TRABAJADOS", "CLAVE_PUESTO", "NETO X PAGAR", "AÑOS CUMPLIDOS"]
    with open("./pagosfinal3.txt","w", encoding="utf-8") as p:
        p.write(tabulate(lista1,headers=head,tablefmt="grid"))
        print(f"Archovo llamado pagos.txt en: {p}" + "\n" +str(datetime.datetime.now()))