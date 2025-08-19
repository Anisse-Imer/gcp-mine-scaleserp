CREATE VIEW `test-startperf-469408.test_anisse.avg_positions_ctr_par_jour` AS
SELECT
  avg(gsc.position) as avg_positions,
  avg(gsc.clicks / gsc.impressions) as avg_ctr,
  date
FROM
  `test-startperf-469408.test_anisse.GscData` as gsc
GROUP BY
  date;
