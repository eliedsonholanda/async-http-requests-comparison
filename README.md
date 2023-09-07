# Comparativo entre Requisições Síncronas e Assíncronas

Um exemplo simples de como usar [asyncio](https://docs.python.org/3/library/asyncio.html) e [httpx](https://github.com/encode/httpx) para realizar requisições HTTP de forma síncrona e assíncrona, permitindo a comparação de desempenho entre os dois métodos.

## Instalação

Certifique-se de ter o python instalado em seu sistema. Você também precisa instalar a biblioteca `httpx`. Você pode fazer isso usando o seguinte comando:

```bash
pip install httpx
```

## Uso

Para executar o exemplo e medir o tempo de execução das requisições síncronas e assíncronas, basta executar o arquivo `main.py`:

```bash
python main.py
```

Isso executará ambos os métodos e exibirá o tempo que cada abordagem levou para completar.