# Fome Zero
## Problema de negócio
A empresa Fome Zero é um marketplace de restaurantes que tem por objetivo facilitar o encontro de clientes e restaurantes. O CEO da empresa foi recém-contratado e possui a necessidade de entender melhor o funcionamento do negócio para conseguir tomar as melhores decisões, com base nessa demanda surgiu a análise dos dados baseados em 5 visões: Geral, País, Cidade, Restaurantes e Culinárias.

## Premissas assumidas para análise
1.	A análise foi realizada com dados de dataset da plataforma Kaggle
2.	As culinárias dos restaurantes foram reduzidas a apenas uma.
3.	O dataset não é sincronizado automaticamente

## Estratégia da solução
O dashboard foi desenvolvido utilizando as principais métricas referente a cada visão:
1.	Geral
  *	Restaurantes cadastrados
  *	Países cadastrados
  *	Cidades
  *	Avaliações feitas
  *	Culinárias

2.	Países
  *	Restaurantes por país
  *	Cidades por país
  *	Média de avaliação por país
  *	Valor médio para duas pessoas

3.	Cidades
  *	10 cidades com mais restaurantes
  *	7 cidades com restaurantes com nota média acima de 4.0
  *	7 cidades com restaurantes com nota média abaixo de 2.50
  *	10 cidades com mais culinárias distintas

4.	Culinárias
Nesta visão existe um filtro extra no menu a esquerda, sendo possível alterar a quantidade de exibições, por padrão ele é iniciado em 10.
  *	Top 10 restaurantes com maiores avaliações
  *	Top 10 melhores tipos de culinárias
  *	Top 10 piores tipos de culinárias
  
# Insights
  1.	Restaurantes melhores avaliados não estão concentrados em apenas uma região geográfica, inclusive são dispersos em diferentes continentes
  2.	A mesma cidade pode conter os melhores restaurantes avaliados e os piores restaurantes avaliados
  3.	O continente americano ocupa 39% da base de dados

## Produto
Dashboard online e interativo, hospedado em um serviço de Cloud para acesso em qualquer dispositivo com acesso à internet.
O dashboard pode ser acessado através do link: https://luizfernandodelchello-fome-zero.streamlit.app/ 

## Conclusão
O objetivo do projeto é criar um dashboard para visualização de métricas da empresa. Da visão empresarial é possível visualizar a distribuição geográfica dos restaurantes, quais os melhores e piores índices de avaliações e números absolutos de itens na base de dados.

## Próximos passos
1.	Criar filtros
2.	Modularizar as funções utilizadas em um arquivo separado do código da página
3.	Acrescentar informações novas ao popup dos restaurantes
4.	Implementar sistema de cores no pin do restaurante com base em sua avaliação

