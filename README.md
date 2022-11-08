# Fundamentos de Programação

## Este repositório encontra-se separado em:
- **Teóricas:** Exemplos feitos em aula
- **Práticas:** Exercícios feitos nas aulas práticas ou Exercícios disponíveis no livro da disciplina "Programação em Python: Introdução à programação com múltiplos paradigmas"
- **Projetos:** Ficheiro que contém o projeto atual em desenvolvimento e os unit testes associados
    - **Dúvidas:**
        - Nas docstrings é suposto referirmo-nos aos nossos TADs como tipos de dados ou continuar a denotar a nossa própria representação (Ex: o return da função coordenadas_vizinhas deve ser do tipo tuple com elementos do tipo 'coordenada' ou tuple com elementos do tipo tuple compostos por um elemento do tipo do string e outro do tipo int, como é no meu caso)
        - Nas docstrings das funções de alto nível referimo-nos ao TAD a nossa implementação ou simplesmente ao seu nome (Ex: em alterna_bandeira dizemos que o tipo de p é parcela ou que definimos)
       - Podemos usar funções definidas posteriormente a uma certa função? Ou apenas podemos usar as que vêem anteriormente ao ponto onde estamos? Podemos usar funções de alto nível de outros TADs na definição de operações básicas de um TAD diferente? (Ex: obtem_numero_minas_vizinhas)
       - Dúvidas sobre limpa_campo relativamente a parcelas com estado "marcada" quando são as coordenadas dadas (se devemos limpar as restantens tal como fariamos para uma parcela "tapada") e quando são coordenadas vizinhas (se devemos limpá-las quando não têm minas na vizinhança) 
       - Consideramos que um state máximo para um gerador é 0xFFFFFFFF para 32 bits e 0xFFFFFFFFFFFFFFFF para 64 bits?
       - As funçoes _iguais() é suposto verificarem se a adress das variáveis dadas é a mesma?
    - **Optimização:**
        - Criar uma função universal que verifica se as linhas e colunas estão válidas