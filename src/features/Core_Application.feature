Feature: Gerenciar Application

Scenario Outline: Eu, como Usuário Autenticado, quero cadastrar um(a) Application

Given Eu sou Usuário Autenticado
And preenchi os seguintes campos:
|Campo 1|
|Campo 2|
|Campo 3|
|Campo 4|

When os dados foram enviados para backend
Then o sistema responde com o <status> e a seguinte <mensagem>

Example:
|Status |mensagem                      |
|Sucesso|Cadastro realizado com sucesso|
|Error  |Cadastro Não Realizado        |


Scenario Outline: Eu, como Usuário Autenticado, quero atualizar a Application

Given Eu sou Usuário Autenticado
And selecionei uma instancia da entidade
And atualizei um dos seguintes campos:
|Campo 1|
|Campo 2|
|Campo 3|
|Campo 4|

When os dados foram enviados para backend
Then o sistema responde com o <status> e a seguinte <mensagem>

Example:
|Status |mensagem                          |
|Sucesso|Atualizado com sucesso com sucesso|
|Error  |Não Atualizado                    |

Scenario Outline: Eu, como Usuário Autenticado, quero deleter a <entidade>

Given Eu sou Usuário Autenticado
And selecionei uma instancia da entidade
When os dados foram enviados para backend
Then o sistema responde com o <status> e a seguinte <mensagem>

Example:
|Status |mensagem                        |
|Sucesso|Deletado com sucesso com sucesso|
|Error  |Não Deletado                    |


Scenario Outline: Eu, como Usuário Autenticado, quero buscar a Application

Given Eu sou Usuário Autenticado
And selecionei uma instancia da entidade
When os dados foram enviados para backend
Then o sistema responde com o <status> e a seguinte <mensagem>

Example:
|Status |mensagem               |
|Sucesso|Retorna a entidade     |
|Error  |Entidade não encontrada|


Scenario Outline: Eu, como Usuário Autenticado, quero buscar a Application

Given Eu sou Usuário Autenticado
And quero buscar todas as entidades
When os dados foram enviados para backend
Then o sistema responde com o <status> e a seguinte <mensagem>

Example:
|Status |mensagem          |
|Sucesso|Retorna a entidade|
