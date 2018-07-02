import csv
import MySQLdb
import pandas as pd

if __name__ == '__main__':

 conn = MySQLdb.connect(
  host="localhost", user="root", 
  passwd="", db="municipiostcc")
 cur = conn.cursor()
 caminho = [
  r'C:\Users\italo.oliveira\Downloads\CSV\regiao.csv',
  r'C:\Users\italo.oliveira\Downloads\CSV\uf.csv',
  r'C:\Users\italo.oliveira\Downloads\CSV\municipio.csv']
 sql_regiao = ("INSERT INTO regiao (idREGIAO,NomeR) VALUES (%s,%s)")
 sql_uf = ("INSERT INTO uf (idUF,SiglaUF,REGIAO_idREGIAO)"+ 
             "VALUES (%s,%s,%s)")
 sql_municipio = ("INSERT INTO municipio("+
  "idMUNICIPIO,NomeM,POP_2010,POP_2013,POP_2014,"
  "POP_2015,POP_2016,QTD_IES,IDH_2010,GINI_2010,"
  "PIB_2010,PERCAPITA_2010,UF_idUF)"
  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
 for file in caminho:
   if("regiao" in file):
    with open(file,encoding='UTF8') as csvfile:
     reader = csv.DictReader(csvfile, delimiter = ',')
     for row in reader:
      cur.executemany(sql_regiao,[(row['idREGIAO'],row['NomeR'])])
      conn.escape_string(sql_regiao)
     conn.commit()
   elif("uf" in file):
    with open(file,encoding='UTF8') as csvfile:
     reader = csv.DictReader(csvfile, delimiter = ',')
     for row in reader:
      cur.executemany(sql_uf,
	   [(row['idUF'],row['SiglaUF'],row['REGIAO_idREGIAO'])])
      conn.escape_string(sql_uf)
     conn.commit()
   elif("municipio" in file):
    with open(file,encoding='UTF8') as csvfile:
     reader = csv.DictReader(csvfile, delimiter = ',')
     for row in reader:
      cur.executemany(sql_municipio,
	  [( row[U'idMUNICIPIO'],row[U'NomeM'],
	   row[U'POP_2010'],row[U'POP_2013'],
	   row[U'POP_2014'],row[U'POP_2015'],
	   row[U'POP_2016'],row[U'QTD_IES'],
	   row[U'IDH_2010'],row[U'GINI_2010'],
	   row[U'PIB_2010'],row[U'PERCAPITA_2010'],
	   row[r'UF_idUF'] )])
      conn.escape_string(sql_municipio)
     conn.commit()
   else:
    print("Fim")
print ("Concluído")