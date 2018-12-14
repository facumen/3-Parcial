import random, pickle, os.path
names = 'Frodo', 'Silvio', 'Serra', 'Seffolani', 'Fritelli', 'Valerio', 'Juan', 'Pedro'


class Miembro:
    def __init__(self, dni, name, importe, esp, prov):
        self.dni = dni
        self.name = name
        self.importe = importe
        self.esp = esp
        self.prov = prov


def create_file(fd, n):
    m = open(fd, 'ab')
    for i in range(n):
        dni = random.randint(2000000, 45000000)
        name = random.choice(names)
        importe = random.randint(0, 10) * 100.34
        esp = random.randint(0, 19)
        prov = random.randint(0, 21)
        r = Miembro(dni, name, importe, esp, prov)
        pickle.dump(r, m)
    m.flush()
    m.close()
    input('Archivo creado satisfactoriamente!!\n')


def to_string(reg):
    print('-' * 100)
    r = ''
    r += '{:<20}'.format('DNI: ' + str(reg.dni))
    r += '{:<20}'.format('Name: ' + reg.name)
    r += '{:<20}'.format('Importe: ' + str(round(reg.importe, 2)))
    r += '{:<20}'.format('Especialidad: ' + str(reg.esp))
    r += '{:<20}'.format('Prov. de origen: ' + str(reg.prov))
    return r


def mostrar_archivo(fd):
    m = open(fd, 'rb')
    size = os.path.getsize(fd)
    while m.tell() < size:
        reg = pickle.load(m)
        print(to_string(reg))
    m.close()


def menu_opciones():
    print('-' * 110)
    print('1- Cargar registros en el archivo de médicos afilliados.')
    print('2- Mostrar el archivo creado en el punto. 1')
    print('3- A partir del archivo, crear un arreglo de registros en el cual se copien los datos de todos los médicos.')
    print('4- Mostrar el arreglo creado en el punto 3.')
    print('5- Buscar en el arreglo creado en el punto 3 un registro cuyo número dni sea igual a "x" '
          'y aumentar su importe un 10%')
    print('6- Buscar en el arreglo creado en el punto 3 un médico cuyo nombre sea igual a nom')
    print('7- Crear y mostrar una matriz de conteo donde indique cada miembro por especialidad y por provincia')
    print('-' * 110)


def add_in_order(v, reg):
    n = len(v)
    pos = n
    for i in range(n):
        if v[i].dni > reg.dni:
            pos = i
            break
    v[pos:pos] = [reg]


def create_vec(fd):
    v = []
    m = open(fd, 'rb')
    size = os.path.getsize(fd)
    while m.tell() < size:
        reg = pickle.load(m)
        if reg.importe != 0:
            add_in_order(v, reg)
    m.close()
    input('Vector creado correctamente!! \n')
    return v


def mostrar_vec(v):
    for i in range(len(v)):
        print(to_string(v[i]))


def buscar_dni(vec, x):
    for i in range(len(vec)):
        if vec[i].dni == x:
            if vec[i].prov == 1:
                print('Encontramos el registro!')
                print(to_string(vec[i]))
                print('Le sumamos un 10% a su importe\n')
                vec[i].importe += vec[i].importe // 10
                print(to_string(vec[i]))
                break
    else:
        print('Lo sentimos, no encontramos el dni ingresado')


def buscar_nom(vec, nom):
    for i in range(len(vec)):
        if vec[i].name == nom:
            print('Encontramos el regisro!!')
            print(to_string(vec[i]))
            break
    else:
        print('Lo sentimos, no encontramos el registro.')


def create_matrix(col, fil, v):
    mat = [[0] * fil for i in range(col)]
    for i in range(len(v)):
        mat[v[i].esp][v[i].prov] += 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] != 0:
                print('Existen', mat[f][c], 'miembros con la especialidad', f, 'de la prov', c)
