Autora: Heimy Katrin Acosta Cárdenas
Programa: Ingeniería de Sistemas – UNAD
Materia: Big Data
Tema: Procesamiento Batch y Streaming de la Tasa Representativa del Mercado (TRM)

📊 Descripción General del Proyecto

Este proyecto desarrolla una solución integral de Big Data para el análisis histórico y en tiempo real de la Tasa Representativa del Mercado (TRM) de Colombia, combinando las capacidades de Apache Spark y Apache Kafka.

El sistema integra dos enfoques:

Procesamiento Batch, enfocado en el análisis histórico y detección de comportamientos atípicos en los datos.

Procesamiento Streaming, diseñado para el monitoreo en tiempo real de variaciones en el valor del dólar y la generación de alertas automáticas.

🎯 Problema Abordado

La volatilidad del valor del dólar frente al peso colombiano tiene un impacto directo en la economía nacional, las importaciones, exportaciones y decisiones empresariales. Sin embargo, analizar de forma eficiente el histórico de la TRM y detectar cambios relevantes en tiempo real representa un reto técnico y computacional.

El proyecto afronta este problema mediante:
✅ El análisis histórico de la evolución del dólar desde 1991 hasta 2025.
✅ La detección de patrones y valores atípicos en la serie temporal.
✅ La implementación de alertas automáticas cuando la TRM supera umbrales críticos.
✅ El procesamiento de grandes volúmenes de datos financieros mediante tecnologías distribuidas.

🏗️ Arquitectura de la Solución

Flujo de trabajo:

Dataset TRM Histórico (Datos Abiertos Colombia)
⬇
Hadoop HDFS (almacenamiento distribuido)
⬇
Spark Batch Processing (análisis estadístico + detección de outliers)
⬇
Kafka Producer (emite datos simulados de TRM en tiempo real)
⬇
Spark Streaming Consumer (procesa flujo, calcula promedios y genera alertas)

⚙️ Requerimientos del Sistema

Sistema operativo: Ubuntu 22.04 LTS
Java: OpenJDK 11
Hadoop: 3.3.6
Spark: 3.5.3
Kafka: 3.6.2
Python: 3.8 o superior

🔧 Instalación de dependencias
pip install kafka-python pyspark

Verifica que Hadoop esté ejecutándose:

su - hadoop
start-all.sh
exit

Inicia servicios de Kafka:

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

Crea el topic para los datos TRM:

/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic trm_data

Verifica la creación:

/opt/Kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092

🚀 Ejecución del Sistema
🧮 Terminal 1: Análisis Batch
spark-submit trm_batch_analysis.py

Resultados esperados:

Estadísticas descriptivas de la TRM histórica

Evolución anual (1991–2025)

Detección de valores atípicos

Promedios, máximos y mínimos anuales

📡 Terminal 2: Productor Kafka
python3 trm_kafka_producer.py

Comportamiento:

Envía datos simulados cada 5 segundos

Rango de valores: 3.800 – 5.000 COP

Muestra cada envío en consola

⚙️ Terminal 3: Consumidor Spark Streaming
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 trm_spark_streaming.py

Funciones principales:

Genera alerta 🚨 cuando TRM > 5.000 COP

Calcula estadísticas en ventanas de 1 minuto

Procesamiento continuo en tiempo real

🌐 Monitoreo Web

Spark UI → http://localhost:4040/

Hadoop HDFS → http://localhost:9870/

Spark Master → http://localhost:8080/

📈 Resultados del Análisis

Procesamiento Batch:

Registros analizados: 8.112

Rango temporal: 1991–2025

Valor promedio histórico: 2.334,74 COP

Valor máximo histórico: 5.061,21 COP (2022)

Valores atípicos detectados: 88

Procesamiento Streaming:

Generación automática de alertas cuando TRM supera 5.000 COP

Actualización de estadísticas cada 60 segundos

Flujo de datos constante y estable

Conclusión Final

Este proyecto demostró el poder del Big Data para transformar datos financieros en conocimiento útil. A través del uso de Apache Spark y Kafka, fue posible integrar análisis histórico y monitoreo en tiempo real, permitiendo detectar comportamientos anómalos en la TRM y reaccionar ante variaciones críticas del mercado.
