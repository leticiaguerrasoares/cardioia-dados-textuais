# CardioIA — Fase 1: Dados Textuais (NLP)

**Aluna:** Leticia Guerra — RM: 567501
**Entrega individual da Fase 1 — "Batimentos de Dados" (Parte 2 – Dados Textuais / NLP).**

Corpus de textos clínicos brasileiros sobre doença cardiovascular, preparado para alimentar os módulos de **Processamento de Linguagem Natural (NLP)** das próximas fases do CardioIA. Esta é a peça textual que se soma às partes **numérica (IoT)** e **visual (Visão Computacional)** entregues pelo restante do grupo, todas ancoradas no mesmo domínio: o coração.

---

## 1. O que foi entregue

Um corpus de **4 textos** (`.txt`, UTF-8), **todos em português**, somando **~83 mil palavras**, cobrindo quatro recortes complementares do tema cardiovascular: **hipertensão** (e adesão ao tratamento), **infarto agudo do miocárdio**, **insuficiência cardíaca** e **prevenção/saúde pública**.

| # | Texto | Ano | Palavras | Tema | Fonte | Licença |
|---|-------|:---:|:-------:|------|-------|---------|
| 01 | O controle da hipertensão arterial em publicações brasileiras — Pinho & Pierin | 2013 | 2.771 | Hipertensão, saúde pública, adesão ao tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 02 | III Diretriz sobre Tratamento do Infarto Agudo do Miocárdio — SBC | 2004 | 77.068 | Infarto agudo do miocárdio: diagnóstico e tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 03 | Insuficiência Cardíaca — Barretto & Ramires | 1998 | 2.420 | Insuficiência cardíaca: fisiopatologia, sintomas e tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 04 | Prevenção de doenças cardiovasculares e promoção da saúde — Achutti | 2012 | 1.232 | Prevenção cardiovascular e promoção da saúde | SciELO / Ciênc. Saúde Coletiva | CC BY-NC 4.0 |

> **Requisito atendido:** o enunciado pede **no mínimo 2 textos** relacionados às doenças cardíacas, saúde pública, sintomas ou tratamentos — aqui são **4**, em português, com diversidade proposital de subtema (hipertensão, infarto, IC, prevenção) e de registro (revisão sistemática, diretriz clínica, artigo de atualização e artigo de debate). Essa variedade dá rótulos naturais para tarefas de NLP.

Os arquivos estão na subpasta **`docs/`** deste repositório. O catálogo de proveniência linha a linha está em **`docs/fontes.csv`**.

---

## 2. Origem e proveniência dos dados

Todos os textos vêm da **SciELO** (Scientific Electronic Library Online), uma das fontes expressamente sugeridas pelo enunciado — base pública, consolidada e citável de periódicos científicos brasileiros. São **artigos reais**, publicados em periódicos revisados por pares (Arquivos Brasileiros de Cardiologia e Ciência & Saúde Coletiva), **não** texto gerado nem de origem duvidosa.

Cada arquivo `.txt` traz, no seu próprio cabeçalho, os metadados completos de proveniência: título, autoria, periódico, ano, DOI, URL e licença. Um resumo está em `docs/fontes.csv`.

- **Texto 01 — Hipertensão / adesão (Pinho & Pierin, 2013).** Revisão sistemática sobre o controle da hipertensão no Brasil e a adesão ao tratamento no contexto do SUS. Traz o vocabulário de **saúde pública** e de **comportamento do paciente**.
- **Texto 02 — Infarto agudo do miocárdio (SBC, 2004).** Diretriz clínica extensa (~77 mil palavras) sobre diagnóstico e tratamento do IAM. É o núcleo de volume do corpus e a fonte mais densa em **sintomas, sinais, condutas e terminologia clínica**.
- **Texto 03 — Insuficiência cardíaca (Barretto & Ramires, 1998).** Artigo de atualização sobre fisiopatologia, história natural, sintomas (dispneia, cansaço, edema) e tratamento da IC.
- **Texto 04 — Prevenção / saúde pública (Achutti, 2012).** Artigo de debate sobre prevenção cardiovascular e promoção da saúde. Registro mais **argumentativo/opinativo**, útil para tarefas de sentimento e de classificação de tópico.

