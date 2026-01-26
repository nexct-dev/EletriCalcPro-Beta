# ============================================================
# ELETRICALC PRO — CÓDIGO COMPLETO REESCRITO
# Versão: 2.1.0
# Norma: ABNT NBR 5410
# Autor: Projeto Profissional (Engenharia Elétrica)
# ============================================================

"""
Este arquivo consolida TODO o software EletriCalc Pro em um único
código-fonte, organizado por seções lógicas, pronto para:
- Uso profissional
- Auditoria técnica
- Evolução modular futura

Tecnologias:
- Python 3.10+
- Streamlit (UI)
- SQLAlchemy (ORM)
- SQLite (persistência)
- ReportLab (PDF)
"""

# ============================================================
# 1. IMPORTAÇÕES
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np
import hashlib
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

# ============================================================
# 2. CONFIGURAÇÕES GERAIS
# ============================================================
APP_NAME = "EletriCalc Pro"
APP_VERSION = "2.1.0"
VERSAO_NBR = "ABNT NBR 5410:2004 + Emendas"
DB_FILE = "projetos_eletricos.db"

# ============================================================
# 3. BANCO DE DADOS (ORM)
# ============================================================
Base = declarative_base()
engine = create_engine(f"sqlite:///{DB_FILE}")
Session = sessionmaker(bind=engine)

class Projeto(Base):
    __tablename__ = "projetos"
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True, nullable=False)
    cliente = Column(String)
    tipo = Column(String)
    criado_em = Column(DateTime, default=datetime.utcnow)
    revisoes = relationship("Revisao", back_populates="projeto")

class Revisao(Base):
    __tablename__ = "revisoes"
    id = Column(Integer, primary_key=True)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    versao = Column(String)
    data = Column(DateTime, default=datetime.utcnow)
    responsavel = Column(String)
    versao_nbr = Column(String)
    versao_motor = Column(String)
    hash_projeto = Column(String)
    projeto = relationship("Projeto", back_populates="revisoes")
    circuitos = relationship("Circuito", back_populates="revisao")

class Circuito(Base):
    __tablename__ = "circuitos"
    id = Column(Integer, primary_key=True)
    revisao_id = Column(Integer, ForeignKey("revisoes.id"))
    nome = Column(String)
    descricao = Column(String)
    corrente = Column(Float)
    tensao = Column(Float)
    fases = Column(Integer)
    comprimento = Column(Float)
    secao_calculada = Column(Float)
    disjuntor = Column(Float)
    queda_percentual = Column(Float)
    conforme = Column(Boolean)
    revisao = relationship("Revisao", back_populates="circuitos")

Base.metadata.create_all(engine)

# ============================================================
# 4. TABELAS NBR 5410 (SIMPLIFICADAS)
# ============================================================
AMPACIDADE_PVC_CU = {
    1.5: 15, 2.5: 21, 4: 28, 6: 36, 10: 50,
    16: 68, 25: 89, 35: 110, 50: 134
}

FATOR_TEMPERATURA = {
    30: 1.00, 35: 0.94, 40: 0.87, 45: 0.79, 50: 0.71
}

FATOR_AGRUPAMENTO = {
    1: 1.00, 2: 0.80, 3: 0.70, 4: 0.65, 5: 0.60
}

# ============================================================
# 5. MOTOR DE CÁLCULO
# ============================================================
def dimensionar_circuito(ib, comprimento, tensao, fases, temp, agrup):
    alertas = []
    f_temp = FATOR_TEMPERATURA.get(temp, 0.87)
    f_agrup = FATOR_AGRUPAMENTO.get(agrup, 0.70)

    secao_escolhida = None
    for secao, iz in AMPACIDADE_PVC_CU.items():
        iz_corr = iz * f_temp * f_agrup
        if iz_corr >= ib:
            secao_escolhida = secao
            break

    if secao_escolhida is None:
        raise ValueError("Corrente acima da capacidade máxima")

    rho = 0.0175
    fator_fases = 2 if fases == 1 else np.sqrt(3)
    queda = (fator_fases * rho * comprimento * ib) / (secao_escolhida * tensao) * 100

    conforme = queda <= 4.0
    if not conforme:
        alertas.append("Queda de tensão acima do permitido")

    return {
        "secao": secao_escolhida,
        "disjuntor": round(ib * 1.25, 1),
        "queda": round(queda, 2),
        "conforme": conforme,
        "alertas": alertas
    }

