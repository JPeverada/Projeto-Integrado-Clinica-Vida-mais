import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

# Configuração inicial
ctk.set_appearance_mode("dark")  # ou "light"
ctk.set_default_color_theme("blue")

# Lista para armazenar pacientes
pacientes = [
    {"nome": "Ana Silva", "data_nascimento": "12/03/1990", "sexo": "Feminino", "telefone": "11987654321", "cpf": "123.456.789-00", "endereco": "Rua das Flores, 123 - São Paulo/SP", "mensalidade_paga": True},
    {"nome": "Carlos Pereira", "data_nascimento": "25/07/1985", "sexo": "Masculino", "telefone": "11912345678", "cpf": "234.567.890-11", "endereco": "Av. Principal, 456 - Rio de Janeiro/RJ", "mensalidade_paga": False},
    {"nome": "Beatriz Souza", "data_nascimento": "09/11/2002", "sexo": "Feminino", "telefone": "11999887766", "cpf": "345.678.901-22", "endereco": "Travessa da Paz, 789 - Belo Horizonte/MG", "mensalidade_paga": True},
    {"nome": "João Mendes", "data_nascimento": "30/01/1978", "sexo": "Masculino", "telefone": "11911223344", "cpf": "456.789.012-33", "endereco": "Rua do Comércio, 321 - Porto Alegre/RS", "mensalidade_paga": False},
    {"nome": "Mariana Oliveira", "data_nascimento": "18/05/1999", "sexo": "Feminino", "telefone": "11922334455", "cpf": "567.890.123-44", "endereco": "Alameda dos Anjos, 654 - Salvador/BA", "mensalidade_paga": True},
]

# Lista para armazenar médicos
medicos = [
    {"nome": "Dr. Roberto Santos", "especialidade": "Cardiologia", "crm": "12345-SP", "telefone": "11988887777", "disponivel": True},
    {"nome": "Dra. Maria Oliveira", "especialidade": "Pediatria", "crm": "54321-SP", "telefone": "11977776666", "disponivel": True},
    {"nome": "Dr. Carlos Mendes", "especialidade": "Ortopedia", "crm": "98765-SP", "telefone": "11966665555", "disponivel": False},
    {"nome": "Dra. Ana Costa", "especialidade": "Dermatologia", "crm": "13579-SP", "telefone": "11955554444", "disponivel": True},
    {"nome": "Dr. Paulo Rodrigues", "especialidade": "Neurologia", "crm": "24680-SP", "telefone": "11944443333", "disponivel": True},
]

# Criação da janela principal
janela = ctk.CTk()
janela.title("Sistema da Clínica Vida+")
janela.geometry("1500x800")

# -----------------------------
# Funções Principais
# -----------------------------
def limpar_tela():
    for widget in main_frame.winfo_children():
        widget.destroy()

def tela_inicial():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Clínica Vida+", font=("Arial", 26, "bold"))
    titulo.pack(pady=20)

    texto = (
        "Bem-vindo ao sistema da Clínica Vida+!\n\n"
        "Aqui cuidamos da sua saúde com atenção e tecnologia.\n"
        "Utilize o menu ao lado para gerenciar pacientes,\n"
        "médicos, consultar estatísticas e manter o histórico atualizado."
    )

    descricao = ctk.CTkLabel(main_frame, text=texto, font=("Arial", 16), justify="center")
    descricao.pack(pady=30)

