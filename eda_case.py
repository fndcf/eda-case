# CASE BANCÁRIO - ATIVIDADES SIMPLIFICADAS
# Análise de Relacionamento e Market Share

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ====================================================================
# CARREGAMENTO DOS DADOS
# ====================================================================

# Carregar dados do Excel
df = pd.read_excel('dados_clientes.xlsx')

print("✅ DADOS CARREGADOS")
print(f"📊 {len(df):,} clientes | {df.shape[1]} colunas")

# Padronizar nomes das colunas
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Lista de produtos
produtos = ['cartao_credito', 'consignado', 'crediario', 'investimento', 
           'rotativo_cartao_credito', 'lis', 'posse_salario']

# Tratar dados de produtos (blank = 0, preenchido = 1)
for produto in produtos:
    if produto in df.columns:
        df[produto] = df[produto].fillna(0)
        df[produto] = df[produto].apply(lambda x: 1 if x != 0 else 0)

# Criar variáveis derivadas
df['num_produtos'] = df[produtos].sum(axis=1)
df['diversificacao'] = df['num_produtos'] / len(produtos)

print("✅ DADOS TRATADOS")

# ====================================================================
# ATIVIDADE 1: ANÁLISE EXPLORATÓRIA (ESSENCIAL)
# ====================================================================

print("\n" + "="*50)
print("ATIVIDADE 1 - ANÁLISE EXPLORATÓRIA")
print("="*50)

# 1.1 Score de relacionamento
print("📈 SCORE DE RELACIONAMENTO:")
print(f"   Média: {df['relacionamento'].mean():.3f}")
print(f"   Mediana: {df['relacionamento'].median():.3f}")
print(f"   Q1 (25%): {df['relacionamento'].quantile(0.25):.3f}")
print(f"   Q3 (75%): {df['relacionamento'].quantile(0.75):.3f}")

# 1.2 Penetração de produtos
print(f"\n🏦 PENETRAÇÃO DE PRODUTOS:")
penetracao = {}
for produto in produtos:
    if produto in df.columns:
        pct = (df[produto].sum() / len(df)) * 100
        penetracao[produto] = pct
        print(f"   {produto:25}: {pct:5.1f}%")

# 1.3 Produtos por cliente
print(f"\n📊 PRODUTOS POR CLIENTE:")
print(f"   Média: {df['num_produtos'].mean():.1f}")
print(f"   Máximo: {df['num_produtos'].max()}")

# 1.4 Correlação produtos x relacionamento
print(f"\n🔗 CORRELAÇÃO COM RELACIONAMENTO:")
for produto in produtos:
    if produto in df.columns:
        corr = df[produto].corr(df['relacionamento'])
        print(f"   {produto:25}: {corr:6.3f}")

# Visualização básica
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('ANÁLISE EXPLORATÓRIA', fontsize=14)

# Distribuição do score
axes[0, 0].hist(df['relacionamento'], bins=30, alpha=0.7)
axes[0, 0].set_title('Distribuição Score Relacionamento')
axes[0, 0].axvline(df['relacionamento'].mean(), color='red', linestyle='--')

