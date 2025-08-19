-- Source : https://stackoverflow.com/questions/39109817/cannot-access-field-in-big-query-with-type-arraystructhitnumber-int64-time-in
-- https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#extract
CREATE VIEW `test-startperf-469408.test_anisse.avg_org_position_par_jour` AS
SELECT
  org_res.date as date,
  avg(org_res.position) as avg_organic_position
FROM
  `test-startperf-469408.test_anisse.ScaleserpData` as sed,
  UNNEST(result.organic_results) as org_res
GROUP BY
  date;
