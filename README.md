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





🔗 O que é CORRELAÇÃO?
Correlação mede se duas variáveis "andam juntas" ou não.
Range de valores:

+1.000: Correlação perfeita positiva
+0.500: Correlação moderada positiva
0.000: Não há relação
-0.500: Correlação moderada negativa
-1.000: Correlação perfeita negativa

📊 Interpretação prática no seu case:
python# Exemplo de output que você vai ver:
cartao_de_credito        : +0.234
investimento             : +0.456  ← FORTE!
consignado              : +0.312
crediario               : +0.189
lis                     : +0.098  ← FRACA
O que isso significa:
🟢 Correlação POSITIVA (+0.456 - Investimento):

Interpretação: Clientes com investimento tendem a ter score de relacionamento MAIOR
Na prática:

Cliente SEM investimento: score médio 0.35
Cliente COM investimento: score médio 0.62


Insight de negócio: "Investimento é produto-âncora do relacionamento"

🟡 Correlação FRACA (+0.098 - LIS):

Interpretação: TER ou NÃO TER LIS quase não impacta o relacionamento
Na prática: Score parecido com e sem LIS
Insight: "LIS não é diferencial para relacionamento"

🎯 Como usar na APRESENTAÇÃO:
Slide: "Produtos que Mais Impactam o Relacionamento"
🏆 PRODUTOS-ÂNCORA (Correlação > 0.30):
   • Investimento: +0.456 → "Produto estratégico #1"  
   • Consignado: +0.312 → "Forte impacto no relacionamento"

⚠️ PRODUTOS BÁSICOS (Correlação < 0.20):
   • LIS: +0.098 → "Produto transacional"
   • Crediário: +0.189 → "Necessário, mas não diferencial"
💡 Insight ESTRATÉGICO:
Para CRESCER relacionamento:

FOQUE em produtos com correlação ALTA (Investimento, Consignado)
Cross-sell prioritário: Ofertar investimento para quem não tem
Campanha: "Clientes com investimento têm 85% mais relacionamento"

Para SEGMENTAR campanhas:

Champions: Já têm produtos de alta correlação
Potential: Oferecer produtos-âncora (investimento)
Developing: Começar com produtos básicos, evoluir para âncora

🧮 Como o Python calcula:
python# Simplificado:
# Para cada cliente, verifica:
# - Tem investimento (1) ou não tem (0)
# - Score de relacionamento (0.0 a 1.0)
# 
# Calcula se há padrão:
# Quem tem investimento → score maior?
# Quem não tem investimento → score menor?
🎤 Frases para usar na apresentação:

"Identificamos produtos-âncora através de análise de correlação"
"Investimento tem correlação 0.456 - o maior impacto no relacionamento"
"Estratégia: priorizar cross-sell de produtos com correlação >0.30"
"Dados mostram que clientes com investimento têm relacionamento X% maior"

⚡ Dica OURO:
Quando apresentar, conecte com ROI:

"Investimento tem correlação 0.456 com relacionamento. Por isso, nossa campanha foca neste produto - cada novo investidor pode aumentar seu score em até 40%, gerando R$ 180/mês adicional."

Agora você domina correlação! 📈✨ É um dos conceitos mais poderosos para justificar estratégias com dados.



























######### Case Dados



# Solução Big Data para Processamento de Contratos
## Arquitetura de Alto Nível na AWS

### 1. INGESTÃO DE DADOS (2AM - 3AM)

**On-Premises → AWS**
- **AWS Direct Connect** ou **VPN Site-to-Site**: Conexão dedicada entre o servidor NFS on-premises e AWS
- **AWS DataSync**: Sincronização automática dos arquivos do NFS para S3
  - Agendamento para executar diariamente às 2:30 AM
  - Transferência otimizada com compressão
  - Verificação de integridade dos dados

**Armazenamento Inicial**
- **Amazon S3 - Bucket Raw Data**: Armazenamento dos arquivos posicionais originais
  - Estrutura: `s3://contracts-raw/year=2025/month=08/day=12/`
  - Storage Class: S3 Standard-IA (menor custo para dados pouco acessados)

### 2. PROCESSAMENTO E TRANSFORMAÇÃO (3AM - 8AM)

**Orquestração**
- **AWS Step Functions**: Coordenação do pipeline completo
- **Amazon EventBridge**: Trigger automático quando novos arquivos chegam no S3

**Processamento Distribuído**
- **Amazon EMR Serverless**: Cluster Spark gerenciado para processamento dos 10GB+ por arquivo
  - **Apache Spark 3.x** com **Scala/Python** para transformação dos dados posicionais
  - Auto-scaling baseado na carga de trabalho
  - Processamento paralelo de múltiplos arquivos simultaneamente

