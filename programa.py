# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:17:00 2016

@author: Felipe
"""

import sqlite3

con = sqlite3.connect("banco.db")
cursor = con.cursor()

cursor.execute("SELECT gene_names, peptide_count FROM proteinGroups WHERE gene_names='ABAT'")

#cursor.execute("SELECT * FROM proteinGroups WHERE gene_names='ABAT'")

for linha in cursor.fetchall():
    print(linha)
