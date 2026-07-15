def validar_texto(dato):
    return len(dato.strip()) > 0

def validar_numero(dato):
    return dato.isdigit() and int(dato) > 0

def validar_cupos(dato):
    return dato.isdigit() and int(dato) >= 0

def validar_clase(dato):
    return dato.upper() in ['A', 'B', 'C']

def buscar_codigo(codigo, dicc):
    for c in dicc:
        if c.lower() == codigo.lower():
            return True
    return False

def cupos_genero(genero, peliculas, cartelera):
    total = 0
    for cod in peliculas:
        if peliculas[cod][1].lower() == genero.lower():
            total += cartelera[cod][1]
    print(f"El total de cupos disponibles es: {total}")

def buscar_precio(p_min, p_max, peliculas, cartelera):
    lista = []
    for cod in cartelera:
        precio = cartelera[cod][0]
        cupos = cartelera[cod][1]
        if p_min <= precio <= p_max and cupos > 0:
            lista.append(f"{peliculas[cod][0]}--{cod}")
    
    if not lista:
        print("No hay peliculas en ese rango de precios.")
    else:
        lista.sort()
        print(f"Las peliculas encontradas son: {lista}")

def actualizar(codigo, precio, cartelera):
    for cod in cartelera:
        if cod.lower() == codigo.lower():
            cartelera[cod][0] = precio
            return True
    return False

def agregar(cod, tit, gen, dur, clas, idio, es_3d, pre, cup, peliculas, cartelera):
    peliculas[cod] = [tit, gen, int(dur), clas.upper(), idio, es_3d]
    cartelera[cod] = [int(pre), int(cup)]

def eliminar(codigo, peliculas, cartelera):
    for cod in list(peliculas.keys()):
        if cod.lower() == codigo.lower():
            del peliculas[cod]
            del cartelera[cod]
            return True
    return False

def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True]
    }
    cartelera = {
        'P101': [5990, 40],
        'P103': [4990, 25],
        'P104': [6990, 12]
    }

    while True:
        print("========== MENU PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("==============================")
        
        op = input("Ingrese opción: ")
        
        if op == "1":
            gen = input("Ingrese genero a consultar: ")
            cupos_genero(gen, peliculas, cartelera)
        elif op == "2":
            try:
                minimo = int(input("Ingrese precio minimo: "))
                maximo = int(input("Ingrese precio maximo: "))
                buscar_precio(minimo, maximo, peliculas, cartelera)
            except:
                print("Debe ingresar valores enteros")
        elif op == "3":
            
            cod = input("Ingrese código de pelicula: ")
            nuevo = int(input("Ingrese nuevo precio: "))
            
            if actualizar(cod, nuevo, cartelera):
                print("Precio actualizado")
            else:
                print("El código no existe")
            
            otra = input("¿Desea actualizar otro precio (s/n)?: ")
            if otra.lower() != 's':
                continue
                
        elif op == "4":
            cod = input("Ingrese código de película: ")
            tit = input("Ingrese título: ")
            gen = input("Ingrese género: ")
            dur = input("Ingrese duración (minutos): ")
            clas = input("Ingrese clasificación: ")
            idio = input("Ingrese idioma: ")
            d3d = input("¿Es 3D? (s/n): ")
            pre = input("Ingrese precio: ")
            cup = input("Ingrese cupos: ")
            
            if not buscar_codigo(cod, peliculas) and validar_texto(tit) and validar_texto(gen) and validar_numero(dur) and validar_clase(clas) and validar_texto(idio) and validar_numero(pre) and validar_cupos(cup):
                es_3d = True if d3d.lower() == 's' else False
                agregar(cod, tit, gen, dur, clas, idio, es_3d, pre, cup, peliculas, cartelera)
                print("Película agregada")
            else:
                print("Datos inválidos o el código ya existe")
        elif op == "5":
            cod = input("Ingrese código de película: ")
            if eliminar(cod, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")
        elif op == "6":
            print("Programa finalizado.")
            break

main()