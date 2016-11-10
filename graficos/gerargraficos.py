# -*- coding: utf-8 -*-

################## Configurações #########################
# Paciente para gerar o gráfico (deixe com 'todos' para gerar de todos os pacientes)

pacientes = ['aa3672', 'aa3710', 'aa3715', 'aa3864', 'aaa00j', 'aaa00n', 'aaa010', 'aaa01r', 
             'aaa022', 'aga002', 'aga02n']

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
                   'aaa01r' : 'TCGA-AA-A01R',
                   'aaa022' : 'TCGA-AA-A022',
                   'aga002' : 'TCGA-AG-A002',
                   'aga02n' : 'TCGA-AG-A02N'
                   }
# plt.plot(px, py, 'ro')
con = sqlite3.connect("../banco.db")
cursor = con.cursor()
def gerar_coordenadas(paciente_id):
    mrna_list = np.array([])
    peptide_count_list = np.array([])
    intensidade_list = np.array([])
    q = "SELECT gene_name, mrna FROM expressaoRNA WHERE id_paciente='"+pacientes_names[paciente_id]+"'"
    cursor.execute(q)
    for linha in cursor.fetchall():
        if (linha[0] != None):
            names = 'peptides_' + paciente_id + ',' + 'intensity_' + paciente_id
            qry = "SELECT " + names + " from proteinGroups WHERE gene_names='" + linha[0] + "'"
            cursor.execute(qry)
            result = cursor.fetchone() 
            if (result != None):
                mrna_list = np.insert(mrna_list, 0, linha[1])
                peptide_count_list = np.insert(peptide_count_list, 0, result[0])
                intensidade_list = np.insert(intensidade_list, 0, result[1])
    return mrna_list, peptide_count_list, intensidade_list

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
        
def gerar_grafico_todos():
    for p_id in pacientes:
        prna, pnum, pintensidade = gerar_coordenadas(p_id)
        gerar_grafico_peptideos(prna, pnum, p_id)
        gerar_grafico_intensidade(prna, pintensidade, p_id)
        
        