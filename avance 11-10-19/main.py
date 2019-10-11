
txt = open("dataset.csv","r");
texto = txt.read();
txt.close();
textos = texto.split('\n');
datos = [];
for t in textos:
    datos.append(t.split(';'));
 # for t in datos:
 #     t[0:-1]
 # for t in datos:
 #     print(t);
titulos = datos[0][0:-1];
datos = datos[1:-1];
import json;
categorias = [];
conta = 0;
for a in titulos:
    categoria = {
    "titulo":"",
    "opciones":[],
    "cantidad sí":[],
    "cantidad no":[],
    "precisión": 0
    }
    categoria["titulo"] = a;
    for e in datos:
        if e[conta] not in categoria["opciones"]:
            categoria["opciones"].append(e[conta])
            categoria["cantidad sí"].append(0)
            categoria["cantidad no"].append(0)
    conta = conta + 1;
    categorias.append(categoria);
conta = 0;
contopc = 0;
for cat in categorias:
    contopc = -1;
    for opc in cat["opciones"]:
        contopc+=1;
        for d in datos:
            if opc == d[conta]:
                if d[-1] == "Yes":
                    cat["cantidad sí"][contopc] = cat["cantidad sí"][contopc] + 1;
                else:
                    cat["cantidad no"][contopc] = cat["cantidad no"][contopc] + 1;
    conta += 1;

for cat in categorias:
    print(cat)
# 
# conta = 0;
# for cat in categorias:
#     cant = len(cat["opciones"]);
#     num = 0;
#     den = 0;
#     for i in range(cant):
#
#
