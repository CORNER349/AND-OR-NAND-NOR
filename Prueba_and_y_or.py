import random
import matplotlib.pyplot as plt


def adaline_and():

    # Datos de la compuerta AND
    datos = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]

    # Valores de mu
    mus = [0.01, 0.25, 0.50, 0.75]

    # Error deseado
    error_objetivo = 0.1

    # Generar pesos aleatorios iniciales
    random.seed(10)

    w1_inicial = random.uniform(-1, 1)
    w2_inicial = random.uniform(-1, 1)
    b_inicial = random.uniform(-1, 1)

    print("\nPESOS ALEATORIOS INICIALES")

    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    # Guardar resultados de cada mu
    resultados = {}

    # Entrenar con cada valor de mu
    for mu in mus:

        # Comenzar con los mismos pesos iniciales
        w1 = w1_inicial
        w2 = w2_inicial
        b = b_inicial

        iteracion = 0
        errores = []

        while True:

            error_total = 0

            for x1, x2, esperado in datos:

                # Salida de ADALINE
                y = w1 * x1 + w2 * x2 + b

                # Error
                error = esperado - y

                # Error cuadrático
                error_total += error ** 2

                # Corrección de los pesos
                w1 = w1 + mu * error * x1
                w2 = w2 + mu * error * x2
                b = b + mu * error

            # Error cuadrático medio
            mse = error_total / len(datos)

            # Guardar el error
            errores.append(mse)

            iteracion += 1

            # Detener cuando llegue al error deseado
            if mse <= error_objetivo:
                break

            # Límite de seguridad
            if iteracion >= 10000:
                break

        # Guardar resultados
        resultados[mu] = {
            "errores": errores,
            "iteraciones": iteracion,
            "w1": w1,
            "w2": w2,
            "b": b
        }

        # Mostrar resultados
        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        # Comparar pesos
        print("\nPesos iniciales:")

        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")

        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        # Comparar las salidas
        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            # Salida lineal
            y = w1 * x1 + w2 * x2 + b

            # Convertir la salida a 0 o 1
            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

    plt.figure()
  
    for mu in mus:
  
        errores = resultados[mu]["errores"]
  
        plt.plot(
          range(1, len(errores) + 1),
          errores,
          label="mu = " + str(mu)
        )
  
          # Línea del error objetivo
        plt.axhline(
            y=error_objetivo,
            linestyle="--",
            label="Error objetivo = 0.1"
        )
  
        plt.xlabel("Iteraciones")
        plt.ylabel("Error cuadrático medio")
        plt.title("ADALINE - Compuerta AND")
  
        plt.legend()
        plt.grid()
  
        plt.show()

def adaline_or():

    # Datos de la compuerta OR
    datos = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    # Valores de mu
    mus = [0.01, 0.25, 0.50, 0.75]

    # Error deseado
    error_objetivo = 0.1

    # Generar pesos aleatorios iniciales
    random.seed(10)

    w1_inicial = random.uniform(-1, 1)
    w2_inicial = random.uniform(-1, 1)
    b_inicial = random.uniform(-1, 1)

    print("\nPESOS ALEATORIOS INICIALES")

    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    # Guardar resultados de cada mu
    resultados = {}

    # Entrenar con cada valor de mu
    for mu in mus:

        # Comenzar con los mismos pesos iniciales
        w1 = w1_inicial
        w2 = w2_inicial
        b = b_inicial

        iteracion = 0
        errores = []

        while True:

            error_total = 0

            for x1, x2, esperado in datos:

                # Salida de ADALINE
                y = w1 * x1 + w2 * x2 + b

                # Error
                error = esperado - y

                # Error cuadrático
                error_total += error ** 2

                # Corrección de los pesos
                w1 = w1 + mu * error * x1
                w2 = w2 + mu * error * x2
                b = b + mu * error

            # Error cuadrático medio
            mse = error_total / len(datos)

            # Guardar el error
            errores.append(mse)

            iteracion += 1

            # Detener cuando llegue al error deseado
            if mse <= error_objetivo:
                break

            # Límite de seguridad
            if iteracion >= 10000:
                break

        # Guardar resultados
        resultados[mu] = {
            "errores": errores,
            "iteraciones": iteracion,
            "w1": w1,
            "w2": w2,
            "b": b
        }

        # Mostrar resultados
        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        # Comparar pesos
        print("\nPesos iniciales:")

        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")

        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        # Comparar las salidas
        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            # Salida lineal
            y = w1 * x1 + w2 * x2 + b

            # Convertir la salida a 0 o 1
            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

  # Graficar todos los valores de mu en una sola gráfica
    plt.figure()

    for mu in mus:

        errores = resultados[mu]["errores"]

        plt.plot(
            range(1, len(errores) + 1),
            errores,
            label="mu = " + str(mu)
        )

        # Línea del error objetivo
        plt.axhline(
            y=error_objetivo,
            linestyle="--",
            label="Error objetivo = 0.1"
        )

        plt.xlabel("Iteraciones")
        plt.ylabel("Error cuadrático medio")
        plt.title("ADALINE - Compuerta OR")

        plt.legend()
        plt.grid()

        plt.show()

# Llamar a la función
adaline_and()
adaline_or()