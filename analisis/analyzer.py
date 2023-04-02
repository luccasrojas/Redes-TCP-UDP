"""Take all the log files from /LOGS_TCP/ p1, p2, ..., p6 and /LOGS_UDP/ p1, p2, ..., p6 and save it in a dictionary."""

import os
import re

logs = dict()

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
                        print(f"p{i} - {num_c} - {p} - {file} - {lineC[0]}")

                        print("\tCliente:", lineC)
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
                    
                        print("\tServidor:", lineS)
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

def main():
    """Main function."""
    for i in range(1,7):
        logs[f"p{i}"] = dict()

        savep(i, "TCP")
        savep(i, "UDP")

    print(logs)

if __name__ == "__main__":
    main()
