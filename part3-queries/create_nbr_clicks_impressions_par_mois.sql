-- Doc : https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions#extract
CREATE VIEW `test-startperf-469408.test_anisse.nbr_clicks_impressions_par_mois` AS
SELECT
  sum(gsc.clicks) as nb_clicks,
  sum(gsc.impressions) as nb_impressions,
  EXTRACT (MONTH FROM gsc.date) as mois
FROM
  `test-startperf-469408.test_anisse.GscData` as gsc
GROUP BY
  mois;
