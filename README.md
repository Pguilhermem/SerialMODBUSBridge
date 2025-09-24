# Serial Modbus Bridge

Este projeto implementa uma ponte de comunicação entre dois dispositivos conectados a portas seriais distintas:

- Um **sistema de baterias** que se comunica via **Modbus RTU**.
- Um **microcontrolador** que envia comandos via **ASCII serial**.

## 📡 Protocolo de Comunicação

O microcontrolador envia uma linha ASCII terminada por `\n` contendo um número inteiro que representa o endereço Modbus a ser lido.

**Exemplo de entrada do microcontrolador:**
