TERMOS DE ANÁLISE DE DADOS
Quartis (Q1, Q3)

Q1 (25%): 25% dos clientes têm score abaixo deste valor
Q3 (75%): 75% dos clientes têm score abaixo deste valor
Uso na apresentação: "O Q3 mostra que 75% dos clientes têm relacionamento abaixo de X"

Correlação (corr)

Range: -1 a +1
Positiva (+0.3): Quando uma variável sobe, a outra também sobe
Negativa (-0.3): Quando uma sobe, a outra desce
Zero (0.0): Não há relação
Uso: "Investimento tem correlação +0.45 com relacionamento - forte impacto positivo"

Penetração (%)

Definição: Percentual de clientes que possui determinado produto
Exemplo: "Penetração investimento: 23%" = 23% dos clientes têm investimento
Uso: "Identificamos produtos com baixa penetração como oportunidades de crescimento"

🎯 TERMOS DE SEGMENTAÇÃO
RFV Score

R: Relacionamento (0-1) → Convertido para score 1-5
F: Frequência/Produtos (0-7) → Convertido para score 1-4
V: Value/Valor (soma dos shares)
Score Final: R + F (2-9)
Uso: "Criamos metodologia RFV adaptada ao contexto bancário"

Bins (Faixas)

Definição: Divisões que transformam valores contínuos em categorias
Exemplo: Score 0.0-0.2 vira "Baixo", 0.8-1.0 vira "Alto"
Uso: "Utilizamos bins para segmentar clientes em grupos acionáveis"

pd.cut() vs pd.qcut()

cut(): Faixas fixas que você define
qcut(): Divide em quantidades iguais (quartis, quintis)
Uso: "Optamos por cut() para ter controle sobre as faixas de segmentação"

💼 TERMOS DE NEGÓCIO
Cross-selling

Definição: Vender produtos complementares ao que o cliente já tem
Exemplo: Cliente tem cartão → ofertar investimento
Uso: "Identificamos oportunidades de cross-selling baseadas em correlações"

Market Share

Definição: Participação da empresa no mercado total
Contexto: % dos produtos financeiros do cliente que são nossos
Uso: "Estratégias para ampliar nosso share of wallet dos clientes"

Churn/Atrito

Definição: Taxa de clientes que deixam o banco
Importância: Retenção é mais barata que aquisição
Uso: "Segmento Inactive tem maior risco de churn - necessita reativação"

Share of Wallet (SHR_*)

Definição: Participação de cada produto no relacionamento total
Cálculo: Valor produto / Valor total relacionamento
Uso: "Share metrics mostram importância relativa de cada produto"

📈 TERMOS DE PERFORMANCE
ROI (Return on Investment)

Fórmula: (Receita - Investimento) / Investimento * 100
Exemplo: Investiu R$850k, ganhou R$2.4MM → ROI = 180%
Uso: "Projetamos ROI de 265% com payback em 10 meses"

Payback

Definição: Tempo para recuperar o investimento
Cálculo: Investimento / (Receita adicional mensal)
Uso: "Payback de 10 meses demonstra viabilidade rápida"

LTV (Customer Lifetime Value)

Definição: Valor que cliente gera durante todo relacionamento
Uso: "Champions têm LTV 4x maior que Developing"

🎯 TERMOS DE METODOLOGIA
Democratização de Dados

Definição: Tornar insights acessíveis para áreas de negócio
Objetivo: Decisões baseadas em dados, não intuição
Uso: "Pipeline automatizado democratiza insights para Finanças e Riscos"

Pipeline de Dados

Definição: Fluxo automatizado de coleta → processamento → entrega
Benefício: Dados em tempo real para tomada de decisão
Uso: "Pipeline robusto garante qualidade e agilidade dos insights"

💡 FRASES-CHAVE PARA APRESENTAÇÃO

"Metodologia RFV consolidada internacionalmente"
"Segmentação baseada em dados, não intuição"
"Correlações identificam produtos-âncora do relacionamento"
"Bins estratégicos para ações comerciais direcionadas"
"Pipeline automatizado democratiza insights"
"ROI robusto com payback acelerado"
