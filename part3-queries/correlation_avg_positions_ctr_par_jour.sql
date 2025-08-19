-- Correlation : Plus la position augmente, plus le ctr se rapproche de 0.
SELECT
  *
FROM
  `test-startperf-469408.test_anisse.avg_positions_ctr_par_jour`
ORDER BY 
  avg_positions;
