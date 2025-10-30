from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, avg, max, min, count, lit, window, current_timestamp
from pyspark.sql.types import StructType, StructField, DoubleType, StringType

# Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_TiempoReal_TRM") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("🔥 CONSUMIDOR SPARK STREAMING INICIADO 🔥")
print("Conectando con el topic 'trm_data' en Kafka...\n")

# Estructura esperada de los datos JSON que llegan desde Kafka
esquema_trm = StructType([
    StructField("valor", DoubleType(), True),
    StructField("fecha", StringType(), True),
    StructField("moneda", StringType(), True),
    StructField("cambio", DoubleType(), True)
])

# Lectura del stream desde Kafka
flujo_kafka = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "trm_data") \
    .option("startingOffsets", "latest") \
    .load()

# Convertir el valor de bytes a JSON legible
datos_parseados = flujo_kafka.select(
    from_json(col("value").cast("string"), esquema_trm).alias("info")
).select("info.*")

# Agregar marca de tiempo para análisis por ventana
datos_procesados = datos_parseados.withColumn("instante", current_timestamp())

# Crear una alerta si el valor supera los 5000
alertas = datos_procesados \
    .filter(col("valor") > 5000) \
    .withColumn("mensaje", lit("🚨 ¡ALERTA! La TRM ha superado los 5000 COP")) \
    .select("fecha", "valor", "mensaje")

# Estadísticas cada minuto (promedio, máximo, mínimo, cantidad)
