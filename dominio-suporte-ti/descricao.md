Descrição do Dashboard

Este dashboard foi criado para a empresa fictícia Domínio Consultoria Empresarial, com o objetivo de monitorar a performance do setor de TI, especialmente no que diz respeito ao atendimento de chamados.

A base de dados foi gerada com a ajuda de inteligência artificial (conforme o script em "script_geracao_base.txt") e está hospedada no SharePoint. Ela contém as seguintes informações:

ID: Código de 6 dígitos gerado sequencialmente.
SOLICITANTE: Nome e sobrenome fictícios representando os funcionários da empresa.
EMAIL_SOLICITANTE: E-mail fictício, seguindo o padrão "nome.sobrenome@dominio.com".
SETOR: Definido aleatoriamente entre 8 opções.
TIPO_CHAMADO: Definido aleatoriamente entre 6 opções.
DESCRIÇÃO DO CHAMADO: Descrição gerada por inteligência artificial.
DATA_CRIAÇÃO: Data aleatória no intervalo de 01/01/2020 a 30/09/2024.
HORA_CRIAÇÃO: Horário aleatório entre 00:00 e 23:59.
UNIDADE: Definida aleatoriamente entre as capitais do Brasil.
ATENDENTE: Nome aleatório entre 6 opções, simulando a equipe de TI.
EMAIL_ATENDENTE: E-mail fictício para a equipe de TI, seguindo o padrão "nome.sobrenome@dominio.com".
DATA_CONCLUSÃO: Gerada aleatoriamente até 5 dias após a DATA_CRIAÇÃO.
HORA_CONCLUSÃO: Horário aleatório entre 00:00 e 23:59.
SLA_DIAS: Diferença entre a DATA_CRIAÇÃO e a DATA_CONCLUSÃO, indicando a quantidade de dias que o chamado ficou em aberto.
STATUS: Definido aleatoriamente entre as opções: AGUARDANDO ATENDIMENTO, EM ANDAMENTO, FINALIZADO.
Para o processo de transformação dos dados no Power BI, foram realizados os seguintes tratamentos:

Conversão de texto para maiúsculas.
Definição do padrão de data (MM/DD/YYYY) e hora (00:00).
Separação das datas para visualização de meses e anos.
Agrupamento das unidades por região (Sudeste, Nordeste, Sul, etc.).
Definição de prazo para o SLA e classificação como "no prazo" ou "fora do prazo".
Em seguida, foram definidas as visões necessárias para o acompanhamento, onde optei por manter:

Por Período: Permite acompanhar a evolução por ano, mês e semana. Essa visão proporciona insights sobre períodos que demandam maior atenção do setor de TI.
Por Região/Setor: Acompanhamento dos tipos de chamados por setor ou região do país, possibilitando identificar quais setores necessitam de mais apoio em tipos específicos de chamados.
Performance do Setor de TI: Visão focada na gestão de TI, que permite monitorar a performance por colaborador, incluindo a quantidade de chamados atendidos em determinado período e a quantidade de chamados em aberto, dentro ou fora do prazo.
BASE: Visão global da base de dados utilizada, onde é possível aplicar filtros para uma análise macro sobre os tipos de chamados, períodos ou regiões específicas.