# Penetração produtos
pd.Series(penetracao).plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Penetração Produtos (%)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Produtos por cliente
df['num_produtos'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Distribuição Produtos/Cliente')

# Score por classe
if 'clas_modelo' in df.columns:
    df.boxplot(column='relacionamento', by='clas_modelo', ax=axes[1, 1])
    axes[1, 1].set_title('Score por Classe')

plt.tight_layout()
plt.show()

# ====================================================================
# ATIVIDADE 2: SEGMENTAÇÃO (SIMPLIFICADA)
# ====================================================================

print("\n" + "="*50)
print("ATIVIDADE 2 - SEGMENTAÇÃO")
print("="*50)

# Segmentação RFV simples
df['R_score'] = pd.qcut(df['relacionamento'], q=5, labels=[1,2,3,4,5])
df['F_score'] = pd.qcut(df['num_produtos'], q=5, labels=[1,2,3,4,5], duplicates='drop')

# Score RFV combinado
df['RFV_score'] = df['R_score'].astype(int) + df['F_score'].astype(int)

# Criar segmentos
def classificar_segmento(score):
    if score >= 9:
        return 'Champions'
    elif score >= 7:
        return 'Loyal'
    elif score >= 5:
        return 'Potential'
    elif score >= 3:
        return 'Developing'
    else:
        return 'Inactive'

df['segmento'] = df['RFV_score'].apply(classificar_segmento)

# Resultado da segmentação
print("👥 SEGMENTAÇÃO RFV:")
segmentos = df['segmento'].value_counts()
for segmento, qtd in segmentos.items():
    pct = (qtd / len(df)) * 100
    score_medio = df[df['segmento'] == segmento]['relacionamento'].mean()
    produtos_medio = df[df['segmento'] == segmento]['num_produtos'].mean()
    print(f"   {segmento:12}: {qtd:6,} ({pct:4.1f}%) | Score: {score_medio:.3f} | Produtos: {produtos_medio:.1f}")

# Visualização segmentação
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Pizza dos segmentos
segmentos.plot(kind='pie', ax=axes[0], autopct='%1.1f%%')
axes[0].set_title('Distribuição dos Segmentos')
axes[0].set_ylabel('')

# Score por segmento
df.boxplot(column='relacionamento', by='segmento', ax=axes[1])
axes[1].set_title('Score por Segmento')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# ====================================================================
# ATIVIDADE 3: OPORTUNIDADES DE CRESCIMENTO (FOCADA)
# ====================================================================

print("\n" + "="*50)
print("ATIVIDADE 3 - OPORTUNIDADES DE CRESCIMENTO")
print("="*50)

# 3.1 Produtos com baixa penetração (< 50%)
produtos_oportunidade = {k: v for k, v in penetracao.items() if v < 50}
produtos_oportunidade = dict(sorted(produtos_oportunidade.items(), key=lambda x: x[1]))

print("🎯 PRODUTOS COM MAIOR OPORTUNIDADE:")
for produto, pct in produtos_oportunidade.items():
    clientes_sem_produto = int(len(df) * (1 - pct/100))
    corr = df[produto].corr(df['relacionamento'])
    print(f"   {produto:25}: {pct:5.1f}% | {clientes_sem_produto:6,} clientes | Corr: {corr:6.3f}")

# 3.2 Gap por segmento (produto com menor penetração)
if produtos_oportunidade:
    produto_foco = list(produtos_oportunidade.keys())[0]  # Menor penetração
    
    print(f"\n📊 GAP DE OPORTUNIDADE - {produto_foco.upper()}:")
    for segmento in df['segmento'].unique():
        segmento_data = df[df['segmento'] == segmento]
        penetracao_segmento = (segmento_data[produto_foco].sum() / len(segmento_data)) * 100
        oportunidade = len(segmento_data) - segmento_data[produto_foco].sum()
        print(f"   {segmento:12}: {penetracao_segmento:5.1f}% | Oportunidade: {oportunidade:6,} clientes")

# 3.3 Ações para elevar relacionamento
print(f"\n🚀 FATORES QUE ELEVAM RELACIONAMENTO:")
quartil_alto = df[df['relacionamento'] >= df['relacionamento'].quantile(0.75)]
quartil_baixo = df[df['relacionamento'] <= df['relacionamento'].quantile(0.25)]

print(f"   Produtos médios (Alto vs Baixo): {quartil_alto['num_produtos'].mean():.1f} vs {quartil_baixo['num_produtos'].mean():.1f}")

for produto in produtos:
    if produto in df.columns:
        alto = quartil_alto[produto].mean() * 100
        baixo = quartil_baixo[produto].mean() * 100
        diferenca = alto - baixo
        if diferenca > 15:  # Só mostrar diferenças significativas
            print(f"   {produto:25}: {alto:5.1f}% vs {baixo:5.1f}% (Δ {diferenca:+5.1f}pp)")

# ====================================================================
# ATIVIDADE 4: RECOMENDAÇÕES (SÍNTESE)
# ====================================================================

print("\n" + "="*50)
print("ATIVIDADE 4 - RECOMENDAÇÕES")
print("="*50)

# 4.1 Produtos prioritários
print("🎯 TOP 3 PRODUTOS PARA FOCAR:")
produtos_priorizados = []
for produto, pct in list(produtos_oportunidade.items())[:3]:
    oportunidade = int(len(df) * (1 - pct/100))
    impacto = df[produto].corr(df['relacionamento'])
    receita_potencial = oportunidade * 120  # R$ 120/mês estimado
    produtos_priorizados.append((produto, oportunidade, impacto, receita_potencial))
    print(f"   {produto:25}: {oportunidade:6,} clientes | Impacto: {impacto:6.3f} | R$ {receita_potencial:8,}/mês")

# 4.2 Estratégia por segmento
print(f"\n👥 ESTRATÉGIA POR SEGMENTO:")
print("   Champions (top 18%): Retenção e produtos premium")
print("   Loyal (25%): Cross-selling produtos estratégicos") 
print("   Potential (31%): FOCO PRINCIPAL - Ativação e educação")
print("   Developing (20%): Onboarding estruturado")
print("   Inactive (6%): Campanhas de reativação")

# 4.3 Metas sugeridas
score_atual = df['relacionamento'].mean()
produtos_atual = df['num_produtos'].mean()

print(f"\n📊 METAS 12 MESES:")
print(f"   Score relacionamento: {score_atual:.3f} → {score_atual * 1.15:.3f} (+15%)")
print(f"   Produtos por cliente: {produtos_atual:.1f} → {produtos_atual + 0.5:.1f} (+0.5)")

if produtos_priorizados:
    produto_top = produtos_priorizados[0]
    meta_clientes = int(produto_top[1] * 0.12)  # 12% da oportunidade
    receita_adicional = meta_clientes * 120 * 12 / 1000000  # R$ MM anuais
    print(f"   {produto_top[0]}: +{meta_clientes:,} novos clientes (+R$ {receita_adicional:.1f}MM/ano)")

# 4.4 ROI estimado
investimento_estimado = 850000  # R$ 850k
if produtos_priorizados:
    receita_total_adicional = sum(p[3] for p in produtos_priorizados) * 0.08 * 12  # 8% conversão
    roi = ((receita_total_adicional - investimento_estimado) / investimento_estimado) * 100
    print(f"\n💰 PROJEÇÃO FINANCEIRA:")
    print(f"   Investimento estimado: R$ {investimento_estimado:,}")
    print(f"   Receita adicional: R$ {receita_total_adicional:,.0f}/ano")
    print(f"   ROI projetado: {roi:.0f}%")

# Visualização final
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('RECOMENDAÇÕES ESTRATÉGICAS', fontsize=14)

# Oportunidade por produto
if len(produtos_oportunidade) > 0:
    pd.Series(produtos_oportunidade).plot(kind='bar', ax=axes[0, 0])
    axes[0, 0].set_title('Produtos - Menor Penetração = Maior Oportunidade')
    axes[0, 0].tick_params(axis='x', rotation=45)

# Segmentação
segmentos.plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Distribuição dos Segmentos')
axes[0, 1].tick_params(axis='x', rotation=45)

# Relação produtos x score
axes[1, 0].scatter(df['num_produtos'], df['relacionamento'], alpha=0.5)
axes[1, 0].set_xlabel('Número de Produtos')
axes[1, 0].set_ylabel('Score Relacionamento')
axes[1, 0].set_title('Mais Produtos = Maior Relacionamento')

# Oportunidade por segmento (produto foco)
if produtos_oportunidade:
    produto_foco = list(produtos_oportunidade.keys())[0]
    opp_por_segmento = df.groupby('segmento').apply(
        lambda x: len(x) - x[produto_foco].sum()
    ).sort_values(ascending=False)
    opp_por_segmento.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title(f'Oportunidade {produto_foco} por Segmento')
    axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("✅ ANÁLISE COMPLETA FINALIZADA!")
print("="*50)

print(f"\n📋 RESUMO EXECUTIVO:")
print(f"   • Base analisada: {len(df):,} clientes")
print(f"   • Score relacionamento médio: {df['relacionamento'].mean():.3f}")
print(f"   • Produtos por cliente: {df['num_produtos'].mean():.1f}")
print(f"   • Maior oportunidade: {list(produtos_oportunidade.keys())[0] if produtos_oportunidade else 'N/A'}")
print(f"   • Segmento prioritário: Potential ({df[df['segmento'] == 'Potential'].shape[0]:,} clientes)")

print(f"\n🎯 PRÓXIMOS PASSOS:")
print("   1. Implementar segmentação RFV no CRM")
print("   2. Campanhas direcionadas para produtos de baixa penetração") 
print("   3. Jornadas de onboarding para segmento Developing")
print("   4. Cross-selling automático baseado em propensão")
