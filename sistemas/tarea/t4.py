import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_excel('Datos T4.xlsx')
df.head(5)

razones_por_fundacion = df.groupby('Fundación')['Razón de llegada'].nunique()
print("Cantidad de razones diferentes en cada fundación:")
print(razones_por_fundacion)

df['Fecha Unión'] = pd.to_datetime(df['Fecha Unión'], format='%Y-%m-%d')
personas_unidas_2023 = df[df['Fecha Unión'] > '2023-01-01'].groupby('Fundación')['Nombre'].count()
print("\nCantidad de personas que se unieron a cada fundación después del 1 de enero de 2023:")
print(personas_unidas_2023)

fundacion_asignada = df[df['Fundación'] == 'Fundación Gantz']
edad_promedio = fundacion_asignada['Edad'].mean()
edad_mediana = fundacion_asignada['Edad'].median()
print(f"\nEdad promedio y mediana en Fundación Gantz:")
print(f"Promedio: {edad_promedio}")
print(f"Mediana: {edad_mediana}")

def number_to_month(month):
    month_list = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    return month_list[month - 1]

# 4. Mes en que más personas han llegado a cada una de las fundaciones (Sin importar el año)
df['Mes unión'] = df['Fecha Unión'].dt.month
mes_mas_llegadas = df.groupby('Fundación')['Mes unión'].agg(lambda x: x.mode()[0])
mes_mas_llegadas = mes_mas_llegadas.apply(number_to_month)
print("\nMes en que más personas han llegado a cada fundación:")
print(mes_mas_llegadas)

voluntarios = df.groupby(['Sexo', 'Edad', 'País Origen']).size() / len(df) * 100
print("\nPorcentaje de personas que son voluntarias según sexo, edad y país de origen:")
print(voluntarios)

voluntarios = df[df['Voluntario']=="Sí"]
total_voluntarios = len(voluntarios)
print(f"Total de voluntarios: {total_voluntarios}")
print(f"porcentaje de voluntarios: {round(total_voluntarios / len(df) * 100, 2)}%")

voluntarios_F = voluntarios[voluntarios["Sexo"] == "F"]
voluntarios_M = voluntarios[voluntarios["Sexo"] == "M"]
voluntarios_sin_sexo = voluntarios[voluntarios["Sexo"].isnull()]
print(f"Total de voluntarios con sexo femenino: {len(voluntarios_F)}")
print(f"porcentaje de voluntarias (Sexo F) con respecto al total de voluntarios: {round(len(voluntarios_F) / total_voluntarios * 100, 2)}%")
print(f"porcentaje de voluntarias (Sexo F) con respecto al total de personas: {round(len(voluntarios_F) / len(df) * 100,2)}%\n")

print(f"Total de voluntarios con sexo masculino: {len(voluntarios_M)}")
print(f"porcentaje de voluntarios (Sexo M) con respecto al total de voluntarios: {round(len(voluntarios_M) / total_voluntarios * 100, 2)}%")
print(f"porcentaje de voluntarios (Sexo M) con respecto al total de personas: {round(len(voluntarios_M) / len(df) * 100,2)}%\n")

print(f"Total de voluntarios sin sexo registrado: {len(voluntarios_sin_sexo)}")
print(f"porcentaje de voluntari@s (Sexo NaN) con respecto al total de voluntarios: {round(len(voluntarios_sin_sexo) / total_voluntarios * 100, 2)}%")
print(f"porcentaje de voluntari@s (Sexo NaN) con respecto al total de personas: {round(len(voluntarios_sin_sexo) / len(df) * 100,2)}%")

voluntarios_por_edad_vol = voluntarios.groupby(['Edad']).size() / len(voluntarios) * 100
voluntarios_por_edad_tot = voluntarios.groupby(['Edad']).size() / len(df) * 100

print(f"porcentaje de voluntarios por rango de edad, con respecto al total de voluntarios:")
print(voluntarios_por_edad_vol)
print(f"{'-'*30}\n")
print(f"porcentaje de voluntarios por rango de edad, con respecto al total de personas:")
print(voluntarios_por_edad_tot)

voluntarios_por_pais_vol = voluntarios.groupby(['País Origen']).size() / len(voluntarios) * 100
voluntarios_por_pais_tot = voluntarios.groupby(['País Origen']).size() / len(df) * 100

print(f"porcentaje de voluntarios por país de origen, con respecto al total de voluntarios:")
print(voluntarios_por_pais_vol)
print(f"{'-'*30}\n")
print(f"porcentaje de voluntarios por país de origen, con respecto al total de personas:")
print(voluntarios_por_pais_tot)

menores_25_regular = df[(df['Edad'] < 25) & (df['Frecuencia Participación'] == 'Regular')].groupby('Fundación')['Nombre'].count()
menores_25_regular.plot(kind='bar')
plt.title('Cantidad de participantes menores a 25 años con frecuencia regular')
plt.ylabel('Cantidad')
plt.xlabel('Fundación')
plt.show()

df['Tiempo en fundación'] = (datetime.now() - df['Fecha Unión']).dt.days / 365 #agregar columna de tiempo en fundación medida en años
df['Porcentaje vida en fundación'] = df['Tiempo en fundación'] / df['Edad']
mas_del_25_vida = df[df['Porcentaje vida en fundación'] > 0.25].groupby('Fundación')['Nombre'].count()
mas_del_25_vida.plot(kind='pie', autopct='%1.1f%%')
plt.title('Personas que llevan más del 25% de su vida como voluntarios en cada fundación')
plt.ylabel('')
plt.show()