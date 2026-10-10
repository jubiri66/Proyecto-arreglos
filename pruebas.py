from main import modificar, resumen

notas = [85, 67, 92, 74, 58]
assert resumen(notas) == (75.2, 3, 2)
print('Prueba 1: promedio y conteo iniciales - CORRECTA')
modificar(notas, 1, 80)
assert notas == [85, 80, 92, 74, 58]
assert resumen(notas) == (77.8, 4, 1)
print('Prueba 2: modificacion y recalculo - CORRECTA')
assert resumen([70, 69, 100, 0, 70]) == (61.8, 3, 2)
print('Prueba 3: limite de aprobacion - CORRECTA')
for indice, nota in [(5, 80), (1, 101), (-1, 90)]:
    anterior = notas.copy()
    try:
        modificar(notas, indice, nota)
        raise AssertionError('Se acepto una entrada invalida')
    except ValueError:
        assert notas == anterior
print('Prueba 4: entradas invalidas sin alterar el vector - CORRECTA')
