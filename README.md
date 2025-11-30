# Projeto-Integrado-Clinica-Vida+
🏥 Sistema de Atendimento Clínico — Python + Tkinter
📚 Projeto acadêmico desenvolvido para a disciplina do curso de Análise e Desenvolvimento de Sistemas.

Este repositório contém um projeto desenvolvido para a faculdade, como parte das atividades práticas da disciplina de desenvolvimento de software. O objetivo é criar um sistema funcional de atendimento clínico utilizando Python e uma interface gráfica feita com Tkinter e CustomTkinter, proporcionando uma interação mais amigável para o usuário.

O sistema reproduz o fluxo real de atendimento em uma clínica, permitindo o gerenciamento de pacientes, filas e regras específicas para consulta normal ou emergência.

✅ Principais Funcionalidades
👤 Cadastro de Pacientes

Registro de informações básicas

Armazenamento em lista estruturada

Validações simples para garantir consistência

🩺 Gerenciamento de Fila de Atendimento

Inclusão e remoção de pacientes

Fila classificada por tipo de atendimento

Regras de prioridade respeitadas

⚙️ Lógica de Decisão do Atendimento
✔ Consulta Normal

O paciente será atendido se:

Possui agendamento, documentos ok e médico disponível
OU

Possui pagamentos em dia, documentos ok e médico disponível

✔ Emergência

Será atendido se:

Existe médico disponível
E

O paciente possui documentos ou pagamentos em dia

🎨 Interface Gráfica — Tkinter + CustomTkinter

Layout visual moderno

Botões personalizados

Campos bem organizados

Fluxo intuitivo para o usuário

🔧 Tecnologias Utilizadas

Python 3

Tkinter

CustomTkinter

Datetime

🎯 Objetivo Geral do Projeto

Proporcionar um entendimento prático sobre:

Estruturação de dados em Python

Criação de interfaces gráficas

Aplicação de regras de negócio

Organização de sistemas desktop

Raciocínio lógico aplicado a processos reais
