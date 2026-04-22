# Trabalho 4 de 11 — Testes de Componente em Python

Este projeto contém:

- código-fonte em `src/`
- testes de unidade prontos em `tests/unit/`
- pasta `tests/components/` vazia para os alunos implementarem os testes de componente

## Como executar

Crie e ative um ambiente virtual:

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rode os testes de unidade:

```bash
pytest tests/unit
```

Rode todos os testes:

```bash
pytest
```

Os alunos devem implementar os testes em:

```text
tests/components/
```
