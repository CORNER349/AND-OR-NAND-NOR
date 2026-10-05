import random
import matplotlib.pyplot as plt


def regresion_lineal(nombre, datos):

    mu = 0.1
    mu_inicial = mu

    error_objetivo = 0.1
    max_iteraciones = 1000

    aumento = 1.05
    reduccion = 0.5


    random.seed(10)

    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)
    b = random.uniform(-1, 1)

    w1_inicial = w1
    w2_inicial = w2
    b_inicial = b

    print("REGRESIÓN LINEAL -", nombre)

    print("\nPESOS INICIALES")
    print("w1 =", round(w1, 4))
    print("w2 =", round(w2, 4))
    print("b  =", round(b, 4))

    errores = []
    valores_mu = []
    iteraciones = []

    error_anterior = None


    for epoca in range(1, max_iteraciones + 1):

        # Gradientes
        gradiente_w1 = 0
        gradiente_w2 = 0
        gradiente_b = 0

        error_total = 0

        n = len(datos)


        for x1, x2, esperado in datos:

            prediccion = (
                b
                + w1 * x1
                + w2 * x2
            )

            error = prediccion - esperado

            # Error cuadrático
            error_total += error ** 2


            # Gradientes del MSE

            gradiente_w1 += (
                2 * error * x1
            ) / n

            gradiente_w2 += (
                2 * error * x2
            ) / n

            gradiente_b += (
                2 * error
            ) / n


        mse = error_total / n


        errores.append(mse)

        valores_mu.append(mu)

        iteraciones.append(epoca)


        if error_anterior is not None:
            if mse < error_anterior:
                mu = mu * aumento
            else:

                mu = mu * reduccion


        error_anterior = mse

        w1 = w1 - mu * gradiente_w1

        w2 = w2 - mu * gradiente_w2

        b = b - mu * gradiente_b


        print(
            "Iteración:", epoca,
            "| Error:", round(mse, 6),
            "| Mu:", round(mu, 6)
        )

        if mse <= error_objetivo:
            break

    print("COMPARACIÓN DE PESOS")

    print(
        "w1:",
        round(w1_inicial, 4),
        " -> ",
        round(w1, 4)
    )

    print(
        "w2:",
        round(w2_inicial, 4),
        " -> ",
        round(w2, 4)
    )

    print(
        "b :",
        round(b_inicial, 4),
        " -> ",
        round(b, 4)
    )


    print("\nMu inicial:", mu_inicial)

    print("Mu final:", round(mu, 6))

    print("Iteraciones:", epoca)

    print("Error final:", round(mse, 6))


    print("SALIDA VS ESPERADO")
   

    print(
        "X1\tX2\tPredicción\tSalida\tEsperado"
    )


    for x1, x2, esperado in datos:

        prediccion = (
            b
            + w1 * x1
            + w2 * x2
        )

        if prediccion >= 0.5:
            salida = 1
        else:
            salida = 0


        print(
            x1,
            "\t",
            x2,
            "\t",
            round(prediccion, 4),
            "\t\t",
            salida,
            "\t",
            esperado
        )

    print("\nECUACIÓN DE REGRESIÓN")

    print(
        "y =",
        round(b, 4),
        "+",
        round(w1, 4),
        "* x1 +",
        round(w2, 4),
        "* x2"
    )
    plt.figure()

    plt.plot(
        iteraciones,
        errores,
        marker="o",
        label="MSE"
    )

    plt.axhline(
        y=error_objetivo,
        linestyle="--",
        label="Error objetivo = 0.1"
    )

    plt.xlabel("Iteraciones")

    plt.ylabel("Error MSE")

    plt.title(
        "Regresión lineal - " + nombre
    )

    plt.legend()

    plt.grid()

    plt.show()

    plt.figure()

    plt.plot(
        iteraciones,
        valores_mu,
        marker="o"
    )

    plt.xlabel("Iteraciones")

    plt.ylabel("Mu")

    plt.title(
        "Evolución del factor de aprendizaje - "
        + nombre
    )

    plt.grid()

    plt.show()


and_datos = [

    [0, 0, 0],

    [0, 1, 0],

    [1, 0, 0],

    [1, 1, 1]

]

or_datos = [

    [0, 0, 0],

    [0, 1, 1],

    [1, 0, 1],

    [1, 1, 1]

]

regresion_lineal(
    "AND",
    and_datos
)

regresion_lineal(
    "OR",
    or_datos
)