def cadastrar_paciente():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Cadastrar Paciente", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    # Campo nome
    nome_label = ctk.CTkLabel(main_frame, text="Nome Completo:")
    nome_label.pack()
    nome_entry = ctk.CTkEntry(main_frame, width=300)
    nome_entry.pack(pady=5)
    
    # Campo data nascimento
    data_label = ctk.CTkLabel(main_frame, text="Data de Nascimento (dd/mm/aaaa):")
    data_label.pack()
    data_entry = ctk.CTkEntry(main_frame, width=250)
    data_entry.pack(pady=5)

    # Campo cpf
    cpf_label = ctk.CTkLabel(main_frame, text="CPF (xxx.xxx.xxx-xx):")
    cpf_label.pack()
    cpf_entry = ctk.CTkEntry(main_frame, width=250)
    cpf_entry.pack(pady=5)

    # Campo telefone
    tele_label = ctk.CTkLabel(main_frame, text="Telefone (DDD + Número):")
    tele_label.pack()
    tele_entry = ctk.CTkEntry(main_frame, width=250)
    tele_entry.pack(pady=5)

    # Campo endereço
    endereco_label = ctk.CTkLabel(main_frame, text="Endereço Completo:")
    endereco_label.pack()
    endereco_entry = ctk.CTkEntry(main_frame, width=350)
    endereco_entry.pack(pady=5)

    # Campo sexo (radiobuttons)
    sexo_label = ctk.CTkLabel(main_frame, text="Sexo:")
    sexo_label.pack(pady=5)

    sexo_var = ctk.StringVar(value="Masculino")
    sexo_masc = ctk.CTkRadioButton(main_frame, text="Masculino", variable=sexo_var, value="Masculino")
    sexo_fem = ctk.CTkRadioButton(main_frame, text="Feminino", variable=sexo_var, value="Feminino")
    sexo_masc.pack()
    sexo_fem.pack()

    # Campo mensalidade paga (checkbox)
    mensalidade_var = ctk.BooleanVar(value=False)
    mensalidade_check = ctk.CTkCheckBox(main_frame, text="Mensalidade Paga", variable=mensalidade_var)
    mensalidade_check.pack(pady=10)

    def salvar():
        nome = nome_entry.get().strip()
        data_nasc = data_entry.get().strip()
        cpf = cpf_entry.get().strip()
        telefone = tele_entry.get().strip()
        endereco = endereco_entry.get().strip()
        sexo = sexo_var.get()
        mensalidade_paga = mensalidade_var.get()

        if not nome or not data_nasc or not cpf or not telefone or not endereco or not sexo:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if len(data_nasc) != 10 or data_nasc[2] != "/" or data_nasc[5] != "/":
            messagebox.showerror("Erro","Data inválida. Use o formato dd/mm/aaaa!")
            return
        
        if len(cpf) != 14 or cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
            messagebox.showerror("Erro","CPF inválido. Use o formato xxx.xxx.xxx-xx!")
            return
               
        if len(telefone) != 12:
            messagebox.showerror("Erro","Telefone inválido!")
            return

        paciente = {
            "nome": nome, 
            "data_nascimento": data_nasc, 
            "cpf": cpf, 
            "telefone": telefone, 
            "endereco": endereco,
            "sexo": sexo, 
            "mensalidade_paga": mensalidade_paga
        }
        pacientes.append(paciente)
        messagebox.showinfo("Sucesso","Paciente cadastrado com sucesso!")
        tela_inicial()

    botao_salvar = ctk.CTkButton(main_frame, text="Salvar", fg_color="#2e8b57", command=salvar)
    botao_salvar.pack(pady=20)

def cadastrar_medico():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Cadastrar Médico", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    # Campo nome
    nome_label = ctk.CTkLabel(main_frame, text="Nome Completo:")
    nome_label.pack()
    nome_entry = ctk.CTkEntry(main_frame, width=300)
    nome_entry.pack(pady=5)

    # Campo especialidade
    especialidade_label = ctk.CTkLabel(main_frame, text="Especialidade:")
    especialidade_label.pack()
    especialidade_entry = ctk.CTkEntry(main_frame, width=250)
    especialidade_entry.pack(pady=5)

    # Campo CRM
    crm_label = ctk.CTkLabel(main_frame, text="CRM (com UF):")
    crm_label.pack()
    crm_entry = ctk.CTkEntry(main_frame, width=200, placeholder_text="Ex: 12345-SP")
    crm_entry.pack(pady=5)

    # Campo telefone
    tele_label = ctk.CTkLabel(main_frame, text="Telefone (DDD + Número):")
    tele_label.pack()
    tele_entry = ctk.CTkEntry(main_frame, width=250)
    tele_entry.pack(pady=5)

    # Campo disponibilidade (checkbox)
    disponivel_var = ctk.BooleanVar(value=True)
    disponivel_check = ctk.CTkCheckBox(main_frame, text="Disponível para consultas", variable=disponivel_var)
    disponivel_check.pack(pady=10)

    def salvar_medico():
        nome = nome_entry.get().strip()
        especialidade = especialidade_entry.get().strip()
        crm = crm_entry.get().strip()
        telefone = tele_entry.get().strip()
        disponivel = disponivel_var.get()

        if not nome or not especialidade or not crm or not telefone:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Verificar se CRM já existe
        for medico in medicos:
            if medico["crm"] == crm:
                messagebox.showerror("Erro", "CRM já cadastrado no sistema!")
                return

        if len(telefone) != 12:
            messagebox.showerror("Erro", "Telefone inválido! Use o formato DDD + Número (12 dígitos)")
            return

        medico = {
            "nome": nome,
            "especialidade": especialidade,
            "crm": crm,
            "telefone": telefone,
            "disponivel": disponivel
        }
        medicos.append(medico)
        messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")
        tela_inicial()

    botao_salvar = ctk.CTkButton(main_frame, text="Salvar Médico", fg_color="#2e8b57", command=salvar_medico)
    botao_salvar.pack(pady=20)

