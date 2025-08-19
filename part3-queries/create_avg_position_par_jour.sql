CREATE VIEW `test-startperf-469408.test_anisse.avg_position_par_jour` AS
SELECT
  avg(gsc.position) as avg_position,
  gsc.date as date
FROM
  `test-startperf-469408.test_anisse.GscData` as gsc
GROUP BY
  gsc.date;
