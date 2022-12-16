# Projeto Job Insights 👮🏻‍♂️👩🏼‍🚒👷🏾

Consiste em uma aplicação web desenvolvida com Flask contendo informações a partir da análise de um conjunto de dados sobre empregos. As páginas inicial e de pesquisa por vaga foram desenvolvidas pela [Trybe](https://www.betrybe.com), utilizando as funções criadas e descritas a seguir para o funcionamento correto da filtragem dos dados. Mediante a estrutura já presente, foi desenvolvido a página de detalhes de uma vaga. 

<details>
  <summary><strong>Descrição das funções criadas:</strong></summary><br />

| Função | Descrição | Localização |
|---|---|---|
| `read` | Função recebe o caminho do arquivo `csv` e retorna os dados em uma lista de dicionários | `src/insights/jobs.py` |
| `get_unique_job_types` | A partir do caminho do arquivo, retorna todos os tipos de empregos | `src/insights/jobs.py` |
| `get_unique_industries` | A partir do caminho do arquivo, retorna todas as indústrias | `src/insights/industries.py` |
| `get_max_salary` | A partir do caminho do arquivo, retorna o maior salário presente | `src/insights/salaries.py` |
| `get_min_salary` | A partir do caminho do arquivo, retorna o menor salário presente | `src/insights/salaries.py` |
| `filter_by_job_type` | A partir de uma lista de dicionários, retorna uma lista filtrada pelo o tipo de emprego informado como parâmetro | `src/insights/jobs.py` |
| `filter_by_industry` | A partir de uma lista de dicionários, retorna uma lista filtrada pela indústria informada como parâmetro | `src/insights/industries.py` |
| `matches_salary_range` | A partir de um dicionário, retorna True ou False se o salário informado está dentro da faixa monetária | `src/insights/salaries.py` |
| `filter_by_salary_range` | A partir de uma lista de dicionários, utiliza a função `matches_salary_range` para filtrar as vagas com salário dentro da faixa | `src/insights/salaries.py` |
<br />
</details>

<details>
  <summary><strong>Descrição dos testes criados:</strong></summary><br />
 
| Teste | Descrição | Localização |
|---|---|---|
| `test_counter` | Implementação dos testes para função `count_ocurrences` | `tests/counter/test_counter.py` |
| `test_brazilian_jobs` | Implementação dos testes para função `read_brazilian_file` | `tests/brazilian/test_brazilian_jobs.py` |
| `test_sort_by_criteria` | Implementação dos testes para função `sort_by` | `tests/sorting/test_sorting.py` |
<br />
</details>



### Instruções

- Para rodar a aplicação localmente e os testes, realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências


Para rodar todos os testes:
<-- na raiz do projeto -->
python3 -m pytest

PAra rodar os testes individualmente:
<-- na raiz do projeto -->
python3 -m pytest -k test_counter
python3 -m pytest -k test_brazilian_jobs
python3 -m pytest -k test_sort_by_criteria

Para rodar a aplicação dockerizada:
<-- na raiz do projeto -->
docker-compose up -d // para subir o container
docker-compose down // para parar o container
```