**Por que esta combinação?** Um corpus só de um subtema (ex.: só hipertensão) não permitiria treinar um classificador de tópicos; um corpus só de diretrizes seria homogêneo demais em registro. A escolha mistura, de propósito, **volume** (a diretriz de IAM), **diversidade de subtema** (hipertensão, infarto, IC, prevenção) e **diversidade de registro** (revisão, diretriz, atualização, debate) — exatamente o tipo de decisão de curadoria que o enunciado pede.

---

## 3. Justificativa: como estes textos serão analisados por NLP

O texto é a modalidade onde mais informação clínica fica "presa" em linguagem livre — laudos, evoluções, diretrizes, cartilhas. As tarefas de NLP previstas para as próximas fases do CardioIA, e como cada uma se apoia neste corpus:

**a) Classificação de tópicos.** Os quatro textos cobrem quatro subtemas distintos e rotuláveis (hipertensão, infarto, insuficiência cardíaca, prevenção). Isso dá rótulos naturais para treinar e avaliar um classificador — de modelos clássicos (TF-IDF + Naïve Bayes / SVM) a *embeddings* e *transformers* em português (ex.: **BERTimbau**). É a base para, no futuro, rotear automaticamente um documento clínico para a área certa.

**b) Extração de sintomas e entidades clínicas (NER).** A diretriz de infarto (texto 02) e o artigo de IC (texto 03) são densos em **sintomas e sinais** (dor torácica, dispneia, edema, cansaço, palpitação) e em **condutas e fármacos** (inibidores da ECA, diuréticos, betabloqueadores). Servem para prototipar **reconhecimento de entidades nomeadas** clínicas em português: extrair sintomas, achados, medicamentos e desfechos do texto corrido. Os sintomas extraídos podem depois ser cruzados com a variável `sintomas` da base numérica (Parte 1) e com as classes de ECG das imagens (Parte 3), integrando as três modalidades do projeto.

**c) Análise de sentimentos / de adesão.** O texto 01 discute **adesão ao tratamento**, crenças do paciente, abandono e barreiras; o texto 04 é **argumentativo**, com vocabulário de opinião. Juntos são o ponto de partida para análise de sentimento aplicada à saúde: medir, em relatos de pacientes ou mensagens de acompanhamento (fases futuras de assistência remota do CardioIA), sinais de baixa adesão, frustração ou risco de abandono do tratamento.

**d) Modelagem de linguagem e recuperação de informação.** O volume total (~83 mil palavras de texto clínico em português) permite estatística de linguagem (frequências, colocações, *n-grams*), construção de um **vocabulário do domínio cardiovascular em português** e uma base para busca semântica / RAG — um assistente que responde perguntas citando trechos das diretrizes.

**e) Sumarização.** A diretriz de IAM é longa e estruturada — insumo natural para tarefas de sumarização automática (resumir conduta clínica em poucos parágrafos), úteis para apoio à decisão.

### Importância para IA aplicada à saúde
Boa parte do conhecimento médico e do histórico do paciente é **texto não estruturado**. Um pipeline de NLP capaz de ler esse texto permite: transformar diretrizes e evoluções em dados estruturados para os modelos; triar automaticamente relatos por sintoma ou urgência; e, na ponta da assistência remota, detectar em linguagem natural o paciente que está abandonando o tratamento — que, como mostra o próprio texto 01, é onde o controle da hipertensão mais falha no Brasil. O ganho não é substituir o profissional: é **estruturar e priorizar** informação que hoje se perde no texto livre.

---

## 4. Governança de dados e viés

O enunciado pede atenção explícita à **Governança de Dados** e ao **viés**. Aplicado a este corpus textual:

**Proveniência e licença.** Fonte única, pública e rastreável (SciELO), com título, autoria, DOI e URL registrados no cabeçalho de cada arquivo e em `docs/fontes.csv`. Todos os quatro textos são **CC BY-NC 4.0** — uso acadêmico e **não comercial** permitido, com atribuição, que está preservada em cada arquivo. **Atenção de governança:** por serem *NonCommercial*, estes textos podem ser usados livremente no projeto acadêmico, mas **não** em um produto comercial sem nova autorização — restrição que precisa ser respeitada se o CardioIA evoluir para uso real.

