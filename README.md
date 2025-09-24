# Serial Modbus Bridge

Este projeto implementa uma ponte de comunicação que permite que um microcontrolador se comunique com um sistema de baterias que utiliza o protocolo Modbus RTU. O microcontrolador envia comandos via uma porta serial ASCII para um computador (PC), que por sua vez, traduz esses comandos para o protocolo Modbus, consulta o sistema de baterias e retorna a resposta para o microcontrolador.

## 📡 Protocolo de Comunicação

A comunicação entre o microcontrolador e o PC é realizada através de uma interface serial ASCII simples:

1.  O **microcontrolador** envia uma linha de texto ASCII contendo um número inteiro, que representa o endereço Modbus a ser lido, terminada com um caractere de nova linha (`\n`).

      * **Exemplo de envio pelo microcontrolador:** `"123\n"`

2.  O **PC** recebe este endereço, realiza a leitura no dispositivo Modbus (o sistema de baterias) no endereço especificado.

3.  Após a leitura, o **PC** envia de volta para o **microcontrolador** o valor lido no registrador Modbus, também como uma linha de texto ASCII terminada com `\n`.

      * **Exemplo de resposta do PC:** `"456\n"` (onde 456 é o valor lido no endereço 123).

## ⚙️ Funcionalidades

  * **Ponte de Comunicação:** Atua como um intermediário entre um dispositivo serial ASCII e um dispositivo Modbus RTU.
  * **Leitura de Registradores:** Implementa a leitura de *holding registers* Modbus.
  * **Configurável:** As portas seriais e os parâmetros de comunicação podem ser facilmente configurados no código.
  * **Tratamento de Erros:** Inclui tratamento básico de erros para a comunicação Modbus e para a conversão de dados recebidos do microcontrolador.

## 📋 Pré-requisitos

  * Python 3
  * Bibliotecas Python listadas no arquivo `requirements.txt`:
      * `pymodbus`
      * `pyserial`

## 🚀 Instalação

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd serial-modbus-bridge
    ```

2.  **Instale as dependências:**
    Recomenda-se o uso de um ambiente virtual (`venv`) para isolar as dependências do projeto.

    ```bash
    # Crie um ambiente virtual (opcional, mas recomendado)
    python -m venv venv

    # Ative o ambiente virtual
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate

    # Instale as bibliotecas necessárias
    pip install -r requirements.txt
    ```

## 🔧 Configuração

Antes de executar o script, é necessário configurar as portas seriais e os parâmetros de comunicação no arquivo `serial_modbus_bridge.py`.

1.  **Configuração da porta Modbus RTU (sistema de baterias):**
    Localize e altere as seguintes linhas para corresponder à configuração do seu dispositivo Modbus:

    ```python
    modbus_client = ModbusSerialClient(
        method='rtu',
        port='COM3',          # Altere para a porta correta do sistema de baterias
        baudrate=9600,
        timeout=1,
        stopbits=1,
        bytesize=8,
        parity='N'
    )
    ```

2.  **Configuração da porta serial ASCII (microcontrolador):**
    Altere a porta `port` para a qual o seu microcontrolador está conectado:

    ```python
    micro_serial = serial.Serial(
        port='COM4',          # Altere para a porta correta do microcontrolador
        baudrate=9600,
        timeout=1
    )
    ```

## ▶️ Execução

Com as dependências instaladas e as portas configuradas, execute o script principal a partir do seu terminal:

```bash
python serial_modbus_bridge.py
```

O programa iniciará um loop infinito, aguardando os dados do microcontrolador, realizando as leituras no dispositivo Modbus e enviando as respostas. Para encerrar o programa, pressione `Ctrl+C` no terminal.

## 📁 Estrutura do Projeto

```
.
├── .gitignore               # Arquivo para ignorar arquivos e pastas no Git
├── README.md                # Este arquivo de documentação
├── requirements.txt         # Lista de dependências Python
└── serial_modbus_bridge.py  # O script principal da aplicação
```

## 🤝 Contribuições

Contribuições são bem-vindas\! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto não possui uma licença definida. Recomenda-se adicionar um arquivo `LICENSE` para esclarecer os termos de uso e distribuição do código.