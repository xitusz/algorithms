# Algorithms
[4/6] [Ciência da Computação](https://github.com/xitusz/Trybe/tree/main/04_Ci%C3%AAncia-da-Computa%C3%A7%C3%A3o)

---

## Sumário

- [Contexto](#contexto)
- [Habilidades Desenvolvidas](#habilidades-desenvolvidas)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Clonando Repositório](#clonando-repositório)
- [Instalando Dependências](#instalando-dependências)
- [Executando Aplicação](#executando-aplicação)
- [Executando Testes](#executando-testes)

---

## Contexto

* Projeto desenvolvido para colocar em prática conhecimentos adquiridos em algoritmos

---

## Habilidades Desenvolvidas

* Lógica;
* Capacidade de interpretação de problemas;
* Capacidade de interpretação de um código legado;
* Capacidade de otimizar a resolução de problemas e;
* Resolver problemas/Otimizar algoritmos sob pressão.

---

## Tecnologias Utilizadas

* Python

---

## Clonando Repositório:

* Clone o repositório
  ```sh
    git clone git@github.com:xitusz/algorithms.git
  ```

---

## Instalando Dependências

* Entre na pasta do repositório que você clonou:
  ```sh
    cd algorithms
  ```

* Crie o ambiente virtual
  ```sh
    python3 -m venv .venv && source .venv/bin/activate
  ```

* Instale as dependências
  ```sh
    python3 -m pip install -r dev-requirements.txt
  ```

* Se aparecer algum erro relacionado a 'wheel', instale-o
  ```sh
    python3 -m pip install wheel && python3 -m pip install -r dev-requirements.txt
  ```

---

## Executando Aplicação

* Entre na pasta challenges:
  ```sh
    cd algorithms/challenges
  ```

* Crie o ambiente virtual
  ```sh
    python3 -m venv .venv && source .venv/bin/activate
  ```

* Execute os challenges desejados
  ```sh
    python3 challenge_anagrams.py

    python3 challenge_palindromes_recursive.py

    python3 challenge_study_schedule.py
  ```

---

## Executando Testes

* Testes removidos pelo fato de terem sido criados pela [Trybe](https://www.betrybe.com/)

---