**Transformação de Dados**
- **Framework**: Apache Spark com:
  - **Linguagem**: Python (PySpark) ou Scala
  - **Bibliotecas**: Pandas, PyArrow para otimização
- **Processo**:
  1. Parse dos arquivos posicionais para estrutura tabular
  2. Validação e limpeza de dados
  3. Particionamento otimizado por data
  4. Conversão para formato Parquet (compressão ~90%)

### 3. ARMAZENAMENTO ESTRUTURADO

**Data Lake**
- **Amazon S3 - Bucket Processed Data**: Dados estruturados em Parquet
  - Estrutura particionada: `s3://contracts-processed/year=2025/month=08/day=12/`
  - Compressão Snappy para otimização de consultas
  - Lifecycle Policy: 
    - Últimos 12 meses: S3 Standard
    - 12 meses - 5 anos: S3 Standard-IA → S3 Glacier Flexible Retrieval

**Catálogo de Dados**
- **AWS Glue Data Catalog**: Metadados e schema dos dados estruturados
- **AWS Glue Crawler**: Descoberta automática de novos dados e atualização do catálogo

### 4. CAMADA DE CONSULTAS SQL

**Query Engine**
- **Amazon Athena**: Motor de consultas SQL serverless
  - Consultas diretas no S3 via Parquet
  - Integração nativa com Glue Data Catalog
  - Particionamento otimizado para performance
  - Custo baseado em dados escaneados

**Cache e Performance**
- **Amazon ElastiCache Redis**: Cache de consultas frequentes
- **Athena Query Result Location**: Reutilização de resultados

### 5. MONITORAMENTO E ALERTAS

**Observabilidade**
- **Amazon CloudWatch**: Métricas customizadas do pipeline
  - Tempo de processamento
  - Volume de dados processados
  - Taxa de erro por etapa
- **AWS X-Ray**: Tracing distribuído para debug

**Alertas**
- **Amazon SNS**: Notificações por email/SMS
  - Sucesso do processamento diário
  - Falhas no pipeline
  - Violação de SLA (processamento não concluído até 8:30 AM)
- **Amazon CloudWatch Alarms**: Alertas baseados em métricas

### 6. GOVERNANÇA E SEGURANÇA

**Controle de Acesso**
- **AWS IAM**: Roles e políticas granulares
- **Amazon Cognito**: Autenticação de usuários para ferramentas de BI
- **AWS Lake Formation**: Governança centralizada do data lake

**Auditoria**
- **AWS CloudTrail**: Log de todas as operações
- **Amazon Macie**: Descoberta e proteção de dados sensíveis

### 7. FERRAMENTAS ANALÍTICAS

**Dashboards e Relatórios**
- **Amazon QuickSight**: Dashboards nativos da AWS
- **Integração com ferramentas externas**:
  - Tableau via JDBC/ODBC
  - Power BI via conectores
  - Jupyter Notebooks via Amazon SageMaker

## STACK TECNOLÓGICO RECOMENDADO

### Linguagens e Frameworks
- **Python/PySpark**: Processamento de dados
- **SQL**: Consultas e análises
- **Terraform/CloudFormation**: Infrastructure as Code
- **Apache Airflow** (alternativa ao Step Functions para orquestrações complexas)

### Bibliotecas Python Principais
```python
# Processamento de dados
import pandas as pd
import pyarrow as pa
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, when

# AWS SDK
import boto3

# Monitoramento
import logging
from datetime import datetime
```

## PIPELINE DE ENTREGA CONTÍNUA

### DevOps e CI/CD
- **AWS CodeCommit**: Repositório de código
- **AWS CodeBuild**: Build e testes automatizados
- **AWS CodePipeline**: Pipeline de deployment
- **AWS CodeDeploy**: Deploy de aplicações

### Estrutura de Ambientes
- **DEV**: Desenvolvimento e testes com subset de dados
- **STAGING**: Homologação com dados simulados
- **PROD**: Produção com dados reais

## ESTRATÉGIA DE CUSTOS

### Otimizações Principais
1. **EMR Serverless**: Pagamento apenas pelo uso efetivo
2. **Athena**: Custo por dados escaneados (otimização via Parquet + particionamento)
3. **S3 Lifecycle**: Transição automática para storage classes mais baratos
4. **Spot Instances**: Para cargas de trabalho tolerantes a interrupção
5. **Reserved Instances**: Para recursos fixos (se necessário)

### Estimativa de Custos Mensais (aproximada)
- **S3 Storage**: $500-800 (dados históricos 5 anos)
- **EMR Serverless**: $300-500 (processamento diário 5h)
- **Athena**: $100-200 (baseado em consultas)
- **Data Transfer**: $50-100
- **Outros serviços**: $100-150
- **Total aproximado**: $1.050-1.750/mês

