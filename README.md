# Este repositório contém: 


1. 99 arquivos com códigos **Python** (_.py_)  desenvolvidos para exercitar lógica de programação essencial juntamente com funcionalidades da linguagem. 

2. 1 arquivo  **"descreveProgramas.md"** : que contém um índice com as descrições dos 99 códigos, mostrando o que cada um faz.

3. Este arquivo **README.md**, onde você pode encontrar orientações sobre a finalidade do repositório e maneiras sugeridas para melhor explorá-lo.

4. 2 imagens:  "**estrutura_codigo.png**_" e "_**estrutura_pasta.png**_" que são utilizadas neste arquivo README.md , mais abaixo, para exemplicar o que está sendo descrito no conteúdo. 



#  Este repositório tem a finalidade de:


1. Servir como meu material de apoio para relembrar conceitos, sintaxes, bibliotecas e funções úteis na linguagem, através de exemplos práticos, com códigos organizados e conteúdo visualmente fácil de encontrar.
2. mostrar um pouco dos meus conhecimentos, da minha evolução e forma de pensar Python e programação
3. contribuir com a comunidade compartilhando conhecimento prático, e também me abrir para aprendizados e contribuições



# Para melhor explorá-lo, como principal sugestão, siga os passos abaixo:




1. Clique em algum dos 99 arquivos .py que deseja visualizar - você pode ler todas as descrições do que faz cada programa no arquivo "descreveProgramas.md"
2. Copie o código inteiro.
3. Abra o Google Colab: https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index#recent=true
4. Crie um Novo Notebook
5. Cole o código inteiro copiado na primeira linha de comando que vai aparecer no Notebook criado
6. Aperte play, primeiro botão em frente a linha de comando do código que colou
7. Veja o código sendo executado, interaja, estude a estrutura e faça bom proveito.



Para as finalidades deste repositório, foi escolhido o Google Colab por ser simples, intuitivo, além de eliminar a necessidade de instalação de pacotes básicos necessários para rodar códigos. Todos os 99 códigos foram testados seguindo os passos acima. 

Caso queira baixar os arquivos e executá-los em seu terminal, em alguns casos você precisará instalar bibliotecas utilizadas em determinados códigos, e também sinta-se livre para alterar os nomes dos arquivos, pois sei que ficaram extensos, mas assim foram feitos única e propositalmente para atender as finalidades deste repositório. Também, vale ressaltar que os textos das strings dos códigos estão em português, e algumas vezes, dependendo das configurações da máquina que está usando, seu terminal poderá encontrar conflitos semânticos devido a questoes de configuração de linguagem ASCII



## **Como foram organizados os conteúdos** e por que:

A organização dos arquivos e a escolha das legendas foram pensadas conforme as finalidades mencionadas acima, de fazer deste repositório apoio prático para revisitar conceitos e sintaxes da linguagem, por isso os nomes dos arquivos .py não seguem uma convenção - tão menos devem ser recomendados como boas práticas - mas para esta finalidade mencionada acima, e seguindo todas as orientações de quais ferramentas utilizar para evitar erros e explorar o conteúdo da melhor maneira, acredito que a proposta das estruturas das legendas tenha sido boa. 

Estas legendas dos arquivos seguem a evolução dos estudos de lógica de programação com Python conforme tópicos abaixo, que poderão ser encontrados dentro de cada arquivo ao qual faz a descrição:



- Manipulação de Strings
- Condições - If / Else
- Condições Aninhadas - Elif
- Estrutura de repetição FOR
- Estrutura de repetição WHILE
- Interrompendo repetições WHIL E com Break
- Estrutura de repetição WHILE TRUE
- Tuplas
- Listas
- Dicionários
- Funções

Veja abaixo um print da pasta, com as legendas dos arquivos mencionando os tópicos de estudo acima. 

![estrutura_pasta](/Users/leandropeixoto/Desktop/99-python-codes/estrutura_pasta.png)



Dentro de cada um dos arquivos, existem comentários que separam e organizam o código seguindo basicamente a estrutura abaixo: 

1. Recebe dados - Inputs

2. Manipula dados 

3. Retorna dados - Outputs

Esta estrutura pode ser encontrada como #comentário em cada código deste repositório, como no exemplo abaixo, do arquivo "06 - Condições - Calcule a multa", onde estão marcados os retângulos pretos, que separam o código conforme estrutura mencionada acima:



![estrutura_codigo](/Users/leandropeixoto/Desktop/99-python-codes/estrutura_codigo.png)



Neste programa da imagem usado como exemplo, o desafio era criar um sistema que recebesse a velocidade de um carro, e calculasse a multa conforme condições especificadas. Logo, como dados de entrada, o programa **receberia os dados** - velocidade do carro e velocidade permitida - e, partir dela e com as condições especificadas, calcularia o valor da multa, ou seja, **manipularia os dados** (velocidade) e criaria novos dados (multa) a partir daqueles imputados; e por último **retornaria os novos dados** - no caso o valor da multa - para o usuário. 

Esta é a estrutura de raciocínio que tento utilizar para me organizar com a estrutura dos códigos de programas que desenvolvo, pois entendo que, alguns requisitos básicos para o funcionamento de um programa, de uma forma bem geral, incluem estas 3 etapas: receber dados - e/ou instruções, manipular dados - e/ou criar novos dados,  e retornar dados. 



Nos arquivos finais deste repositório, de códigos com funções, a estrutura separadora de código utilizada foi basicamente:

1. Cria função
2. Usa função

ou seja, antes de iniciar o programa, eu crio as funções que serão necessárias para em seguida utilizá-las. 