def ver_medicos_disponiveis():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Médicos Disponíveis", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    # Filtrar médicos disponíveis
    medicos_disponiveis = [m for m in medicos if m["disponivel"]]
    medicos_indisponiveis = [m for m in medicos if not m["disponivel"]]

    if not medicos_disponiveis and not medicos_indisponiveis:
        ctk.CTkLabel(main_frame, text="Nenhum médico cadastrado no sistema.").pack(pady=10)
        return

    # Médicos disponíveis
    if medicos_disponiveis:
        ctk.CTkLabel(main_frame, text="✅ MÉDICOS DISPONÍVEIS:", 
                    font=("Arial", 16, "bold"), text_color="#2e8b57").pack(pady=10)
        
        frame_disponiveis = ctk.CTkScrollableFrame(main_frame, width=650, height=200)
        frame_disponiveis.pack(pady=10, padx=20, fill="both", expand=True)

        for medico in medicos_disponiveis:
            texto = f"• {medico['nome']} - {medico['especialidade']} - CRM: {medico['crm']} - Tel: {medico['telefone']}"
            label_medico = ctk.CTkLabel(frame_disponiveis, text=texto, text_color="#2e8b57")
            label_medico.pack(pady=3, anchor="w")

    # Médicos indisponíveis
    if medicos_indisponiveis:
        ctk.CTkLabel(main_frame, text="⏸️ MÉDICOS INDISPONÍVEIS:", 
                    font=("Arial", 16, "bold"), text_color="#ff6b6b").pack(pady=(20, 10))
        
        frame_indisponiveis = ctk.CTkScrollableFrame(main_frame, width=650, height=150)
        frame_indisponiveis.pack(pady=10, padx=20, fill="both", expand=True)

        for medico in medicos_indisponiveis:
            texto = f"• {medico['nome']} - {medico['especialidade']} - CRM: {medico['crm']}"
            label_medico = ctk.CTkLabel(frame_indisponiveis, text=texto, text_color="#ff6b6b")
            label_medico.pack(pady=3, anchor="w")

    # Estatísticas rápidas
    ctk.CTkLabel(main_frame, text=f"📊 Resumo: {len(medicos_disponiveis)} disponíveis de {len(medicos)} médicos cadastrados",
                font=("Arial", 14)).pack(pady=20)