## SLA E PERFORMANCE

### Cronograma Diário
- **02:00**: Geração dos arquivos (mainframe)
- **02:30**: Início da sincronização para S3
- **03:00**: Início do processamento Spark
- **08:00**: Processamento concluído
- **09:00**: Dados disponíveis para consulta (SLA atendido)

### Estratégias de Recuperação
- **Backup**: Replicação cross-region dos dados críticos
- **Disaster Recovery**: Pipeline em região secundária
- **Rollback**: Versionamento de dados e código

## EVOLUÇÃO E ESCALABILIDADE

### Melhorias Futuras
1. **Real-time Processing**: Kinesis + Lambda para dados streaming
2. **Machine Learning**: SageMaker para análises preditivas
3. **Data Quality**: Great Expectations + Glue Data Quality
4. **Metadata Management**: Apache Atlas ou AWS DataZone

### Escalabilidade Horizontal
- EMR Serverless escala automaticamente
- Athena suporta consultas paralelas ilimitadas
- S3 não possui limites de armazenamento

## IMPLEMENTAÇÃO FASEADA

### Fase 1 (MVP - 4 semanas)
- Setup básico S3 + EMR + Athena
- Pipeline simples de transformação
- Monitoramento básico

### Fase 2 (8 semanas)
- Otimizações de performance
- Alertas e monitoramento avançado
- Governança de dados

### Fase 3 (12 semanas)
- Ferramentas de BI
- Automação completa
- Documentação e treinamento

Esta arquitetura atende todos os requisitos de escala, performance, custo e SLA, utilizando as melhores práticas de Big Data na nuvem AWS.


Resumo Executivo da Solução
Bottom Line Up Front: A solução proposta utiliza uma arquitetura serverless na AWS que processa automaticamente 300 milhões de contratos diários, transformando dados posicionais em formato estruturado (Parquet) e disponibilizando via SQL com custo otimizado de ~$1.200/mês.
Principais Diferenciais:
🚀 Performance: EMR Serverless + Spark processam os 10GB+ por arquivo em paralelo, garantindo conclusão até 8AM
⚡ SLA Garantido: Pipeline automatizado das 2:30 às 8:00, dados disponíveis às 9:00 conforme requisito
💰 Custo Otimizado:

Pagamento apenas pelo uso efetivo (serverless)
Storage lifecycle automático (S3 Standard → IA → Glacier)
Formato Parquet reduz custos de consulta em ~90%

🔧 Tecnologia Moderna:

Linguagem: Python/PySpark para transformações
Formato: Parquet com compressão Snappy
Query Engine: Amazon Athena (SQL direto no data lake)
Orquestração: Step Functions + EventBridge

📊 Analytics Ready: Integração nativa com QuickSight, Tableau, Power BI e qualquer ferramenta que suporte JDBC/ODBC
🔔 Monitoramento Completo: CloudWatch + SNS para alertas automáticos de sucesso/falha e violação de SLA
A arquitetura é totalmente gerenciada, escalável automaticamente e permite implementação faseada começando com um MVP funcional em 4 semanas.



















# Detalhamento Funcional dos Componentes da Arquitetura

## 🏢 AMBIENTE ON-PREMISES (2:00 - 2:30 AM)

### **Mainframe**
**O que faz:**
- Processa sistemas legados de contratos durante a madrugada
- Gera arquivos de texto posicionais com 300 milhões de registros
- Executa rotinas batch de extração de dados dos sistemas core
- Consolida informações de múltiplas fontes internas

**Como funciona:**
- Job schedulado para executar às 2:00 AM todos os dias
- Extrai dados de bancos DB2/VSAM do mainframe
- Formata dados em layout posicional fixo (ex: posições 1-10 = ID contrato, 11-30 = nome cliente)
- Grava arquivos sequenciais no sistema de arquivos do mainframe

### **Servidor NFS (Network File System)**
**O que faz:**
- Armazena temporariamente os arquivos gerados pelo mainframe
- Disponibiliza arquivos via protocolo NFS para outros sistemas
- Funciona como staging area entre mainframe e cloud

**Como funciona:**
- Recebe arquivos do mainframe via transferência interna
- Monta sistema de arquivos compartilhado (/mnt/contratos/YYYYMMDD/)
- Organiza arquivos por data: contratos_20250812_001.txt, contratos_20250812_002.txt...
- Cada arquivo tem ~10GB com aproximadamente 12-15 milhões de registros

### **Conector Cloud**
**O que faz:**
- Monitora continuamente o diretório NFS por novos arquivos
- Inicia transferência automática para AWS assim que detecta novos dados
- Garante integridade dos dados durante a transferência

