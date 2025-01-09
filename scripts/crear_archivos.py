import os

"""
Only used it once to create the files and then fill them manually
"""

file_names = [
    "codigo_civil_y_comercial.txt",
    "codigo_penal.txt",
    "codigo_procesal_civil_y_comercial.txt",
    "codigo_procesal_penal_federal.txt",
    "codigo_aduanero.txt",
    "codigo_aeronautico.txt",
    "codigo_de_mineria.txt",
    "codigo_alimentario_argentino.txt",
    "codigo_de_etica_publica.txt",
    "codigo_electoral_nacional.txt"
]

for file_name in file_names:
    with open('../data/' + file_name, 'w') as f:
        pass

print("Archivos creados exitosamente.")