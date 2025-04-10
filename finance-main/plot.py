import matplotlib.pyplot as plt

x = ["март","апрель","июнь","июль","август"]
incomes = [5000,4000,3250,10000,15000,20000]
expences = [4000,5000,4500,9000,15000,15000]

plt.plot(x, incomes, label="Доходы")
plt.plot(x, expences, label="Доходы")
plt.legend()
plt.grid()

plt.show()