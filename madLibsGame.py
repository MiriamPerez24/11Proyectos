#es un BUCLE, nos permite repetir un conjunto de codigo
loop = 1

while (loop < 2):

   
    sustantivo = input("Elija un sustantivo: ")
    p_sus = input("Elija un sustantivo en plural: ")
    sus2 = input("Elija otro sustantivo: ")
    lugar = input("Mencione un lugar: ")
    adj = input("Elija un adjetivo(Palabra que describe): ")
    sus3 = input("Elija un sustantivo: ")

    print ("------------------------------------------")
    print ("Se amable con tu ",sustantivo," porque es", p_sus)
    print ("Ya que podria ser de ", sus2,",")
    print ("Esto puede ser ",p_sus," en ",lugar)
    print ("Porque hace un buen ",adj,".")
    print ("Usted puede pensar que este es el ",sus3,",")
    print ("Bueno lo es.")
    print ("------------------------------------------")

    loop = loop + 1