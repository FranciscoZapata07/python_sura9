import pandas as pd

tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados)
#print(tablaEmpleados.to_string())

#filtro 1 quiero obtener todos los datos de los analistas 1
tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaAnalistas1.to_html()
archivoTEXTO=open("datosanalistas1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


#filtro 2 quiero obtener todos los datos de los analistas 2
tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas2.to_html()
archivoTEXTO=open("datosanalistas2.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()