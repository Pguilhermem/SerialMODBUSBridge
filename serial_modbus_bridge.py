"""
serial_modbus_bridge.py

Este programa realiza a comunicação entre um sistema de baterias via Modbus RTU e um microcontrolador via comunicação serial ASCII.

Requisitos:
- pymodbus
- pyserial

Instale com:
    pip install pymodbus pyserial

Descrição do protocolo de comunicação com o microcontrolador:
- O microcontrolador envia uma linha ASCII terminada por '\n' contendo um número inteiro.
    Exemplo: "123\n" → representa o endereço Modbus a ser lido.
- O PC lê esse endereço, consulta o sistema de baterias via Modbus, e responde com o valor lido:
    Exemplo: "456\n" → valor lido no endereço 123.
"""

import serial
import time
from pymodbus.client import ModbusSerialClient

# Configuração da porta Modbus RTU (sistema de baterias)
modbus_client = ModbusSerialClient(
    method='rtu',
    port='COM3',          # Altere para a porta correta do sistema de baterias
    baudrate=9600,
    timeout=1,
    stopbits=1,
    bytesize=8,
    parity='N'
)

# Conecta ao cliente Modbus
modbus_client.connect()

# Configuração da porta serial ASCII (microcontrolador)
micro_serial = serial.Serial(
    port='COM4',          # Altere para a porta correta do microcontrolador
    baudrate=9600,
    timeout=1
)

def ler_endereco_modbus():
    """Lê o endereço Modbus enviado pelo microcontrolador."""
    if micro_serial.in_waiting:
        linha = micro_serial.readline().decode().strip()
        try:
            endereco = int(linha)
            return endereco
        except ValueError:
            print(f"Endereço inválido recebido: {linha}")
    return None

def ler_dado_modbus(endereco):
    """Lê o dado do sistema de baterias via Modbus."""
    try:
        resposta = modbus_client.read_holding_registers(address=endereco, count=1, unit=1)
        if resposta.isError():
            print("Erro na leitura Modbus.")
            return None
        return resposta.registers[0]
    except Exception as e:
        print(f"Exceção na leitura Modbus: {e}")
        return None

def enviar_dado_microcontrolador(dado):
    """Envia o dado lido para o microcontrolador."""
    if dado is not None:
        micro_serial.write(f"{dado}\n".encode())

# Loop principal
try:
    while True:
        endereco = ler_endereco_modbus()
        if endereco is not None:
            dado = ler_dado_modbus(endereco)
            enviar_dado_microcontrolador(dado)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Encerrando programa...")
finally:
    modbus_client.close()
    micro_serial.close()
