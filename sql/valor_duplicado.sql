SELECT DCB, Count(*) FROM nome_tabela
GROUP BY DCB
HAVING Count(*) > 1