def listar_todos_medicos():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Todos os Médicos Cadastrados", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    if not medicos:
        ctk.CTkLabel(main_frame, text="Nenhum médico cadastrado no sistema.").pack(pady=10)
        return

    frame_scroll = ctk.CTkScrollableFrame(main_frame, width=700, height=300)
    frame_scroll.pack(pady=10, padx=20, fill="both", expand=True)

    for medico in medicos:
        status = "✅ Disponível" if medico["disponivel"] else "⏸️ Indisponível"
        cor_status = "#2e8b57" if medico["disponivel"] else "#ff6b6b"
        
        # Frame para cada médico
        medico_frame = ctk.CTkFrame(frame_scroll)
        medico_frame.pack(pady=5, fill="x", padx=5)

        info_text = f"{medico['nome']} | {medico['especialidade']} | CRM: {medico['crm']} | Tel: {medico['telefone']} | Status: {status}"
        
        label_info = ctk.CTkLabel(medico_frame, text=info_text, text_color=cor_status)
        label_info.pack(side="left", padx=10, pady=5)

        # Botão para alterar disponibilidade
        novo_status = not medico["disponivel"]
        texto_botao = "Tornar Indisponível" if medico["disponivel"] else "Tornar Disponível"
        cor_botao = "#ff6b6b" if medico["disponivel"] else "#2e8b57"
        
        btn_alterar = ctk.CTkButton(medico_frame, text=texto_botao, 
                                  fg_color=cor_botao, hover_color="#3cb371" if not medico["disponivel"] else "#a83232",
                                  width=140, height=25,
                                  command=lambda m=medico, ns=novo_status: alterar_disponibilidade_medico(m, ns))
        btn_alterar.pack(side="right", padx=10, pady=5)

def alterar_disponibilidade_medico(medico, novo_status):
    """Altera a disponibilidade de um médico"""
    status_text = "disponível" if novo_status else "indisponível"
    
    resposta = messagebox.askyesno(
        "Alterar Disponibilidade",
        f"Alterar status do médico:\n\n"
        f"{medico['nome']} - {medico['especialidade']}\n\n"
        f"Tornar {status_text.upper()}?"
    )
    
    if resposta:
        medico["disponivel"] = novo_status
        messagebox.showinfo("Sucesso", f"Status do médico {medico['nome']} alterado para {status_text}!")
        listar_todos_medicos()

