from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("EDA").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Carga y limpieza
df = spark.read.csv("datos.csv", header=True, inferSchema=True).dropna().dropDuplicates()

# Análisis descriptivo
df.describe().show()
res = df.groupBy("sensor_id").agg(
    F.round(F.avg("temperatura"), 2).alias("temp_prom"),
    F.round(F.avg("humedad"), 2).alias("hum_prom")
).orderBy("sensor_id")
res.show()

# Generación de gráficos PNG
pdf = df.toPandas()
rpdf = res.toPandas()

plt.figure()
plt.hist(pdf["temperatura"], bins=20)
plt.title("Distribucion de temperatura")
plt.savefig("hist_temp.png")
plt.clf()

plt.figure()
plt.scatter(pdf["temperatura"], pdf["humedad"], s=5)
plt.title("Temperatura vs humedad")
plt.savefig("dispersion.png")
plt.clf()

plt.figure()
plt.bar(rpdf["sensor_id"].astype(str), rpdf["temp_prom"])
plt.title("Temperatura promedio por sensor")
plt.savefig("barras.png")

spark.stop()
print("Analisis finalizado exitosamente y graficos creados.")
