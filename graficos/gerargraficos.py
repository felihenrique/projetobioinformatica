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
def generate_peptides_points():
    point_x = np.array([])
    point_y = np.array([])
    for pacient_id in pacientes:
        cursor.execute("SELECT gene_name, mrna FROM expressaoRNA WHERE id_paciente=?", 
                       (pacientes_names[pacient_id],))
        for linha in cursor.fetchall():
            if (linha[0] != None):
                name = 'peptides_' + pacient_id
                qry = "SELECT " + name + " from proteinGroups WHERE gene_names='" + linha[0] + "'"
                cursor.execute(qry)
                result = cursor.fetchone() 
                if (result != None):
                    point_x = np.insert(point_x, 0, linha[1])
                    point_y = np.insert(point_y, 0, result[0])
    return point_x, point_y
