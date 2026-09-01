# CardioIA — Fase 1: Dados Textuais (NLP)

**Aluna:** Leticia Guerra — RM: 567501

**Entrega da Fase 1 — "Batimentos de Dados" (Parte 2 – Dados Textuais / NLP).**

---

## 1. O que foi entregue

Quatro textos em `.txt`, retirados da SciELO, sobre quatro assuntos: hipertensão, infarto, insuficiência cardíaca e prevenção cardiovascular. Juntos somam cerca de 83 mil palavras. Os arquivos ficam na pasta `docs/`, e a origem de cada um está registrada em `docs/fontes.csv`.

| # | Texto | Ano | Palavras | Tema | Fonte | Licença |
|---|-------|:---:|:-------:|------|-------|---------|
| 01 | O controle da hipertensão arterial em publicações brasileiras — Pinho & Pierin | 2013 | 2.771 | Hipertensão, saúde pública, adesão ao tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 02 | III Diretriz sobre Tratamento do Infarto Agudo do Miocárdio — SBC | 2004 | 77.068 | Infarto agudo do miocárdio: diagnóstico e tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 03 | Insuficiência Cardíaca — Barretto & Ramires | 1998 | 2.420 | Insuficiência cardíaca: fisiopatologia, sintomas e tratamento | SciELO / Arq. Bras. Cardiol. | CC BY-NC 4.0 |
| 04 | Prevenção de doenças cardiovasculares e promoção da saúde — Achutti | 2012 | 1.232 | Prevenção cardiovascular e promoção da saúde | SciELO / Ciênc. Saúde Coletiva | CC BY-NC 4.0 |

> **Requisito atendido:** O enunciado pede pelo menos dois textos. Escolhi quatro, de assuntos e tipos diferentes (uma revisão, uma diretriz clínica, um artigo de atualização e um artigo de opinião), para ter mais material e mais variedade nas análises.

Os arquivos estão na subpasta **`docs/`** deste repositório. O catálogo de proveniência linha a linha está em **`docs/fontes.csv`**.

---

## 2. Origem e proveniência dos dados

Todos os textos vêm da **SciELO** (Scientific Electronic Library Online), uma das fontes indicadas no enunciado — base pública, consolidada e citável de periódicos científicos brasileiros. São **artigos reais**, publicados em periódicos revisados por pares (Arquivos Brasileiros de Cardiologia e Ciência & Saúde Coletiva), **não** texto gerado nem de origem duvidosa.

Cada arquivo `.txt` começa com um cabeçalho que informa título, autores, revista, ano, DOI, link e licença. Essas mesmas informações estão reunidas em **`docs/fontes.csv`**, para conferência rápida.

- **Texto 01 — Hipertensão e adesão (Pinho & Pierin, 2013).** Revisão sobre o controle da hipertensão no Brasil e a adesão ao tratamento no SUS. Traz o vocabulário de saúde pública e do comportamento do paciente.
- **Texto 02 — Infarto (SBC, 2004).** Diretriz clínica extensa (~77 mil palavras) sobre diagnóstico e tratamento do infarto. É o texto mais denso em sintomas, sinais e condutas.
- **Texto 03 — Insuficiência cardíaca (Barretto & Ramires, 1998).** Artigo de atualização sobre a doença, com muitos sintomas citados (falta de ar, cansaço, inchaço) e opções de tratamento.
- **Texto 04 — Prevenção (Achutti, 2012).** Artigo de opinião sobre prevenção cardiovascular e saúde pública, com um tom mais argumentativo.

Procurei juntar textos de tamanhos, assuntos e estilos diferentes de propósito: a diretriz de infarto dá volume, e os outros três trazem outros temas e outros jeitos de escrever. Assim dá para treinar e comparar tarefas de NLP, e não só cumprir o mínimo pedido.

---

## 3. Como esses textos podem ser usados em NLP

**Classificação de tópicos.** Como cada texto trata de um assunto diferente, dá para usá-los como exemplos rotulados e treinar um modelo que identifique o tema de um documento novo — de métodos mais simples (TF-IDF com Naïve Bayes ou SVM) a modelos em português como o **BERTimbau**.