# ============================================================
# 6. GERADOR DE PDF
# ============================================================
def gerar_pdf(projeto, revisao, circuitos):
    nome_arquivo = f"{projeto.nome}_{revisao.versao}.pdf"
    doc = SimpleDocTemplate(nome_arquivo)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"<b>{APP_NAME}</b>", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Projeto: {projeto.nome}", styles['Normal']))
    story.append(Paragraph(f"Cliente: {projeto.cliente}", styles['Normal']))
    story.append(Paragraph(f"Norma: {VERSAO_NBR}", styles['Normal']))
    story.append(Spacer(1, 12))

    tabela = [["Circuito", "Corrente", "Seção", "Disjuntor", "Queda", "Conforme"]]
    for c in circuitos:
        tabela.append([
            c.nome,
            f"{c.corrente} A",
            f"{c.secao_calculada} mm²",
            f"{c.disjuntor} A",
            f"{c.queda_percentual} %",
            "SIM" if c.conforme else "NÃO"
        ])

    story.append(Table(tabela))
    doc.build(story)
    return nome_arquivo

# ============================================================
# 7. INTERFACE STREAMLIT
# ============================================================
st.set_page_config(page_title=APP_NAME, layout="wide")
st.title("⚡ EletriCalc Pro")
st.caption("Dimensionamento elétrico conforme NBR 5410")

session = Session()

# Sidebar — Projeto
st.sidebar.header("Projeto")
projetos = session.query(Projeto).all()
nome_proj = st.sidebar.selectbox("Selecionar", [p.nome for p in projetos] + ["Novo"])

if nome_proj == "Novo":
    nome = st.sidebar.text_input("Nome do projeto")
    cliente = st.sidebar.text_input("Cliente")
    tipo = st.sidebar.selectbox("Tipo", ["Residencial", "Comercial", "Industrial"])
    if st.sidebar.button("Criar"):
        p = Projeto(nome=nome, cliente=cliente, tipo=tipo)
        session.add(p)
        session.commit()
        st.experimental_rerun()
else:
    projeto = session.query(Projeto).filter_by(nome=nome_proj).first()

    st.subheader("Circuitos")
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame({
            "Nome": ["C1"],
            "Corrente": [10.0],
            "Comprimento": [20.0],
            "Fases": [1]
        })

    df = st.data_editor(st.session_state.df, num_rows="dynamic")
    st.session_state.df = df

    if st.button("Calcular"):
        circuitos = []
        payload = str(df.to_dict()).encode()
        hash_proj = hashlib.sha256(payload).hexdigest()

        revisao = Revisao(
            projeto_id=projeto.id,
            versao=f"R{len(projeto.revisoes)}",
            responsavel="Eng. Responsável",
            versao_nbr=VERSAO_NBR,
            versao_motor=APP_VERSION,
            hash_projeto=hash_proj
        )
        session.add(revisao)
        session.commit()

        for _, r in df.iterrows():
            res = dimensionar_circuito(r["Corrente"], r["Comprimento"], 220, r["Fases"], 30, 1)
            c = Circuito(
                revisao_id=revisao.id,
                nome=r["Nome"],
                corrente=r["Corrente"],
                tensao=220,
                fases=r["Fases"],
                comprimento=r["Comprimento"],
                secao_calculada=res["secao"],
                disjuntor=res["disjuntor"],
                queda_percentual=res["queda"],
                conforme=res["conforme"]
            )
            session.add(c)
            circuitos.append(c)

        session.commit()
        pdf = gerar_pdf(projeto, revisao, circuitos)
        st.success("Projeto calculado e salvo")
        st.download_button("Baixar PDF", open(pdf, "rb"), file_name=pdf)

session.close()

# ============================================================
# FIM DO SOFTWARE
# ============================================================
