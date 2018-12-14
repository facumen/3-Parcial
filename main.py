from reg import *
fd = 'members.dat'


def main():
    opcion = -1
    while opcion != 0:
        if opcion == 1:
            n = int(input('Ingrese la cantidad de registros a cargar en el archivo: '))
            create_file(fd, n)
        elif opcion == 2:
            mostrar_archivo(fd)
        elif opcion == 3:
            vec = create_vec(fd)
        elif opcion == 4:
            mostrar_vec(vec)
        elif opcion == 5:
            x = int(input('Ingrese el DNI a buscar: '))
            buscar_dni(vec, x)
        elif opcion == 6:
            nom = input('Ingrese el nombre a buscar: ')
            buscar_nom(vec, nom)
        elif opcion == 7:
            create_matrix(20, 22, vec)
        elif opcion == 8:
            menu_opciones()
        opcion = int(input('\nIngrese la opcion deseada(8- Menu): '))


main()