**Extração de sintomas.** A diretriz de infarto e o artigo de insuficiência cardíaca têm muitos sintomas e medicamentos citados (dor no peito, falta de ar, inchaço, cansaço). Servem para testar a extração automática dessas informações do texto. Depois, os sintomas encontrados podem ser cruzados com a coluna de sintomas da base numérica (Parte 1) e com as classes de ECG das imagens (Parte 3).

**Análise de sentimento e de adesão.** O texto sobre hipertensão fala de adesão ao tratamento e de abandono; o de prevenção tem um tom mais opinativo. Dão uma base para, mais adiante, identificar em mensagens de pacientes sinais de que a pessoa está deixando de se cuidar.

**Vocabulário e busca.** Com o total de palavras dá para estudar os termos mais comuns da área e montar uma busca que responda perguntas citando trechos das diretrizes.

---

## 4. Por que isso importa para a saúde

Grande parte das informações médicas está solta em texto: diretrizes, laudos, anotações. Conseguir ler esse texto automaticamente ajuda a organizar essas informações, separar casos por sintoma ou urgência e, no atendimento a distância, perceber quem está abandonando o tratamento — que é justamente onde o controle da hipertensão mais falha no Brasil, como mostra o primeiro texto. Vale lembrar que os textos são para estudo e testes, **não** para diagnóstico nem decisão médica.

---

## 5. Governança de dados e viés

**Origem e licença.** A fonte é uma só, pública e fácil de rastrear (SciELO). Cada arquivo guarda o título, os autores, o DOI e o link, e tudo está resumido em `docs/fontes.csv`. Os quatro textos têm licença **CC BY-NC 4.0**, que permite usar em trabalho acadêmico, sem fins comerciais e com crédito ao autor. Por não permitir uso comercial, não poderiam entrar num produto pago sem nova autorização.

**Dados pessoais.** Nenhum texto traz dados de pacientes que permitam identificá-los. São artigos com números gerais ou orientações clínicas, sem nome, documento ou prontuário. Se mais para frente o grupo usar laudos ou mensagens reais, será preciso anonimizar antes de qualquer análise, seguindo a LGPD.

**Vieses que percebi:**

- Um texto (a diretriz de infarto) é muito maior que os outros e concentra quase todas as palavras. Na hora de treinar, é bom equilibrar isso e trazer mais textos dos outros assuntos.
- Todos são textos científicos. Falta a forma como o paciente comum escreve, que é o que aparece no atendimento a distância.
- Os artigos são de 1998 a 2013, e algumas condutas médicas já mudaram. São ótimos para a linguagem, mas o tratamento atual precisa ser conferido em fontes mais novas.
- Todos são brasileiros, mas a maioria dos estudos é do Sudeste e do Sul; Norte e Nordeste aparecem pouco.

> **Cuidado ao rotular.** Quando for marcar os textos por assunto para treinar um modelo, o rótulo deve ficar guardado à parte (no `fontes.csv`), nunca dentro do texto — senão o modelo "cola" a resposta em vez de aprender. Pelo mesmo motivo, o cabeçalho que coloquei no começo de cada arquivo deve ser retirado antes desse tipo de teste. O script de exemplo já desconsidera esse cabeçalho nas contagens.

---

## 6. Estrutura do repositório

| Caminho | Conteúdo |
|---------|----------|
| `README.md` | Este arquivo |
| `.gitignore` | Arquivos ignorados pelo Git |
| `docs/texto_01_pinho_pierin_controle_hipertensao_2013.txt` | Texto 01 — hipertensão |
| `docs/texto_02_diretriz_infarto_agudo_miocardio_2004.txt` | Texto 02 — infarto |
| `docs/texto_03_insuficiencia_cardiaca_1998.txt` | Texto 03 — insuficiência cardíaca |
| `docs/texto_04_prevencao_doencas_cardiovasculares_2012.txt` | Texto 04 — prevenção |
| `docs/fontes.csv` | Catálogo com a origem de cada texto |
| `scripts/explorar_textos.py` | Script de exploração dos textos (NLP) |

---

## 7. Como reproduzir

Com Python 3 (só a biblioteca padrão), o script faz uma exploração rápida dos textos — palavras mais frequentes, tamanho do vocabulário e ocorrência de termos clínicos. Basta rodar `python3 scripts/explorar_textos.py` no terminal, a partir da pasta do projeto.

Os quatro textos foram baixados da SciELO pelos links que estão em `docs/fontes.csv` e no começo de cada arquivo.
