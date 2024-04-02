import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Linewidth = controla a espessuira da linha que plot() gera 
ax.plot(x_values,y_values, linewidth=3)

#Define o titulo do Grafico e os eixos do rotulo 
ax.set_title("Square numbers", fontsize=24)
ax.set_title("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Define o intervalo para cada eixo 
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

#Define o tamanho dos rotulos de marcação de escala
ax.tick_params(labelsize=14)

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')