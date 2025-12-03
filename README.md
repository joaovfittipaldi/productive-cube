# Productive Cube

Um sistema de gerenciamento de produtividade e tempo, desenvolvido com Flask e integrado com MQTT para comunicação em tempo real com dispositivos embarcados.

## Descrição do Projeto

O Productive Cube é uma aplicação que monitora e gerencia sessões de produtividade, permitindo rastrear o tempo gasto em atividades e analisar métricas de desempenho diário, semanal e mensal. O sistema utiliza um servidor Flask para fornecer APIs REST e se integra com um broker MQTT para comunicação com dispositivos IoT.

## Estrutura do Projeto

```
productive-cube/
├── README.md                    # Este arquivo
├── start_project.bat            # Script para iniciar o projeto
└── flask_server/                # Servidor Flask
    ├── requirements.txt         # Dependências do projeto
    ├── run.py                   # Ponto de entrada da aplicação
    ├── schema.sql              # Schema do banco de dados
    ├── populate.sql            # Scripts de população do banco
    └── app/
        ├── __init__.py          # Inicialização da aplicação Flask
        ├── environment.py       # Gerenciamento de variáveis de ambiente
        ├── database_setup.py    # Configuração inicial do banco de dados
        ├── database_manager.py  # Gerenciador de operações no banco
        ├── views.py             # Definição das rotas/endpoints
        ├── worker.py            # Worker para processar mensagens MQTT
        └── timer.py             # Gerenciamento de timers
```

## Configuração e Instalação

### Pré-requisitos

- Python 3.8+
- MySQL Server
- Um broker MQTT (ex: Mosquitto)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/joaovfittipaldi/productive-cube.git
cd productive-cube
```

2. Instale as dependências:
```bash
pip install -r flask_server/requirements.txt
```

3. Configure as variáveis de ambiente criando um arquivo `.env`:
```
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
MQTT_BROKER=seu_broker_mqtt
SECRET_KEY=sua_chave_secreta
```

4. Inicie o servidor:
```bash
python flask_server/run.py
```

## Dependências

- **Flask 3.0.3** - Framework web
- **mysql-connector-python 9.0.0** - Conector MySQL
- **python-dotenv 1.0.1** - Gerenciamento de variáveis de ambiente
- **paho-mqtt 2.1.0** - Cliente MQTT

## API Endpoints

### `/sessoes_completas`
Retorna o número de sessões não completas.
```json
{
  "sessoes_nao_completas": 5
}
```

### `/dia`
Retorna o total de tempo trabalhado no dia.
```json
{
  "total_diario": 480
}
```

### `/semana`
Retorna a meta semanal e o tempo total da semana.
```json
{
  "meta_semanal": 2400,
  "tempo_total_semana": 1850
}
```

### `/mes`
Retorna a meta mensal e o tempo total do mês.
```json
{
  "meta_mensal": 9600,
  "tempo_total_mes": 7200
}
```

### `/dashboard`
Retorna dados de desempenho semanal para o dashboard.

## Arquitetura

### Camada de Aplicação
- **views.py**: Define as rotas HTTP e endpoints da API
- **database_manager.py**: Gerencia consultas e operações no banco de dados
- **worker.py**: Processa mensagens MQTT em tempo real

### Camada de Dados
- **database_setup.py**: Configura conexão e schema do banco
- **schema.sql**: Define a estrutura das tabelas

### Configuração
- **environment.py**: Carrega variáveis de ambiente
- **timer.py**: Gerencia timers e sessões de produtividade

## Integração MQTT

O sistema se conecta a um broker MQTT para receber atualizações de status e comandos de dispositivos embarcados:

- **Tópico de Status**: `focuscube/status`
- **Tópico de Comando**: `focuscube/comando`

## Executar o Projeto

Use o script de inicialização:
```bash
start_project.bat
```

Ou execute diretamente:
```bash
python flask_server/run.py
```

## Segurança

- As credenciais do banco de dados são carregadas de variáveis de ambiente
- Use um arquivo `.env` para armazenar informações sensíveis
- Configure a chave secreta do Flask adequadamente

## Licença

Este projeto é parte de um trabalho acadêmico de sistemas embarcados.

## Autores

- João Vitor Fittipaldi
- André Luiz Goes Costa da Fonseca
- Lizandra Vieira
- Gabriel Caetano Farias
---

