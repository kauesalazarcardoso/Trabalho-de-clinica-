# Trabalho Prático — Testes de Componente com `pytest`

## Tema
**Sistema de clínica médica com agendamento, cancelamento e fila de espera**

## Objetivo
Neste trabalho, vocês receberão um pequeno subsistema já implementado, com **testes de unidade prontos**. O trabalho do grupo é criar os **testes de componente**, verificando a colaboração real entre as classes do módulo.

## Estrutura geral do sistema
O sistema contém as seguintes classes:

- `DoctorRepository`
- `PatientRepository`
- `AppointmentRepository`
- `WaitlistRepository`
- `ClinicService`

## Regras de negócio

### Agendamento
Um paciente pode agendar uma consulta somente se:

- o paciente existir;
- o médico existir;
- o paciente não estiver bloqueado;
- o paciente não tiver pendência financeira;
- o paciente tiver menos de 2 consultas ativas;
- o horário solicitado estiver disponível;
- o paciente ainda não tiver consulta agendada com o mesmo médico no mesmo horário.

Quando o agendamento é realizado com sucesso:

- a consulta é registrada;
- se o paciente estava na fila de espera daquele médico e horário, sua entrada na fila deve ser removida.

### Fila de espera
Um paciente pode entrar na fila de espera somente se:

- o paciente existir;
- o médico existir;
- o paciente não estiver bloqueado;
- o horário solicitado já estiver ocupado;
- o paciente ainda não estiver na fila daquele médico e horário;
- o paciente não já tiver consulta confirmada com o mesmo médico no mesmo horário.

A fila deve obedecer a ordem de chegada.

### Cancelamento
Ao cancelar uma consulta:

- a consulta ativa correspondente deve existir;
- a consulta é removida;
- se houver alguém na fila de espera para aquele médico e horário, o primeiro da fila deve ser automaticamente agendado;
- se não houver fila de espera, o horário volta a ficar livre.

## O que deve ser implementado pelos alunos
Os alunos devem criar os testes em:

```text
tests/components/test_clinic_component.py
```

## Quantidade esperada
Criem **entre 10 e 12 testes de componente**.

## Cenários mínimos obrigatórios
1. agendamento com sucesso;
2. agendamento com paciente inexistente;
3. agendamento com médico inexistente;
4. agendamento bloqueado por paciente bloqueado;
5. agendamento bloqueado por pendência financeira;
6. agendamento bloqueado por limite de consultas ativas;
7. entrada na fila de espera com sucesso;
8. tentativa de entrada duplicada na fila;
9. cancelamento sem fila de espera;
10. cancelamento com promoção automática do primeiro da fila;
11. remoção da fila ao agendar um paciente que já estava aguardando;
12. sequência completa envolvendo agendamento, fila e cancelamento.

## Restrições
- não alterar os testes de unidade fornecidos;
- não reescrever a lógica das classes;
- usar as classes reais do subsistema;
- não usar banco de dados, rede ou Docker;
- os testes devem rodar com `pytest`.

## Critérios de avaliação
- cobertura dos cenários obrigatórios;
- qualidade e clareza dos testes;
- aderência ao conceito de teste de componente;
- organização do projeto;
- casos extras bem escolhidos.
