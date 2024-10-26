## Descrição do Projeto
Este projeto é uma aplicação back-end construída com Django que segue as práticas de Código Limpo e o Design Orientado ao Domínio (DDD). A aplicação é modularizada em camadas para facilitar a manutenção e evolução, garantindo que cada camada tenha responsabilidades específicas.

## Arquitetura
A arquitetura do projeto foi desenhada de acordo com o DDD (Domain-Driven Design), separando as preocupações em quatro camadas principais:

- **Camada de domain**: Representa o núcleo da aplicação, onde ficam as regras de negócios e as entidades do domínio.
- **Camada de application**: Contém os serviços e coordenadores que orquestram os casos de uso, interagindo com o domínio e os adaptadores.
- **Camada de infra**: Engloba todas as implementações técnicas, como os repositórios de banco de dados e provedores de serviços externos.

## Requisitos

- **Python 3.12+**
- **Django 5.0+**
- **Django REST Framework** para a construção da API RESTful.
- **PostgreSQL** (ou outro banco de dados conforme configuração).
- **Docker** (opcional, para desenvolvimento e testes em container).