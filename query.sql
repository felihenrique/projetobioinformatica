DROP TABLE IF EXISTS lista_num_aga002;
CREATE TABLE lista_num_aga002 (
   protein_id VARCHAR(50) UNIQUE DEFAULT(0),
   gene_names VARCHAR(50) DEFAULT(0),
   peptides INT DEFAULT(0),
   intensity BIGINT DEFAULT(0)
);
INSERT INTO lista_num_aga002 (protein_id, gene_names, peptides, intensity)
SELECT protein_id, gene_names, peptides_aga002, intensity_aga002
FROM proteinGroups, expressaoRNA
WHERE id_paciente='TCGA-AG-A002' AND gene_names = gene_name ORDER BY peptides_aga002 DESC;
DELETE FROM lista_num_aga002 WHERE protein_id LIKE '%;%';
.mode csv
.headers on
.output listas/numpeptideos/lista_aga002.txt
.separator \t
SELECT * FROM lista_num_aga002 LIMIT 500;
.output stdout