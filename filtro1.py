import pandas as pd

tablaMunicipios=pd.read_csv("./Siembras.csv")

datosBarbosa=tablaMunicipios[tablaMunicipios["Ciudad"]=="Barbosa"]
print(datosBarbosa)
archivoHTML=datosBarbosa.to_html()