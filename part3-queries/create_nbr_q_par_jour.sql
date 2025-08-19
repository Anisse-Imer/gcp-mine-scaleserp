CREATE VIEW `test-startperf-469408.test_anisse.nbr_q_par_jour` AS
SELECT
  sed.result.search_metadata.created_at as date,
  count(sed.search.q) as nbr_q
FROM
  `test-startperf-469408.test_anisse.ScaleserpData` sed
GROUP BY
  sed.result.search_metadata.created_at;
