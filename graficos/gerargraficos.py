# -*- coding: utf-8 -*-

################## Configurações #########################
# Paciente para gerar o gráfico (deixe com 'todos' para gerar de todos os pacientes)

pacientes = ['aa3672', 'aa3710', 'aa3715', 'aa3864', 'aaa00j', 'aaa00n', 'aaa010', 'aga002']

####################################################################################

import sqlite3
import matplotlib.pyplot as plt
import numpy as np

pacientes_names = {
                   'aa3672' : 'TCGA-AA-3672',
                   'aa3710' : 'TCGA-AA-3710',
                   'aa3715' : 'TCGA-AA-3715',
                   'aa3864' : 'TCGA-AA-3864',
                   'aaa00j' : 'TCGA-AA-A00J',
                   'aaa00n' : 'TCGA-AA-A00N',
                   'aaa010' : 'TCGA-AA-A010',
                   'aga002' : 'TCGA-AG-A002'                   
                   }
             
                   #'aaa01r' : 'TCGA-AA-A01R',
                   #'aaa022' : 'TCGA-AA-A022',
                   #'aga02n' : 'TCGA-AG-A02N'
con = sqlite3.connect("../banco.db")
cursor = con.cursor()

def gerar_sql(name1, name2):
    query = """DROP TABLE IF EXISTS lista_{0};
CREATE TABLE lista_{0} (
   protein_id VARCHAR(50) UNIQUE DEFAULT(0),
   gene_names VARCHAR(50) DEFAULT(0),
   peptides INT DEFAULT(0),
   intensity BIGINT DEFAULT(0)
);
INSERT INTO lista_aa3672 (protein_id, gene_names, peptides, intensity)
SELECT protein_id, gene_names, peptides_{0}, intensity_{0}
FROM proteinGroups, expressaoRNA
WHERE id_paciente='{1}' AND gene_names = gene_name ORDER BY intensity_{0} DESC;
DELETE FROM lista_{0} WHERE protein_id LIKE '%;%';
.mode csv
.headers on
.output ../listas/intensidade/lista_{0}.txt
.separator \\t
SELECT * FROM lista_{0} LIMIT 500;
.output stdout
""".format(name1, name2)
    f = open('../consultas_sql/lista_{0}.sql'.format(name1), 'w+')
    f.writelines(query)

def gerar_coordenadas(paciente_id):
    q = """SELECT mrna, peptides_"""+paciente_id+""", intensity_"""+paciente_id+""" FROM expressaoRNA, proteinGroups 
    WHERE id_paciente='"""+pacientes_names[paciente_id]+"""' 
    AND proteinGroups.gene_names=expressaoRNA.gene_name"""
    cursor.execute(q)
    mt = np.array(cursor.fetchall())
    return mt[:, 0], mt[:, 1], mt[:, 2]
    
def gerar_grafico_intensidade(prn, pin, paciente_id):
    plt.clf()
    plt.title('Intensidade x mRNA ' + paciente_id)
    plt.xlabel('mRNA')
    plt.ylabel('Intensidade')
    plt.plot(prn, pin, 'ro')
    plt.savefig('intensidade_'+paciente_id+'.png')
    
def gerar_grafico_peptideos(arr_rna, arrnum, paciente_id):
    plt.clf()
    plt.title('Número de peptideos x mRNA ' + paciente_id)
    plt.xlabel('mRNA')
    plt.ylabel('Número de peptídeos')
    plt.plot(arr_rna, arrnum, 'ro')
    plt.savefig('peptides_'+paciente_id+'.png')
    
def gerar_graficos_todos():
    for p_id in pacientes:
        gerar_graficos_paciente(p_id)
        
def gerar_graficos_paciente(p_id):
    prna, pnum, pintensidade = gerar_coordenadas(p_id)
    gerar_grafico_peptideos(prna, pnum, p_id)
    gerar_grafico_intensidade(prna, pintensidade, p_id)
    
        
        