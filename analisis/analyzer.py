"""Take all the log files from /LOGS_TCP/ p1, p2, ..., p6 and /LOGS_UDP/ p1, p2, ..., p6 and save it in a dictionary."""

import os
import re

def CC_to_w(string):
    # Split the string into words using regular expressions
    words = re.findall(r'[A-Z]?[a-z]+', string)
    # Join the words with spaces and return the result
    return ' '.join(words)

logs = dict()

dsc = {
    "p1": "1 cliente, archivo de 101.96MB",
    "p2": "1 cliente, archivo de 250MB",
    "p3": "5 clientes, archivo de 101.96MB",
    "p4": "5 clientes, archivo de 250MB",
    "p5": "10 clientes, archivo de 101.96MB",
    "p6": "10 clientes, archivo de 250MB",
}

def savep(i, p):
    pathClient = f"LOGS_{p}/p{i}/LogClient"
    pathServer = f"LOGS_{p}/p{i}/LogServer"

    for file in os.listdir(pathClient): # los archivos son los mismo para cliente y servidor
        if file.endswith("log.txt"):
            with open(f"{pathClient}/{file}", "r") as fC:
                with open(f"{pathServer}/{file}", "r") as fS:

                    headerC = fC.readline().strip().split(",")
                    headerC[0] = "PuertoCliente"
                    headerC[headerC.index("TamanioArchivo")] = "BytesCliente"
                    headerC[headerC.index("Tiempo")] = "TiempoCliente"

                    headerS = fS.readline().strip().split(",")
                    headerS[0] = "PuertoServidor"
                    headerS[headerS.index("TamanioArchivo")] = "BytesServidor"
                    headerS[headerS.index("Tiempo")] = "TiempoServidor"

                    for lineC, lineS in zip(fC,fS):
                        lineC = lineC.strip().split(",")
                        lineS = lineS.strip().split(",")

                        num_c = lineC[1].split(".")[0][-1]

                        # Datos del cliente
                        logs[f"p{i}"][num_c] = logs[f"p{i}"].get(num_c, {"TCP": dict(), "UDP": dict()})
                        for j in range(len(headerC)):
                            if headerC[j] in ["Hash", "NombreArchivo"]:
                                continue
                            try:
                                lineC[j] = int(lineC[j])
                            except ValueError:
                                try:
                                    lineC[j] = float(lineC[j])
                                except ValueError:
                                    pass
                            logs[f"p{i}"][num_c][p][headerC[j]] = lineC[j]
                        logs[f"p{i}"][num_c][p]["TasaCliente"] = logs[f"p{i}"][num_c][p]['BytesCliente'] / logs[f"p{i}"][num_c][p]['TiempoCliente']
                    
                        # Datos del servidor
                        for j in range(len(headerS)):
                            if headerS[j] in ["Hash", "NombreArchivo", "Entrega exitosa"]:
                                continue
                            if headerS[j] == "PuertoServidor":
                                lineS[j] = 10000 if p == "UDP" else 4456
                            try:
                                lineS[j] = int(lineS[j])
                            except ValueError:
                                try:
                                    lineS[j] = float(lineS[j])
                                except ValueError:
                                    pass
                            logs[f"p{i}"][num_c][p][headerS[j]] = lineS[j]
                        logs[f"p{i}"][num_c][p]["TasaServidor"] = logs[f"p{i}"][num_c][p]['BytesServidor'] / logs[f"p{i}"][num_c][p]['TiempoServidor']

                        # reordenar las columnas en el orden: "Entrega exitosa" (solo TCP), "PuertoCliente", "PuertoServidor", "BytesCliente", "BytesServidor", "TasaCliente", "TasaServidor", "TiempoCliente", "TiempoServidor"
                        if p == "TCP":
                            logs[f"p{i}"][num_c][p] = {k: logs[f"p{i}"][num_c][p][k] for k in ["Entrega exitosa", "PuertoCliente", "PuertoServidor", "BytesCliente", "BytesServidor", "TasaCliente", "TasaServidor", "TiempoCliente", "TiempoServidor"]}
                        else:
                            logs[f"p{i}"][num_c][p] = {k: logs[f"p{i}"][num_c][p][k] for k in ["PuertoCliente", "PuertoServidor", "BytesCliente", "BytesServidor", "TasaCliente", "TasaServidor", "TiempoCliente", "TiempoServidor"]}