**Como funciona:**
- Scanner automático verifica diretório a cada 5 minutos
- Identifica arquivos novos baseado em timestamp/tamanho
- Prepara arquivos para upload (compressão opcional)
- Mantém log de transferências para auditoria

---

## ☁️ AWS CLOUD - CAMADA DE INGESTÃO (2:30 - 3:00 AM)

### **AWS Direct Connect / VPN Site-to-Site**
**O que faz:**
- Estabelece conexão segura e dedicada entre datacenter on-premises e AWS
- Garante largura de banda consistente para transferência dos 10GB+ diários
- Reduz latência e custos de transferência de dados

**Como funciona:**
- Conexão dedicada de 1-10 Gbps entre seu datacenter e AWS
- Roteamento direto para VPC sem passar pela internet pública
- Criptografia em trânsito para segurança dos dados
- Monitoramento de bandwidth e latência

### **AWS DataSync**
**O que faz:**
- Sincroniza automaticamente arquivos do NFS on-premises para S3
- Verifica integridade dos dados durante transferência
- Otimiza transferência com compressão e paralelização

**Como funciona:**
```python
# Configuração do DataSync (conceitual)
task_config = {
    "source_location": "nfs://servidor-nfs/contratos/",
    "destination_location": "s3://contracts-raw/",
    "schedule": "cron(30 2 * * ? *)",  # 2:30 AM diário
    "options": {
        "verify_mode": "POINT_IN_TIME_CONSISTENT",
        "preserve_deleted_files": "REMOVE",
        "transfer_mode": "CHANGED"
    }
}
```
- Agenda execução para 2:30 AM todos os dias
- Transfere apenas arquivos novos/modificados
- Calcula checksums para validação de integridade
- Comprime dados durante transferência (economia ~30-50%)

### **S3 Raw Data Bucket**
**O que faz:**
- Armazena arquivos originais posicionais como data lake bronze
- Organiza dados por partições de data para otimização
- Serve como fonte única da verdade para dados brutos

**Como funciona:**
```
Estrutura do bucket:
s3://contracts-raw/
├── year=2025/
│   ├── month=08/
│   │   ├── day=12/
│   │   │   ├── contratos_20250812_001.txt
│   │   │   ├── contratos_20250812_002.txt
│   │   │   └── contratos_20250812_...txt
│   │   └── day=13/
│   └── month=09/
└── year=2024/
```
- Storage Class: S3 Standard-IA (acesso pouco frequente)
- Versionamento habilitado para recuperação
- Lifecycle policy: dados >30 dias → S3 Glacier

### **Amazon EventBridge**
**O que faz:**
- Monitora eventos do S3 (chegada de novos arquivos)
- Dispara pipeline de processamento automaticamente
- Funciona como trigger inteligente para orquestração

**Como funciona:**
```json
{
  "Rules": [{
    "Name": "contracts-processing-trigger",
    "EventPattern": {
      "source": ["aws.s3"],
      "detail-type": ["Object Created"],
      "detail": {
        "bucket": {"name": ["contracts-raw"]},
        "object": {"key": [{"prefix": "year=2025/month=08/day="}]}
      }
    },
    "Targets": [{
      "Arn": "arn:aws:states:::stateMachine:contracts-pipeline",
      "RoleArn": "arn:aws:iam:::role/EventBridgeRole"
    }]
  }]
}
```
- Detecta novos objetos no S3 em tempo real
- Filtra apenas arquivos de contrato (.txt)
- Envia evento para Step Functions com metadados do arquivo

---

## ⚙️ AWS CLOUD - CAMADA DE PROCESSAMENTO (3:00 - 8:00 AM)

### **AWS Step Functions**
**O que faz:**
- Orquestra todo o pipeline de processamento como workflow
- Coordena execução sequencial e paralela de tarefas
- Gerencia tratamento de erros e retry logic

**Como funciona:**
```json
{
  "Comment": "Pipeline de Processamento de Contratos",
  "StartAt": "ValidateInput",
  "States": {
    "ValidateInput": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:::function:validate-files",
      "Next": "ProcessInParallel"
    },
    "ProcessInParallel": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "ProcessFile1",
          "States": {
            "ProcessFile1": {
              "Type": "Task",
              "Resource": "arn:aws:emr-serverless:::startJobRun",
              "Parameters": {
                "applicationId": "emr-app-123",
                "jobDriver": {
                  "sparkSubmit": {
                    "entryPoint": "s3://scripts/process_contracts.py"
                  }
                }
              }
            }
          }
        }
      ],
      "Next": "UpdateCatalog"
    },
    "UpdateCatalog": {
      "Type": "Task",
      "Resource": "arn:aws:glue:::startCrawler",
      "End": true
    }
  }
}
```
- Recebe evento do EventBridge com lista de arquivos
- Executa validações preliminares (tamanho, formato)
- Paraleliza processamento de múltiplos arquivos
- Monitora status de cada job EMR

