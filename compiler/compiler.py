instrucciones = {
    "not": 0,
    "suma": 1,
    "resta": 2,
    "o": 3,
    "y": 4,
    "carga": 5,
    "almacena": 6,
    "sumai": 7,
    "igual": 8,
    "mayor": 9,
    "mayorig": 10
}

def complemento_a_dos(dec):
    if dec < 0:
        dec = dec + 16
    return format(dec, "x")

filename = input("Ingrese el nombre del archivo sin extensión: \n")

with open("programs/"+filename+".tsm", "r") as archivo:
    newLines = []
    for line in archivo:
        line = line.replace(",", "")
        words = line.split()
        
        opcode = instrucciones.get(words[0], None)

        if opcode is not None:
            if opcode >= 0 and opcode <= 6:
                opcode = format(opcode, "x")

                words[1] = words[1].replace("r", "")
                n1 = int(words[1])
                n1 = format(n1, "x")

                words[2] = words[2].replace("r", "")
                n2 = int(words[2])
                n2 = format(n2, "x")

                words[3] = words[3].replace("r", "")
                n3 = int(words[3])
                n3 = format(n3, "x")

                newLine = " ".join([opcode, n1, n2, n3])
                newLines.append(newLine)
            elif opcode == 7:
                opcode = format(opcode, "x")

                words[1] = words[1].replace("r", "")
                n1 = int(words[1])
                n1 = format(n1, "x")

                words[2] = words[2].replace("r", "")
                n2 = int(words[2])
                n2 = format(n2, "x")

                n3 = int(words[3])
                n3 = complemento_a_dos(n3)

                newLine = " ".join([opcode, n1, n2, n3])
                newLines.append(newLine)
            elif opcode >= 8 and opcode <= 10:
                opcode = format(opcode, "x")

                n1 = int(words[1])
                n1 = complemento_a_dos(n1)

                words[2] = words[2].replace("r", "")
                n2 = int(words[2])
                n2 = format(n2, "x")

                words[3] = words[3].replace("r", "")
                n3 = int(words[3])
                n3 = format(n3, "x")

                newLine = " ".join([opcode, n1, n2, n3])
                newLines.append(newLine)

with open("bin/"+filename+".x", "w") as archivo_destino:
    for line in newLines:
        archivo_destino.write(line + '\n')