**Dados pessoais (LGPD).** Os textos não contêm dados pessoais identificáveis de pacientes: são artigos científicos com dados **agregados** ou orientações clínicas gerais, sem nome, documento ou prontuário. Portanto não há tratamento de dado pessoal sensível de saúde na acepção da LGPD (art. 5º, II e art. 11). Se, nas próximas fases, o grupo incorporar laudos ou mensagens reais de pacientes, será obrigatório **anonimizar** (remover nome, documento, endereço e datas identificadoras) **antes** de qualquer processamento.

**Vieses conhecidos deste corpus — declarados, não escondidos:**

- **Desbalanceamento de volume.** A diretriz de infarto (texto 02) sozinha responde por ~92% das palavras. Um modelo treinado sem cuidado aprenderia sobretudo a linguagem de infarto. **Mitigação:** balancear por amostragem/peso ao treinar, e ampliar os demais subtemas antes de qualquer classificação séria.
- **Viés de registro.** Predomina o texto científico/erudito (diretriz, revisão). Falta a "voz do paciente" — linguagem coloquial, informal, com erros — justamente a que aparece na assistência remota. Coletar esse registro é passo previsto.
- **Viés temporal.** Os textos vão de 1998 a 2013. Condutas e fármacos evoluíram (as diretrizes já têm versões mais novas). São ótimos para linguagem e estrutura clínica, mas a **conduta atual** deve ser confirmada em fontes recentes antes de qualquer uso de apoio à decisão.
- **Viés geográfico/populacional.** Todos são brasileiros — o que é bom para o projeto —, mas com concentração de estudos na região Sudeste/Sul (visível já no texto 01). Um corpus representativo de todo o Brasil ainda precisa crescer (Norte e Nordeste sub-representados).
- **Viés de seleção do curador.** A escolha dos artigos reflete decisões minhas (disponibilidade, licença, tema). Está documentada aqui para ser auditável e revisável pelo grupo — como o próprio enunciado prevê.

**Vazamento de rótulo (label leakage).** Ao rotular estes textos por tópico para treino, o rótulo deve ficar em metadados (ex.: `fontes.csv`), **nunca** concatenado ao corpo do texto — senão o modelo "lê a resposta" em vez de aprender a linguagem. Pela mesma razão, o cabeçalho de metadados que adicionei em cada `.txt` deve ser removido antes de tarefas que não devam "ver" título/tema (o script de exemplo já ignora esse cabeçalho na estatística).

---

## 5. Estrutura do repositório

```
cardioia-dados-textuais/
├── README.md                       # este arquivo
├── .gitignore
├── docs/
│   ├── texto_01_pinho_pierin_controle_hipertensao_2013.txt
│   ├── texto_02_diretriz_infarto_agudo_miocardio_2004.txt
│   ├── texto_03_insuficiencia_cardiaca_1998.txt
│   ├── texto_04_prevencao_doencas_cardiovasculares_2012.txt
│   └── fontes.csv                  # catálogo/proveniência de cada texto
└── scripts/
    └── explorar_textos.py          # leitura + estatística básica de NLP (reprodutível)
```

---

## 6. Reprodução

Contagens e uma exploração inicial de NLP (frequência de termos, tamanho do vocabulário, ocorrência de termos clínicos) podem ser reproduzidas com Python 3 (só biblioteca padrão):

```bash
python3 scripts/explorar_textos.py
```

Os quatro textos foram coletados da SciELO pelas URLs registradas em `docs/fontes.csv` e no cabeçalho de cada arquivo, para auditoria da proveniência.

---

## 7. Observações finais

Como o próprio enunciado lembra, esta base pode ser revista pelo grupo ao longo do curso. As prioridades de evolução já estão mapeadas na seção 4: **balancear o volume entre subtemas**, **acrescentar registro de linguagem de paciente**, **atualizar as condutas com diretrizes recentes** e **anonimizar** quando entrarem dados reais. A base atual já é suficiente e legítima para os experimentos de NLP das próximas fases, é toda em português (alinhada ao público-alvo brasileiro do CardioIA) e mantém coerência com as partes numérica e visual do projeto.