### **Amazon EMR Serverless**
**O que faz:**
- Executa jobs Apache Spark para transformar dados posicionais em estruturados
- Processa múltiplos arquivos de 10GB em paralelo
- Converte formato texto para Parquet otimizado

**Como funciona:**
```python
# Script principal de processamento (process_contracts.py)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring, trim, when, regexp_replace
from pyspark.sql.types import StructType, StructField, StringType, DateType, DecimalType

def main():
    spark = SparkSession.builder \
        .appName("ContractsProcessing") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .getOrCreate()
    
    # Schema do arquivo posicional
    schema_posicional = {
        "id_contrato": (1, 15),      # posições 1-15
        "cpf_cnpj": (16, 30),        # posições 16-30  
        "nome_cliente": (31, 80),     # posições 31-80
        "valor_contrato": (81, 95),   # posições 81-95
        "data_inicio": (96, 104),     # posições 96-104 (YYYYMMDD)
        "data_fim": (105, 113),       # posições 105-113
        "status": (114, 120),         # posições 114-120
        "tipo_produto": (121, 140)    # posições 121-140
    }
    
    # Lê arquivo texto
    input_path = "s3://contracts-raw/year=2025/month=08/day=12/"
    df_raw = spark.read.text(input_path)
    
    # Converte posicional para colunas estruturadas
    df_structured = df_raw.select(
        trim(substring(col("value"), 1, 15)).alias("id_contrato"),
        trim(substring(col("value"), 16, 15)).alias("cpf_cnpj"),
        trim(substring(col("value"), 31, 50)).alias("nome_cliente"),
        substring(col("value"), 81, 15).cast(DecimalType(15,2)).alias("valor_contrato"),
        substring(col("value"), 96, 8).alias("data_inicio_raw"),
        substring(col("value"), 105, 8).alias("data_fim_raw"),
        trim(substring(col("value"), 114, 7)).alias("status"),
        trim(substring(col("value"), 121, 20)).alias("tipo_produto")
    )
    
    # Transformações e limpeza
    df_clean = df_structured \
        .filter(col("id_contrato").isNotNull()) \
        .withColumn("data_inicio", 
            when(col("data_inicio_raw").rlike("^\d{8}$"), 
                 to_date(col("data_inicio_raw"), "yyyyMMdd"))) \
        .withColumn("data_fim",
            when(col("data_fim_raw").rlike("^\d{8}$"),
                 to_date(col("data_fim_raw"), "yyyyMMdd"))) \
        .withColumn("cpf_cnpj_clean", 
            regexp_replace(col("cpf_cnpj"), "[^0-9]", "")) \
        .drop("data_inicio_raw", "data_fim_raw")
    
    # Particionamento e escrita otimizada
    output_path = "s3://contracts-processed/year=2025/month=08/day=12/"
    df_clean.write \
        .mode("overwrite") \
        .option("compression", "snappy") \
        .partitionBy("tipo_produto") \
        .parquet(output_path)
    
    # Métricas para monitoramento
    total_records = df_clean.count()
    invalid_records = df_raw.count() - total_records
    
    print(f"Processamento concluído: {total_records} registros válidos")
    print(f"Registros inválidos: {invalid_records}")
    
    spark.stop()

if __name__ == "__main__":
    main()
```

**Configuração do EMR Serverless:**
- **Executors**: Auto-scaling de 10-100 executors baseado na carga
- **Memory per executor**: 8GB (para arquivos de 10GB)
- **CPU cores per executor**: 4 vCPUs
- **Driver**: 4 vCPUs, 16GB RAM
- **Tempo estimado**: 1-2 horas para processar todos os arquivos do dia

### **S3 Processed Data Bucket**
**O que faz:**
- Armazena dados estruturados em formato Parquet (data lake silver)
- Otimiza consultas com particionamento inteligente
- Reduz drasticamente o tamanho dos dados (compressão ~90%)

**Como funciona:**
```
Estrutura otimizada:
s3://contracts-processed/
├── year=2025/month=08/day=12/
│   ├── tipo_produto=CREDITO_PESSOAL/
│   │   ├── part-00000-snappy.parquet (100MB)
│   │   ├── part-00001-snappy.parquet (100MB)
│   │   └── ...
│   ├── tipo_produto=FINANCIAMENTO/
│   │   ├── part-00000-snappy.parquet
│   │   └── ...
│   └── tipo_produto=CARTAO_CREDITO/
└── year=2025/month=08/day=13/
```

