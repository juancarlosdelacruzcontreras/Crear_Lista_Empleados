import modul_1 as m1

personas = m1.arch1("base.txt")
claves = m1.arch1("puestos.txt")
pagadas = m1.pagos(personas,claves)
m1.escribir(pagadas)
#print()