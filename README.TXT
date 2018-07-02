# UNICEUB
 Material to support the course completion work focused on data analysis using mysql database, and python language to do analysis with IBGE data from 2010.

Tutorial de instalações de dependecias para execução dos scripts.

* Recomendavel usar a ultima versão do python 3.6



Banco de Dados MySQL: 

- Ativar o xampp ou mysql-server (manter o serviço ativado)
- Executar o script de criação do banco ou rodar o modelo lógico pelo workbench
- Baixar a pasta de csv em um diretorio local e capturar o caminho do repositorio local
- Editar o script de população no banco com o endereço dos csv
- Executar o script pelo cmd usando o comando de python.
  - Comando: python route_pop.py
- Verificar se os dados estão no banco de dados usando o mysql Workbench



python -m pip install --upgrade pip

python -m pip install jupyter
pip install pandas
pip install mysqlclient
pip install matplotlib


pip install dash==0.21.1
pip install dash-renderer==0.12.1
pip install dash-html-components==0.10.1
pip install dash-core-components==0.22.1
pip install dash-table-experiments
pip install plotly --upgrade


-> python app.py

* Caso ocorra de os graficos não serem plotados no sistema, verificar 
o banco de dados se o mesmo estão com dados, caso não esteja é necessario
que insira e aperte f5 para atualizar o navegador.




Navegador: http://127.0.0.1:8050/