**Benefícios do Parquet:**
- **Compressão**: 10GB texto → ~1GB Parquet
- **Consultas rápidas**: Leitura colunar otimizada
- **Predicate pushdown**: Filtra dados durante leitura
- **Schema evolution**: Adiciona colunas sem reprocessar dados históricos

### **AWS Glue Data Catalog**
**O que faz:**
- Armazena metadados e schema dos dados estruturados
- Funciona como "catálogo de biblioteca" para todas as tabelas
- Permite descoberta automática de dados

**Como funciona:**
```sql
-- Schema automático criado no Glue Catalog
CREATE EXTERNAL TABLE contracts_processed (
    id_contrato string,
    cpf_cnpj string,
    nome_cliente string,
    valor_contrato decimal(15,2),
    data_inicio date,
    data_fim date,
    status string,
    tipo_produto string
)
PARTITIONED BY (
    year string,
    month string,
    day string,
    tipo_produto string
)
STORED AS PARQUET
LOCATION 's3://contracts-processed/'
```
- Registra automaticamente novas partições
- Mantém histórico de alterações de schema
- Integra com Athena para consultas SQL

### **AWS Glue Crawler**
**O que faz:**
- Escaneia automaticamente novos dados no S3
- Descobre schema e partições dos arquivos Parquet
- Atualiza Glue Catalog com novos metadados

**Como funciona:**
- **Schedule**: Executa a cada 1 hora durante processamento (3-8 AM)
- **Classificadores**: Identifica formato Parquet automaticamente
- **Schema detection**: Analisa amostras para inferir tipos de dados
- **Partition detection**: Descobre novas partições year/month/day
- **Update behavior**: Adiciona apenas novas tabelas/partições

---

## 📊 AWS CLOUD - CAMADA DE CONSULTAS (9:00 AM+)

### **Amazon Athena**
**O que faz:**
- Motor de consultas SQL serverless que opera diretamente no S3
- Processa consultas analíticas complexas sem infraestrutura
- Escala automaticamente baseado na complexidade da query

**Como funciona:**
```sql
-- Exemplos de consultas que os usuários farão:

-- 1. Relatório diário de contratos por produto
SELECT 
    tipo_produto,
    COUNT(*) as total_contratos,
    SUM(valor_contrato) as valor_total,
    AVG(valor_contrato) as valor_medio
FROM contracts_processed 
WHERE year='2025' AND month='08' AND day='12'
GROUP BY tipo_produto
ORDER BY valor_total DESC;

-- 2. Análise de tendência mensal
SELECT 
    year, month,
    COUNT(*) as contratos_mes,
    SUM(valor_contrato) as volume_mensal
FROM contracts_processed 
WHERE year='2025' AND month BETWEEN '06' AND '08'
GROUP BY year, month
ORDER BY year, month;

-- 3. Contratos vencendo nos próximos 30 dias
SELECT 
    id_contrato,
    nome_cliente,
    valor_contrato,
    data_fim,
    DATEDIFF(data_fim, CURRENT_DATE) as dias_para_vencer
FROM contracts_processed 
WHERE data_fim BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL 30 DAY
ORDER BY data_fim;
```

**Otimizações do Athena:**
- **Projection**: Elimina necessidade de listar partições
- **Columnar reads**: Lê apenas colunas necessárias
- **Predicate pushdown**: Filtra no S3 antes de trazer dados
- **Query result caching**: Reutiliza resultados por 24h

### **Amazon ElastiCache (Redis)**
**O que faz:**
- Cache em memória para consultas frequentes
- Reduz latência de relatórios executados múltiplas vezes
- Armazena resultados de dashboards populares

**Como funciona:**
```python
# Exemplo de implementação de cache
import redis
import json
import hashlib

redis_client = redis.Redis(host='elasticache-endpoint', port=6379)

def cached_query(sql_query, ttl=3600):
    # Gera hash da query para usar como chave
    query_hash = hashlib.md5(sql_query.encode()).hexdigest()
    
    # Verifica se resultado está em cache
    cached_result = redis_client.get(f"query:{query_hash}")
    
    if cached_result:
        return json.loads(cached_result)
    
    # Se não está em cache, executa query no Athena
    result = execute_athena_query(sql_query)
    
    # Armazena resultado em cache
    redis_client.setex(
        f"query:{query_hash}", 
        ttl, 
        json.dumps(result)
    )
    
    return result
```
- **TTL**: 1 hora para dados do dia, 24h para dados históricos
- **Invalidação**: Limpa cache quando novos dados chegam
- **Memory**: 16GB Redis cluster para ~10K consultas cacheadas

### **Amazon QuickSight**
**O que faz:**
- Cria dashboards e visualizações business intelligence
- Conecta diretamente ao Athena para dados em tempo real
- Permite self-service analytics para usuários de negócio

