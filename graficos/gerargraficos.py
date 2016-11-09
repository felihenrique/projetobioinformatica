# -*- coding: utf-8 -*-

################## Configurações #########################
# Paciente para gerar o gráfico (deixe com 'todos' para gerar de todos os pacientes)

pacientes = ['aa3672']

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
def generate_points():
    mrna_list = np.array([])
    peptide_count_list = np.array([])
    score_list = np.array([])
	
    for pacient_id in pacientes:
        cursor.execute("SELECT gene_name, mrna FROM expressaoRNA WHERE id_paciente=?", 
                       (pacientes_names[pacient_id],))
        for linha in cursor.fetchall():
            if (linha[0] != None):
                names = 'peptides_' + pacient_id + ',' + 'intensity_' + pacient_id
                qry = "SELECT " + names + " from proteinGroups WHERE gene_names='" + linha[0] + "'"
                cursor.execute(qry)
                result = cursor.fetchone() 
                if (result != None):
                    mrna_list = np.insert(mrna_list, 0, linha[1])
                    peptide_count_list = np.insert(peptide_count_list, 0, result[0])
                    score_list = np.insert(score_list, 0, result[1])
    return mrna_list, peptide_count_list, score_list

def generate_score_graphic(pr, ps):
    plt.title('Score')
    plt.plot(pr, ps, 'ro')
    plt.savefig('score.png')
    
def generate_peptides_graphic(pr, ps):
    plt.title('Peptides')
    plt.plot(pr, ps, 'ro')
    plt.savefig('peptides.png')