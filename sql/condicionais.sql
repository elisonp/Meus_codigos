/* Seleciona a nota
 Caso quando a nota for 11111, retorne o valor 'one' na coluna CASE
 caso seja 2, retorne two
 Se não atenteder nenhuma das condições, retorne other
 fim
*/
SELECT nota,
       CASE WHEN nota ='11111' THEN 'one'
            WHEN nota ='2' THEN 'two'
            ELSE 'other'
       END
    FROM v360.notas_fiscais nf ;

 -- Subquery
 -- Retorna Uma query, contanto que re
 select * 
 from v360.notas_fiscais nf 
 where exists (select * from v360.notas_fiscais_1 nf2  where nota = '11111')



-- Comparar se um valor não existe, caso exista, ele não fará nada,
-- Caso não tenha o valor, ele irá inserir um nova linha

DO
$do$
BEGIN
   IF not EXISTS (select *  FROM v360.notas_fiscais_1 nf where nota = '3' ) THEN
      INSERT INTO v360.notas_fiscais_1  VALUES ('1','5','2022-05-05','3');
   END IF;
END
$do$