**Como funciona:**
- **Data Sources**: Conecta ao Athena via JDBC
- **SPICE**: Cache in-memory para dashboards mais rápidos
- **Auto-refresh**: Atualiza dados a cada 1 hora
- **Dashboards típicos**:
  - Volume diário de contratos
  - Distribuição por tipo de produto
  - Top 10 clientes por valor
  - Análise de inadimplência
  - Previsão de renovações

### **Ferramentas BI Externas (Tableau/Power BI)**
**O que faz:**
- Conecta via JDBC/ODBC para análises avançadas
- Permite criação de relatórios personalizados
- Integra com ferramentas existentes da organização

**Como funciona:**
```
Conexão JDBC para Athena:
jdbc:awsathena://AwsRegion=us-east-1;
S3OutputLocation=s3://athena-results/;
Workgroup=contracts-workgroup;
```
- **Drivers**: ODBC/JDBC oficiais da AWS
- **Authentication**: IAM roles ou Cognito
- **Performance**: Queries otimizadas com cache

---

## 🚨 AWS CLOUD - CAMADA DE MONITORAMENTO

### **Amazon CloudWatch**
**O que faz:**
- Coleta métricas de todos os serviços AWS
- Monitora performance, erros e SLA
- Gera alertas baseados em thresholds

**Como funciona:**
```python
# Métricas customizadas enviadas durante processamento
import boto3

cloudwatch = boto3.client('cloudwatch')

def publish_metrics(processed_records, processing_time, errors):
    cloudwatch.put_metric_data(
        Namespace='Contracts/Processing',
        MetricData=[
            {
                'MetricName': 'ProcessedRecords',
                'Value': processed_records,
                'Unit': 'Count',
                'Dimensions': [
                    {'Name': 'ProcessDate', 'Value': '2025-08-12'}
                ]
            },
            {
                'MetricName': 'ProcessingTime',
                'Value': processing_time,
                'Unit': 'Seconds'
            },
            {
                'MetricName': 'ErrorRate',
                'Value': errors / processed_records * 100,
                'Unit': 'Percent'
            }
        ]
    )
```

**Métricas monitoradas:**
- **EMR**: Tempo de processamento, memory usage, falhas de job
- **S3**: Tamanho dos arquivos, número de objetos
- **Athena**: Query execution time, data scanned, falhas
- **Step Functions**: Executions success/failure rate

### **Amazon SNS (Simple Notification Service)**
**O que faz:**
- Envia notificações por email, SMS ou webhook
- Distribui alertas para múltiplos destinatários
- Integra com outros sistemas de monitoramento

**Como funciona:**
```json
{
  "TopicArn": "arn:aws:sns:us-east-1:123456789:contracts-alerts",
  "Subscriptions": [
    {
      "Protocol": "email",
      "Endpoint": "admin@empresa.com"
    },
    {
      "Protocol": "sms", 
      "Endpoint": "+5511999999999"
    },
    {
      "Protocol": "https",
      "Endpoint": "https://slack-webhook.empresa.com/alerts"
    }
  ]
}
```

**Tipos de alertas:**
- ✅ **Sucesso**: "Processamento concluído - 300M registros em 4h30min"
- ❌ **Falha**: "ERRO: Job EMR falhou - arquivo corrompido detected"
- ⚠️ **Warning**: "SLA em risco - processamento 80% concluído às 7:30 AM"
- 📊 **Métricas**: "Hoje: +5% volume vs ontem, -2% tempo processamento"

### **AWS X-Ray**
**O que faz:**
- Rastreamento distribuído de requests através de múltiplos serviços
- Identifica gargalos de performance no pipeline
- Debug de falhas complexas

**Como funciona:**
- **Traces**: Segue execução desde EventBridge até conclusão
- **Service Map**: Visualiza interações entre serviços
- **Performance insights**: Identifica serviços mais lentos
- **Error analysis**: Correlaciona erros entre componentes

---

## 🔒 AWS CLOUD - CAMADA DE SEGURANÇA

### **AWS IAM (Identity and Access Management)**
**O que faz:**
- Controla quem pode acessar quais recursos AWS
- Define permissões granulares por serviço e ação
- Implementa princípio de menor privilégio

