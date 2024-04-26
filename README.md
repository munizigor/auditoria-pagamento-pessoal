# Controle de Pagamentos de Pessoal

Este repositório contém um sistema desenvolvido para o controle de pagamentos de pessoal, especializado na análise e processamento de dados de remuneração do sistema SIAPE, bases corporativas e arquivos de dados. O sistema foi concebido pelo Tenente-Coronel QOBM/Comb. Igor MUNIZ da Silva como produto do trabalho monográfico do Curso de Altos Estudos para Oficiais Combatentes do ano de 2023 (CAEO/Comb - 2023), realizado no Centro de Estudos de Política, Estratégia e Doutrina (CEPED) do Corpo de Bombeiros Militar do Distrito Federal.

## Objetivo

O objetivo principal do sistema é automatizar o processo de controle de pagamentos, desde a extração das bases de dados até a geração de relatórios finais. Ele lida com dados provenientes do sistema SIAPE, GECOPE, GEDEP e GSVWeb, realizando diversas etapas de formatação, validação e análise para garantir a precisão e integridade dos resultados.

## Requisitos

Para executar o sistema, você precisa ter os seguintes requisitos instalados:

- [Python](https://www.python.org/downloads/) 3.8 ou superior
- Pacote [libpq-dev](https://www.postgresql.org/docs/devel/libpq.html), necessário para operar com o PostgreSQL
- [Git](https://git-scm.com/)

## Estrutura do Diretório

    .
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── src
        ├── sispag
        │   ├── Controle de Folha.ipynb
        │   └── queries.py
        ├── 
        ├── dados
        │   └── csv
        │       └── remuneracao
        │           ├── dwsiape
        │           │   ├── AAAAMM
        │           │   │   └── Relatório Auditoria Mensal - AAAAMM.txt
        │           │   └── AAAAMM
        │           │       └── Relatório Auditoria Mensal - AAAAMM.txt
        │           └── remuneracao.csv
        └── relatorios
            └── relatorioMensal - AAAAMM.csv

## Estrutura do Arquivo _Controle de Folha.ipynb_

O código está estruturado em diversos passos, cada um correspondendo a uma etapa específica do processo de controle de pagamentos. Abaixo estão os principais passos do código:

### Extração das bases de dados

- Inclui a obtenção de dados dos sistemas SIAPE, GECOPE, GEDEP e GSVWeb.

### Formatação e validação dos dados

- Realiza a formatação adequada dos dados e validações, incluindo a correção do número de CPF quando necessário.

### Criação de tabela remuneratória

- Gera uma tabela remuneratória específica para o mês especificado.

### Manipulação e transformação dos dados

- Realiza manipulações e transformações nos dados conforme as necessidades do processo.

### Abordagem geral

- Identifica valores que estão lançados em conformidade com os dados cadastrais, seguindo uma abordagem de fora para dentro.

### Abordagem pontual

- Identifica lançamentos atípicos (outliers), seguindo uma abordagem de dentro para fora

### Geração de Relatório Final

- Produz um relatório final contendo as rubricas do mês e uma análise detalhada dos valores

## Como Utilizar

Para utilizar o sistema, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/munizigor/SISPAG-Controle.git
2. Acesse o diretório do projeto:

    ```bash
    cd SISPAG-Controle
3. Crie um ambiente virtual para a instalação isolada das dependências do código:

   ```bash
   python -m venv ./venv
4. Ative o ambiente virtual

   ```bash
   source venv/bin/activate
5. Instale as dependências do sistema constantes no arquivo _requirements.txt_:

   ```bash
   pip install -r requirements.txt
7. Insira o arquivo de relatório de folha extraído do sistema DW SIAPE e insira-o na pasta correspondente AO MÊS DE TRABALHO:

   ```bash
   ./src/dados/csv/remuneracao/dwsiape/AAAAMM
8. Renomeie o arquivo _.env.example_ para _.env_ e defina as credenciais de acesso.

8. Renomeie o arquivo _queriesexample.py_ para _queries.py_ e defina as regras de consulta a banco de dados.

9. Inicie o _Juyter Notebook_ a partir da linha de comando:
    ```bash
    jupyter notebook
10. De um navegador da web, acesse o endereço *<http://localhost:8888>*

11. Acesse o arquivo _src/Controle de Folha.ipynb_

12. Edite as constantes de definição do mês de trabalho no arquivo _src/Controle de Folha.ipynb_:

    ```bash
    MES_REFERENCIA = "AAAAMM"
    DATA_REFERENCIA_INICIO_FOLHA = "AAAA-MM-DD"
    DATA_REFERENCIA_TERMINO_FOLHA = "AAAA-MM-DD"
13. Execute o arquivo

14.  Analise os gráficos e o relatório final gerado para obter insights sobre os pagamentos de pessoal.

Certifique-se de revisar os comentários explicativos fornecidos ao longo do código para uma compreensão mais detalhada de cada etapa.

Observação: Este sistema foi desenvolvido para o contexto do Corpo de Bombeiros Militar do Distrito Federal e pode necessitar de adaptações para outros cenários.