def ver_estatisticas():
    limpar_tela()
    titulo = ctk.CTkLabel(main_frame, text="Estatísticas Gerais", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    # Estatísticas de pacientes
    total_pacientes = len(pacientes)
    masc = sum(1 for p in pacientes if p["sexo"] == "Masculino")
    fem = sum(1 for p in pacientes if p["sexo"] == "Feminino")
    mensalidade_paga = sum(1 for p in pacientes if p["mensalidade_paga"])
    mensalidade_pendente = total_pacientes - mensalidade_paga

    # Estatísticas de médicos
    total_medicos = len(medicos)
    medicos_disponiveis = sum(1 for m in medicos if m["disponivel"])
    medicos_indisponiveis = total_medicos - medicos_disponiveis

    ctk.CTkLabel(main_frame, text="👥 ESTATÍSTICAS DE PACIENTES:", 
                font=("Arial", 16, "bold")).pack(pady=(10, 5))
    
    ctk.CTkLabel(main_frame, text=f"• Total de pacientes: {total_pacientes}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Masculino: {masc}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Feminino: {fem}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Mensalidades pagas: {mensalidade_paga}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Mensalidades pendentes: {mensalidade_pendente}").pack(pady=2)

    # Cálculo de idades dos pacientes (se houver pacientes)
    if pacientes:
        try:
            idades = []
            pacientes_com_idade = []
            
            for p in pacientes:
                data_nasc = datetime.strptime(p["data_nascimento"], "%d/%m/%Y").date()
                hoje = datetime.now().date()
                idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
                idades.append(idade)
                # Criar uma cópia do paciente com a idade calculada
                paciente_com_idade = p.copy()
                paciente_com_idade["idade"] = idade
                paciente_com_idade["data_obj"] = data_nasc
                pacientes_com_idade.append(paciente_com_idade)

            # Calcular idade média
            idade_media = sum(idades) / len(idades)
            ctk.CTkLabel(main_frame, text=f"• Idade média dos pacientes: {idade_media:.1f} anos").pack(pady=2)

            # Encontrar paciente mais novo e mais velho
            if pacientes_com_idade:
                paciente_mais_velho = min(pacientes_com_idade, key=lambda x: x["data_obj"])
                paciente_mais_novo = max(pacientes_com_idade, key=lambda x: x["data_obj"])
                
                # Calcular idades exatas
                idade_mais_novo = paciente_mais_novo["idade"]
                idade_mais_velho = paciente_mais_velho["idade"]
                
                ctk.CTkLabel(main_frame, text=f"• Paciente mais novo: {paciente_mais_novo['nome']} ({idade_mais_novo} anos)").pack(pady=2)
                ctk.CTkLabel(main_frame, text=f"• Paciente mais velho: {paciente_mais_velho['nome']} ({idade_mais_velho} anos)").pack(pady=2)

        except Exception as e:
            ctk.CTkLabel(main_frame, text="• Erro ao calcular idades e idades extremas").pack(pady=2)
            print(f"Erro: {e}")

    # Estatísticas de médicos
    ctk.CTkLabel(main_frame, text="👨‍⚕️ ESTATÍSTICAS DE MÉDICOS:", 
                font=("Arial", 16, "bold")).pack(pady=(20, 5))
    
    ctk.CTkLabel(main_frame, text=f"• Total de médicos: {total_medicos}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Médicos disponíveis: {medicos_disponiveis}").pack(pady=2)
    ctk.CTkLabel(main_frame, text=f"• Médicos indisponíveis: {medicos_indisponiveis}").pack(pady=2)

    # Estatística de especialidades médicas
    if medicos:
        especialidades = {}
        for medico in medicos:
            esp = medico["especialidade"]
            especialidades[esp] = especialidades.get(esp, 0) + 1
        
        especialidade_mais_comum = max(especialidades.items(), key=lambda x: x[1])
        ctk.CTkLabel(main_frame, text=f"• Especialidade mais comum: {especialidade_mais_comum[0]} ({especialidade_mais_comum[1]} médicos)").pack(pady=2)

def buscar_paciente():
    limpar_tela()
    
    titulo = ctk.CTkLabel(main_frame, text="Buscar Paciente", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)
    
    nome_label = ctk.CTkLabel(main_frame, text="Digite o nome:")
    nome_label.pack()
    nome_entry = ctk.CTkEntry(main_frame, width=250)
    nome_entry.pack(pady=5)

    def buscar():
        nome = nome_entry.get().strip().lower()
        resultados = [p for p in pacientes if nome in p["nome"].lower()]

        if resultados:
            # Mostrar informações completas incluindo mensalidade
            msg = ""
            for p in resultados:
                status_mensalidade = "PAGA" if p["mensalidade_paga"] else "PENDENTE"
                msg += f"{p['nome']} - {p['data_nascimento']} - {p['sexo']}\n"
                msg += f"Endereço: {p['endereco']}\n"
                msg += f"Mensalidade: {status_mensalidade}\n\n"
            messagebox.showinfo("Resultados", msg)
        else:
            messagebox.showinfo("Nenhum resultado", "Paciente não encontrado.")
                
    ctk.CTkButton(main_frame, text="Buscar", command=buscar).pack(pady=10)

def listar_pacientes():
    limpar_tela()
    
    titulo = ctk.CTkLabel(main_frame, text="Lista de Pacientes", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)
    
    if not pacientes:
        ctk.CTkLabel(main_frame, text="Nenhum paciente cadastrado.").pack(pady=10)
    else:
        # Criar um frame com scroll para a lista de pacientes
        frame_scroll = ctk.CTkScrollableFrame(main_frame, width=700, height=300)
        frame_scroll.pack(pady=10, padx=20, fill="both", expand=True)
        
        for p in pacientes:
            status_mensalidade = "✓ PAGA" if p["mensalidade_paga"] else "✗ PENDENTE"
            cor_status = "#2e8b57" if p["mensalidade_paga"] else "#ff6b6b"
            
            texto = f"Nome: {p['nome']} | Data Nasc.: {p['data_nascimento']} | Sexo: {p['sexo']} | Mensalidade: {status_mensalidade}"
            
            label_paciente = ctk.CTkLabel(frame_scroll, text=texto)
            label_paciente.pack(pady=3, anchor="w")
            
            # Destacar a mensalidade com cor
            label_endereco = ctk.CTkLabel(frame_scroll, text=f"Endereço: {p['endereco']}", text_color="gray")
            label_endereco.pack(pady=2, anchor="w")

def verificar_mensalidades():
    limpar_tela()
    
    titulo = ctk.CTkLabel(main_frame, text="Verificar Mensalidades", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)
    
    # Pacientes com mensalidade pendente
    pendentes = [p for p in pacientes if not p["mensalidade_paga"]]
    
    if not pendentes:
        ctk.CTkLabel(main_frame, text="✅ Todas as mensalidades estão em dia!", 
                    font=("Arial", 16), text_color="#2e8b57").pack(pady=20)
    else:
        ctk.CTkLabel(main_frame, text=f"⚠️ {len(pendentes)} paciente(s) com mensalidade pendente:", 
                    font=("Arial", 16), text_color="#ff6b6b").pack(pady=10)
        
        frame_scroll = ctk.CTkScrollableFrame(main_frame, width=600, height=250)
        frame_scroll.pack(pady=10, padx=20, fill="both", expand=True)
        
        for p in pendentes:
            texto = f"• {p['nome']} - Telefone: {p['telefone']} - CPF: {p['cpf']}"
            
            # Frame para cada paciente com botão de pagar
            paciente_frame = ctk.CTkFrame(frame_scroll)
            paciente_frame.pack(pady=5, fill="x", padx=5)
            
            label_pendente = ctk.CTkLabel(paciente_frame, text=texto, text_color="#ff6b6b")
            label_pendente.pack(side="left", padx=10, pady=5)
            
            # Botão para pagar mensalidade
            btn_pagar = ctk.CTkButton(paciente_frame, text="Pagar Mensalidade", 
                                    fg_color="#2e8b57", hover_color="#3cb371",
                                    width=120, height=25,
                                    command=lambda pat=p: pagar_mensalidade(pat))
            btn_pagar.pack(side="right", padx=10, pady=5)

def pagar_mensalidade(paciente):
    """Função para marcar a mensalidade como paga"""
    resposta = messagebox.askyesno(
        "Confirmar Pagamento",
        f"Confirmar pagamento da mensalidade para:\n\n"
        f"Paciente: {paciente['nome']}\n"
        f"CPF: {paciente['cpf']}\n\n"
        f"Deseja marcar como PAGA?"
    )
    
    if resposta:
        # Encontrar e atualizar o paciente na lista
        for p in pacientes:
            if p['cpf'] == paciente['cpf']:
                p['mensalidade_paga'] = True
                break
        
        messagebox.showinfo("Sucesso", f"Mensalidade de {paciente['nome']} marcada como PAGA!")
        # Atualizar a tela de mensalidades pendentes
        verificar_mensalidades()

def pagar_mensalidade_por_busca():
    """Tela para buscar paciente e pagar mensalidade"""
    limpar_tela()
    
    titulo = ctk.CTkLabel(main_frame, text="Pagar Mensalidade", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)
    
    # Frame de busca
    frame_busca = ctk.CTkFrame(main_frame)
    frame_busca.pack(pady=10, padx=20, fill="x")
    
    ctk.CTkLabel(frame_busca, text="Buscar Paciente para Pagamento:", font=("Arial", 14)).pack(pady=10)
    
    # Campo de busca por nome ou CPF
    ctk.CTkLabel(frame_busca, text="Nome ou CPF:").pack()
    busca_entry = ctk.CTkEntry(frame_busca, width=300, placeholder_text="Digite nome ou CPF do paciente")
    busca_entry.pack(pady=5)
    
    # Frame para resultados
    resultados_frame = ctk.CTkScrollableFrame(main_frame, width=600, height=200)
    resultados_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    def buscar_para_pagamento():
        # Limpar resultados anteriores
        for widget in resultados_frame.winfo_children():
            widget.destroy()
            
        termo = busca_entry.get().strip().lower()
        if not termo:
            messagebox.showwarning("Aviso", "Digite um nome ou CPF para buscar.")
            return
            
        resultados = [p for p in pacientes if termo in p["nome"].lower() or termo in p["cpf"]]
        
        if not resultados:
            ctk.CTkLabel(resultados_frame, text="Nenhum paciente encontrado.", text_color="gray").pack(pady=10)
            return
            
        for p in resultados:
            
            paciente_frame = ctk.CTkFrame(resultados_frame)
            paciente_frame.pack(pady=5, fill="x", padx=5)
            
            status_mensalidade = "✓ PAGA" if p["mensalidade_paga"] else "✗ PENDENTE"
            cor_status = "#2e8b57" if p["mensalidade_paga"] else "#ff6b6b"
            
            info_text = f"{p['nome']} | CPF: {p['cpf']} | Mensalidade: {status_mensalidade}"
            
            label_info = ctk.CTkLabel(paciente_frame, text=info_text, text_color=cor_status)
            label_info.pack(side="left", padx=10, pady=5)
            
            # Botão de pagamento (só mostra se estiver pendente)
            if not p["mensalidade_paga"]:
                btn_pagar = ctk.CTkButton(paciente_frame, text="Pagar Mensalidade", 
                                        fg_color="#2e8b57", hover_color="#3cb371",
                                        width=120, height=25,
                                        command=lambda pat=p: pagar_mensalidade(pat))
                btn_pagar.pack(side="right", padx=10, pady=5)
            else:
                label_pago = ctk.CTkLabel(paciente_frame, text="JÁ PAGO", 
                                        text_color="#2e8b57", font=("Arial", 12, "bold"))
                label_pago.pack(side="right", padx=10, pady=5)
    
    # Botão de busca
    ctk.CTkButton(frame_busca, text="Buscar", command=buscar_para_pagamento).pack(pady=10)

# -----------------------------
# Layout da interface
# -----------------------------
# Frame lateral (menu)
menu_frame = ctk.CTkFrame(janela, width=220, corner_radius=0)
menu_frame.pack(side="left", fill="y")

# Frame principal (conteúdo)
main_frame = ctk.CTkFrame(janela)
main_frame.pack(side="right", expand=True, fill="both")

# -----------------------------
# Botões do menu
# -----------------------------
titulo_menu = ctk.CTkLabel(menu_frame, text="MENU", font=("Arial", 20, "bold"))
titulo_menu.pack(pady=25)

b = ctk.CTkButton(menu_frame, text="Início", command=tela_inicial)
b.pack(pady=8, fill="x", padx=15)

# Seção Pacientes
ctk.CTkLabel(menu_frame, text="PACIENTES", font=("Arial", 14, "bold")).pack(pady=(10, 5))
b1 = ctk.CTkButton(menu_frame, text="Cadastrar Paciente", command=cadastrar_paciente)
b1.pack(pady=4, fill="x", padx=15)
b3 = ctk.CTkButton(menu_frame, text="Buscar Paciente", command=buscar_paciente)
b3.pack(pady=4, fill="x", padx=15)
b4 = ctk.CTkButton(menu_frame, text="Listar Pacientes", command=listar_pacientes)
b4.pack(pady=4, fill="x", padx=15)
b5 = ctk.CTkButton(menu_frame, text="Verificar Mensalidades", command=verificar_mensalidades)
b5.pack(pady=4, fill="x", padx=15)
b6 = ctk.CTkButton(menu_frame, text="Pagar Mensalidade", command=pagar_mensalidade_por_busca)
b6.pack(pady=4, fill="x", padx=15)

# Seção Médicos
ctk.CTkLabel(menu_frame, text="MÉDICOS", font=("Arial", 14, "bold")).pack(pady=(10, 5))
b7 = ctk.CTkButton(menu_frame, text="Cadastrar Médico", command=cadastrar_medico)
b7.pack(pady=4, fill="x", padx=15)
b8 = ctk.CTkButton(menu_frame, text="Médicos Disponíveis", command=ver_medicos_disponiveis)
b8.pack(pady=4, fill="x", padx=15)
b9 = ctk.CTkButton(menu_frame, text="Todos os Médicos", command=listar_todos_medicos)
b9.pack(pady=4, fill="x", padx=15)

# Seção Geral
ctk.CTkLabel(menu_frame, text="GERAL", font=("Arial", 14, "bold")).pack(pady=(10, 5))
b2 = ctk.CTkButton(menu_frame, text="Estatísticas", command=ver_estatisticas)
b2.pack(pady=4, fill="x", padx=15)

b_sair = ctk.CTkButton(menu_frame, text="Sair", fg_color="red", hover_color="#a83232", command=janela.destroy)
b_sair.pack(side="bottom", pady=20, fill="x", padx=15)

# Tela inicial ao abrir
tela_inicial()

# Loop principal
janela.mainloop()