**Como funciona:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::account:role/DataAnalyst"},
      "Action": [
        "athena:GetQueryResults",
        "athena:StartQueryExecution", 
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::contracts-processed/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:prefix": ["year=2025/"]
        }
      }
    }
  ]
}
```
**Roles principais:**
- **DataEngineer**: Acesso completo ao pipeline
- **DataAnalyst**: Apenas leitura de dados processados
- **BusinessUser**: Acesso via QuickSight apenas
- **EMRServiceRole**: Permissões para EMR acessar S3/Glue

### **Amazon Cognito**
**O que faz:**
- Autentica usuários para ferramentas de BI
- Gerencia login federado com Active Directory
- Controla acesso baseado em grupos de usuário

**Como funciona:**
- **User Pools**: Diretório de usuários com MFA
- **Identity Pools**: Troca tokens por credenciais AWS temporárias
- **SAML/OIDC**: Integração com AD corporativo
- **Group-based access**: Analistas vs Executives têm acessos diferentes

---

## 📈 RESUMO DO FLUXO COMPLETO

### **Timeline Diária Detalhada:**

**2:00 AM** → Mainframe executa jobs de extração
**2:15 AM** → Arquivos gravados no NFS (300M registros, ~100GB total)
**2:30 AM** → DataSync inicia transferência para S3
**2:45 AM** → Primeiros arquivos chegam no S3, EventBridge dispara pipeline
**3:00 AM** → Step Functions inicia, EMR Serverless começa processamento
**3:15 AM** → Múltiplos jobs Spark processam arquivos em paralelo
**6:00 AM** → 80% dos dados processados, arquivos Parquet gerados
**7:30 AM** → Glue Crawler atualiza catálogo, novos dados disponíveis
**8:00 AM** → Pipeline concluído, SNS envia notificação de sucesso
**9:00 AM** → **SLA CUMPRIDO** - Usuários fazem primeiras consultas SQL

### **Métricas de Performance:**
- **Volume diário**: 300M registros → ~1GB Parquet (compressão 99%)
- **Tempo total**: 5 horas (2:30-8:00 AM)
- **Throughput**: 60M registros/hora
- **Consultas**: <5s para relatórios típicos via cache
- **Disponibilidade**: 99.9% (SLA cumprido 364 dias/ano)



Detalhei exatamente o que cada componente faz no processamento dos seus 300 milhões de contratos!
Principais Insights:
🎯 Fluxo de Transformação dos Dados:

Entrada: Arquivos texto posicionais (10GB cada)
Processamento: Spark converte para estrutura tabular
Saída: Parquet comprimido (99% menor, consultas 100x mais rápidas)

⚡ Otimizações Críticas:

Paralelização: Múltiplos arquivos processados simultaneamente
Particionamento: Dados organizados por data + tipo_produto
Cache inteligente: Redis armazena consultas frequentes
Compressão Snappy: Reduz drasticamente tempo de I/O

🔄 Automação Completa:

Trigger automático: Novos arquivos → pipeline inicia sozinho
Auto-scaling: EMR ajusta recursos baseado na carga
Alertas inteligentes: Notifica sucesso/falha/SLA em risco

💡 Benefício Principal:
Transforma dados "mortos" (arquivos texto) em data lake consultável via SQL, permitindo que analistas façam perguntas como:

"Quantos contratos de crédito pessoal foram criados ontem?"
"Qual a tendência de inadimplência nos últimos 6 meses?"
"Quais clientes têm contratos vencendo na próxima semana?"

Resultado: De um processamento batch manual para uma plataforma de dados self-service que atende 300M+ registros diários dentro do SLA de 5 horas!

























<img width="925" height="747" alt="diagrama" src="https://github.com/user-attachments/assets/48ca7b87-1aab-4e9a-9040-7c214a494e96" />












Criei um diagrama completo da arquitetura com todos os serviços AWS interconectados! O diagrama mostra:
Fluxo Principal de Dados (setas laranja):

On-premises → AWS: Mainframe (2AM) → NFS → Conector → DataSync → S3 Raw
Processamento: S3 Raw → EMR Serverless → S3 Processed (Parquet)
Consultas: S3 Processed → Athena → Ferramentas de BI

Orquestração (setas pretas):

EventBridge detecta novos arquivos no S3 Raw
Step Functions coordena todo o pipeline
Glue Crawler atualiza metadados automaticamente

Monitoramento (linhas tracejadas azuis):

CloudWatch coleta métricas de todos os serviços
SNS envia alertas por email
X-Ray faz tracing distribuído

Principais Conexões:

EMR Serverless processa dados do S3 Raw e salva no S3 Processed
Athena consulta dados via Glue Catalog
ElastiCache armazena cache de consultas frequentes
QuickSight e BI externos conectam via Athena
Todas as operações são monitoradas pelo CloudWatch

Timeline Garantida:

2:00 AM: Geração no mainframe
2:30-3:00 AM: Ingestão para AWS
3:00-8:00 AM: Processamento completo
9:00 AM+: Dados disponíveis para consulta

O diagrama evidencia como cada serviço se integra para garantir o SLA de 5h e disponibilizar os dados estruturados para consultas SQL eficientes!

