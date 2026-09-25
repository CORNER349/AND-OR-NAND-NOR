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

    print("\n====================================")
    print("COMPUERTA AND")
    print("====================================")

    print("\nPESOS ALEATORIOS INICIALES")
    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    resultados = {}

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

        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        print("\nPesos iniciales:")
        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")
        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            y = w1 * x1 + w2 * x2 + b

            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

    # UNA SOLA GRÁFICA PARA AND
    plt.figure()

    for mu in mus:

        errores = resultados[mu]["errores"]

        plt.plot(
            range(1, len(errores) + 1),
            errores,
            label="mu = " + str(mu)
        )

    plt.axhline(
        y=error_objetivo,
        linestyle="--",
        label="Error objetivo = 0.1"
    )

    plt.xlabel("Iteraciones")
    plt.ylabel("Error cuadrático medio")
    plt.title("ADALINE - AND")
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

    mus = [0.01, 0.25, 0.50, 0.75]
    error_objetivo = 0.1

    random.seed(10)

    w1_inicial = random.uniform(-1, 1)
    w2_inicial = random.uniform(-1, 1)
    b_inicial = random.uniform(-1, 1)

    print("\n====================================")
    print("COMPUERTA OR")
    print("====================================")

    print("\nPESOS ALEATORIOS INICIALES")
    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    resultados = {}

    for mu in mus:

        w1 = w1_inicial
        w2 = w2_inicial
        b = b_inicial

        iteracion = 0
        errores = []

        while True:

            error_total = 0

            for x1, x2, esperado in datos:

                y = w1 * x1 + w2 * x2 + b

                error = esperado - y

                error_total += error ** 2

                w1 = w1 + mu * error * x1
                w2 = w2 + mu * error * x2
                b = b + mu * error

            mse = error_total / len(datos)

            errores.append(mse)
            iteracion += 1

            if mse <= error_objetivo:
                break

            if iteracion >= 10000:
                break

        resultados[mu] = {
            "errores": errores,
            "iteraciones": iteracion,
            "w1": w1,
            "w2": w2,
            "b": b
        }

        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        print("\nPesos iniciales:")
        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")
        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            y = w1 * x1 + w2 * x2 + b

            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

    # UNA SOLA GRÁFICA PARA OR
    plt.figure()

    for mu in mus:

        errores = resultados[mu]["errores"]

        plt.plot(
            range(1, len(errores) + 1),
            errores,
            label="mu = " + str(mu)
        )

    plt.axhline(
        y=error_objetivo,
        linestyle="--",
        label="Error objetivo = 0.1"
    )

    plt.xlabel("Iteraciones")
    plt.ylabel("Error cuadrático medio")
    plt.title("ADALINE - OR")
    plt.legend()
    plt.grid()
    plt.show()


