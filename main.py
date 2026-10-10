"""Sistema de calificaciones: ejemplo educativo de vectores en Python."""
NOTA_MINIMA = 70


def mostrar(calificaciones):
    for indice, nota in enumerate(calificaciones):
        if nota >= NOTA_MINIMA:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(f"Indice {indice} | Estudiante {indice + 1}: {nota} - {estado}")


def resumen(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    aprobados = 0
    for nota in calificaciones:
        if nota >= NOTA_MINIMA:
            aprobados += 1
    reprobados = len(calificaciones) - aprobados
    print(f"Promedio: {promedio:.2f}")
    print(f"Mayor: {max(calificaciones)} | Menor: {min(calificaciones)}")
    print(f"Aprobados: {aprobados} | Reprobados: {reprobados}")
    return promedio, aprobados, reprobados


def modificar(calificaciones, indice, nueva_nota):
    if not 0 <= indice < len(calificaciones):
        raise ValueError("Indice fuera de rango")
    if not 0 <= nueva_nota <= 100:
        raise ValueError("La nota debe estar entre 0 y 100")
    calificaciones[indice] = nueva_nota


def main():
    calificaciones = [85, 67, 92, 74, 58]
    print("SISTEMA DE CALIFICACIONES")
    print("Criterio del proyecto: aprobar con 70 o mas.")
    print("Vector inicial:", calificaciones)
    mostrar(calificaciones)
    print("Consulta por indice: calificaciones[2] =", calificaciones[2])
    print("RESULTADOS INICIALES")
    resumen(calificaciones)
    while True:
        try:
            indice = int(input("Indice a modificar (0 a 4): "))
            nueva_nota = int(input("Nueva nota entera (0 a 100): "))
            anterior = calificaciones[indice] if 0 <= indice < len(calificaciones) else None
            modificar(calificaciones, indice, nueva_nota)
            print(f"Modificacion: indice {indice}, de {anterior} a {nueva_nota}")
            break
        except ValueError as error:
            print("Entrada invalida:", error)
    print("Vector actualizado:", calificaciones)
    mostrar(calificaciones)
    print("RESULTADOS FINALES")
    resumen(calificaciones)
    print("Programa finalizado correctamente.")


if __name__ == "__main__":
    main()
