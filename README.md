# 🏥 Trabalho Clínica - Testes de Componentes

## 📖 Descrição

Este projeto implementa um sistema simples de agendamento de consultas médicas em Python.

O sistema simula o funcionamento de uma clínica, incluindo:

* Controle de pacientes e médicos
* Agendamento de consultas
* Verificação de horários disponíveis
* Gerenciamento de fila de espera com reposição automática

---

## 🛠 Tecnologias

* Python
* Pytest

---

## 📂 Estrutura do Projeto

```bash
TRABALHO_CLINICA_COMPONENTES/
│
├── src/
│   └── código-fonte fornecido pelo professor
│
├── tests/
│   ├── unit/        # testes fornecidos pelo professor
│   └── components/  # testes desenvolvidos no trabalho
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Funcionamento

O sistema é dividido em:

* **Repositórios** → responsáveis por armazenar dados em memória
* **Serviço (ClinicService)** → responsável por aplicar regras de negócio, como validação de agendamentos e controle da fila de espera

---

## 🧪 Testes

* Os **testes unitários** foram fornecidos pelo professor
* O foco do trabalho é o desenvolvimento de **testes de componente**, validando o funcionamento integrado do sistema

---

## ▶️ Como executar

```bash
git clone https://github.com/kauesalazarcardoso/Trabalho-de-clinica-.git
cd Trabalho-de-clinica-
```

---

## 🧪 Rodar testes

```bash
pip install -r requirements.txt
pytest
```

---

## 🎓 Objetivo Acadêmico

Este trabalho tem como objetivo:

* Analisar um sistema já implementado
* Compreender testes unitários existentes
* Desenvolver testes de componente
* Aplicar boas práticas de testes automatizados

**Observação:**
Os códigos-base e os testes unitários foram fornecidos pelo professor para fins educacionais.