def tomd(p, file):
    if file is None:
        # Convertir a código Markdown, donde p1, p2, ..., p6 son las tablas
        print(f"\n# Pruebas {p}\n")
        for k,v in logs.items():
            # k: p1, p2, ..., p6
            # v: {1: {"TCP": {...}, "UDP": {...}}, 2: {"TCP": {...}, "UDP": {...}}, 2: {...}}
            print(f"## Prueba {k[-1]}\n{dsc[k]}\n")

            print("| # |", end="")
            for c in v["1"][p].keys():
                if c in ["BytesCliente", "BytesServidor"]:
                    print(f" {CC_to_w(c)} (MB) |", end="")
                elif c in ["TasaCliente", "TasaServidor"]:
                    print(f" {CC_to_w(c)} (MBps) |", end="")
                elif c in ["TiempoCliente", "TiempoServidor"]:
                    print(f" {CC_to_w(c)} (ms) |", end="")
                else:
                    print(f" {CC_to_w(c)} |", end="") # Nombre de las columnas
            print()

            print("| --- |", end="")
            for c in v["1"][p].keys():
                print(" --- |", end="")
            print()

            for k2, v2 in v.items():
                # k2: 1, 2, 3, 4, 5, ...
                # v2: {"TCP": {...}, "UDP": {...}}
                print(f"| {k2} |", end="")
                for c, v3 in v2[p].items():
                    if c in ["BytesCliente", "BytesServidor", "TasaCliente", "TasaServidor"]:
                        print(f" {(v3/1e6):.2f} |", end="")
                    elif c in ["TiempoCliente", "TiempoServidor"]:
                        print(f" {(v3*1e3):.2f} |", end="")
                    else:
                        print(f" {v3} |", end="")
                print()
                    
            print()
    else:
        # Convertir a código Markdown, donde p1, p2, ..., p6 son las tablas
        print(f"\n## Pruebas {p}\n", file=file)
        for k,v in logs.items():
            # k: p1, p2, ..., p6
            # v: {1: {"TCP": {...}, "UDP": {...}}, 2: {"TCP": {...}, "UDP": {...}}, 2: {...}}
            print(f"### Prueba {k[-1]}\n{dsc[k]}\n", file=file)

            print("| # |", end="", file=file)
            for c in v["1"][p].keys():
                if c in ["BytesCliente", "BytesServidor"]:
                    print(f" {CC_to_w(c)} (MB) |", end="", file=file)
                elif c in ["TasaCliente", "TasaServidor"]:
                    print(f" {CC_to_w(c)} (MBps) |", end="", file=file)
                elif c in ["TiempoCliente", "TiempoServidor"]:
                    print(f" {CC_to_w(c)} (ms) |", end="", file=file)
                else:
                    print(f" {CC_to_w(c)} |", end="", file=file) # Nombre de las columnas
            print(file=file)

            print("| --- |", end="", file=file)
            for c in v["1"][p].keys():
                print(" --- |", end="", file=file)
            print(file=file)

            for k2, v2 in v.items():
                # k2: 1, 2, 3, 4, 5, ...
                # v2: {"TCP": {...}, "UDP": {...}}
                print(f"| {k2} |", end="", file=file)
                for c, v3 in v2[p].items():
                    if c in ["BytesCliente", "BytesServidor", "TasaCliente", "TasaServidor"]:
                        print(f" {(v3/1e6):.2f} |", end="", file=file)
                    elif c in ["TiempoCliente", "TiempoServidor"]:
                        print(f" {(v3*1e3):.2f} |", end="", file=file)
                    else:
                        print(f" {v3} |", end="", file=file)
                print(file=file)

            print(file=file)


def main(file=None):
    """Main function."""
    for i in range(1,7):
        logs[f"p{i}"] = dict()

        savep(i, "TCP")
        savep(i, "UDP")

    tomd("TCP", file)
    if file is not None:
        print("<br>", file=file)
    else:
        print("<br>")
    tomd("UDP", file)

if __name__ == "__main__":
    with open('logs.md', 'w') as f:
        main(file=f)

