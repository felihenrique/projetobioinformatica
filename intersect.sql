.mode csv
.headers on
.output listas/numpeptideos/lista_interseccao.txt
.separator \t

create TEMPORARY table temp1 as select protein_id from lista_num_aa3710 limit 500;
create TEMPORARY table temp2 as select protein_id from lista_num_aa3864 limit 500;
create TEMPORARY table temp3 as select protein_id from lista_num_aaa00n limit 500;
create TEMPORARY table temp4 as select protein_id from lista_num_aga002 limit 500;
create TEMPORARY table temp5 as select protein_id from lista_num_aa3715 limit 500;
create TEMPORARY table temp6 as select protein_id from lista_num_aaa00j limit 500;
create TEMPORARY table temp7 as select protein_id from lista_num_aaa010 limit 500;
create TEMPORARY table temp8 as select protein_id from lista_num_aa3672 limit 500;

select * from temp1 intersect
select * from temp2 intersect
select * from temp3 intersect
select * from temp4 intersect
select * from temp5 intersect
select * from temp6 intersect
select * from temp7 intersect 
select * from temp8;

drop table temp1;
drop table temp2;
drop table temp3;
drop table temp4;
drop table temp5;
drop table temp6;
drop table temp7;
drop table temp8;

.output stdout