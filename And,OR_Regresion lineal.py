import random
import matplotlib.pyplot as plt


class RegresionLineal:

    def __init__(self, nombre, datos):

        self.nombre = nombre
        self.datos = datos

        self.error_objetivo = 0.1
        self.mu = 0.1

        random.seed(10)

        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.b = random.uniform(-1, 1)

        self.iteraciones = []
        self.errores = []
        self.valores_mu = []


    def entrenar(self):

    
        print("COMPUERTA", self.nombre)

        print("\nPESOS INICIALES")
        print("w1 =", round(self.w1, 4))
        print("w2 =", round(self.w2, 4))
        print("b  =", round(self.b, 4))

        for epoca in range(1, 101):

            error_total = 0

            for x1, x2, esperado in self.datos:

                salida = (
                    self.b
                    + self.w1 * x1
                    + self.w2 * x2
                )

                error = esperado - salida

                error_total += error ** 2

                self.w1 += self.mu * error * x1
                self.w2 += self.mu * error * x2
                self.b += self.mu * error

            mse = error_total / len(self.datos)

            self.iteraciones.append(epoca)
            self.errores.append(mse)
            self.valores_mu.append(self.mu)

            if len(self.errores) > 1:

                if self.errores[-1] < self.errores[-2]:
                    self.mu *= 1.05
                else:
                    self.mu *= 0.7

            if mse <= self.error_objetivo:
                break


    def mostrar_pesos(self):

        print("\nPESOS FINALES")

        print("w1 =", round(self.w1, 4))
        print("w2 =", round(self.w2, 4))
        print("b  =", round(self.b, 4))

        print("Mu final =", round(self.mu, 4))


    def mostrar_resultados(self):

        print("\nCOMPARACIÓN DE RESULTADOS")

        print("x1\tx2\tEsperado\tSalida")

        for x1, x2, esperado in self.datos:

            salida = (
                self.b
                + self.w1 * x1
                + self.w2 * x2
            )

            print(
                x1,
                "\t",
                x2,
                "\t",
                esperado,
                "\t\t",
                round(salida, 4)
            )


    def mostrar_ecuacion(self):

        print("\nECUACIÓN DE REGRESIÓN")

        print(
            "y =",
            round(self.b, 4),
            "+",
            round(self.w1, 4),
            "* x1 +",
            round(self.w2, 4),
            "* x2"
        )


    def graficar_error(self):

        plt.figure()

        plt.plot(
            self.iteraciones,
            self.errores,
            marker="o",
            label="MSE"
        )

        plt.axhline(
            y=self.error_objetivo,
            linestyle="--",
            label="Error objetivo = 0.1"
        )

        plt.xlabel("Iteraciones")
        plt.ylabel("Error MSE")

        plt.title(
            "Regresión lineal - " + self.nombre
        )

        plt.legend()
        plt.grid()

        plt.show()


    def graficar_mu(self):

        plt.figure()

        plt.plot(
            self.iteraciones,
            self.valores_mu,
            marker="o"
        )

        plt.xlabel("Iteraciones")
        plt.ylabel("Mu")

        plt.title(
            "Evolución del factor de aprendizaje - "
            + self.nombre
        )

        plt.grid()

        plt.show()


    def ejecutar(self):

        self.entrenar()
        self.mostrar_pesos()
        self.mostrar_resultados()
        self.mostrar_ecuacion()
        self.graficar_error()
        self.graficar_mu()


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

modelo_and = RegresionLineal(
    "AND",
    and_datos
)

modelo_or = RegresionLineal(
    "OR",
    or_datos
)
modelo_and.ejecutar()

modelo_or.ejecutar()