def adaline_nand():

    # Datos de la compuerta NAND
    datos = [
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    mus = [0.01, 0.25, 0.50, 0.75]
    error_objetivo = 0.1

    random.seed(10)

    w1_inicial = random.uniform(-1, 1)
    w2_inicial = random.uniform(-1, 1)
    b_inicial = random.uniform(-1, 1)

    print("\n====================================")
    print("COMPUERTA NAND")
    print("====================================")

    print("\nPESOS ALEATORIOS INICIALES")
    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    resultados = {}

    for mu in mus:

        w1 = w1_inicial
        w2 = w2_inicial
        b = b_inicial

        iteracion = 0
        errores = []

        while True:

            error_total = 0

            for x1, x2, esperado in datos:

                y = w1 * x1 + w2 * x2 + b

                error = esperado - y

                error_total += error ** 2

                w1 = w1 + mu * error * x1
                w2 = w2 + mu * error * x2
                b = b + mu * error

            mse = error_total / len(datos)

            errores.append(mse)
            iteracion += 1

            if mse <= error_objetivo:
                break

            if iteracion >= 10000:
                break

        resultados[mu] = {
            "errores": errores,
            "iteraciones": iteracion,
            "w1": w1,
            "w2": w2,
            "b": b
        }

        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        print("\nPesos iniciales:")
        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")
        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            y = w1 * x1 + w2 * x2 + b

            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

    # UNA SOLA GRÁFICA PARA NAND
    plt.figure()

    for mu in mus:

        errores = resultados[mu]["errores"]

        plt.plot(
            range(1, len(errores) + 1),
            errores,
            label="mu = " + str(mu)
        )

    plt.axhline(
        y=error_objetivo,
        linestyle="--",
        label="Error objetivo = 0.1"
    )

    plt.xlabel("Iteraciones")
    plt.ylabel("Error cuadrático medio")
    plt.title("ADALINE - NAND")
    plt.legend()
    plt.grid()
    plt.show()


def adaline_nor():

    # Datos de la compuerta NOR
    datos = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 0]
    ]

    mus = [0.01, 0.25, 0.50, 0.75]
    error_objetivo = 0.1

    random.seed(10)

    w1_inicial = random.uniform(-1, 1)
    w2_inicial = random.uniform(-1, 1)
    b_inicial = random.uniform(-1, 1)

    print("\n====================================")
    print("COMPUERTA NOR")
    print("====================================")

    print("\nPESOS ALEATORIOS INICIALES")
    print("w1 =", round(w1_inicial, 4))
    print("w2 =", round(w2_inicial, 4))
    print("b =", round(b_inicial, 4))

    resultados = {}

    for mu in mus:

        w1 = w1_inicial
        w2 = w2_inicial
        b = b_inicial

        iteracion = 0
        errores = []

        while True:

            error_total = 0

            for x1, x2, esperado in datos:

                y = w1 * x1 + w2 * x2 + b

                error = esperado - y

                error_total += error ** 2

                w1 = w1 + mu * error * x1
                w2 = w2 + mu * error * x2
                b = b + mu * error

            mse = error_total / len(datos)

            errores.append(mse)
            iteracion += 1

            if mse <= error_objetivo:
                break

            if iteracion >= 10000:
                break

        resultados[mu] = {
            "errores": errores,
            "iteraciones": iteracion,
            "w1": w1,
            "w2": w2,
            "b": b
        }

        print("\n====================================")
        print("MU =", mu)
        print("====================================")

        print("\nNúmero de iteraciones:", iteracion)
        print("Error final:", round(errores[-1], 6))

        print("\nPesos iniciales:")
        print("w1 =", round(w1_inicial, 4))
        print("w2 =", round(w2_inicial, 4))
        print("b =", round(b_inicial, 4))

        print("\nPesos corregidos:")
        print("w1 =", round(w1, 4))
        print("w2 =", round(w2, 4))
        print("b =", round(b, 4))

        print("\nComparación de las salidas:")

        for x1, x2, esperado in datos:

            y = w1 * x1 + w2 * x2 + b

            if y >= 0.5:
                salida = 1
            else:
                salida = 0

            print("\nEntrada:", x1, x2)
            print("Salida de ADALINE:", round(y, 4))
            print("Salida obtenida:", salida)
            print("Salida esperada:", esperado)

    # UNA SOLA GRÁFICA PARA NOR
    plt.figure()

    for mu in mus:

        errores = resultados[mu]["errores"]

        plt.plot(
            range(1, len(errores) + 1),
            errores,
            label="mu = " + str(mu)
        )

    plt.axhline(
        y=error_objetivo,
        linestyle="--",
        label="Error objetivo = 0.1"
    )

    plt.xlabel("Iteraciones")
    plt.ylabel("Error cuadrático medio")
    plt.title("ADALINE - NOR")
    plt.legend()
    plt.grid()
    plt.show()


# Llamar a las funciones
adaline_and()
adaline_or()
adaline_nand()
adaline_nor()