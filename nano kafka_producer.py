import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Función para generar datos falsos de TRM
def crear_dato_trm():
    valor_base = random.uniform(3800, 5000)
    return {
        "valor": round(valor_base, 2),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "moneda": "COP",
        "cambio": round(random.uniform(-50, 50), 2)
    }

# Configuración del productor
productor = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda mensaje: json.dumps(mensaje).encode("utf-8")
)

print("🚀 Productor Kafka - Simulación TRM")
print("Enviando datos simulados al topic 'trm_data' cada 5 segundos...")
print("Presiona CTRL+C para detener el envío.\n")

try:
    while True:
        dato_trm = crear_dato_trm()
        productor.send("trm_data", value=dato_trm)
        print(f"📤 Dato enviado: {dato_trm}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Proceso detenido por el usuario.")
finally:
    productor.close()
    print("✅ Conexión con Kafka cerrada correctamente.")
