-- Source : https://stackoverflow.com/questions/39109817/cannot-access-field-in-big-query-with-type-arraystructhitnumber-int64-time-in
CREATE VIEW `test-startperf-469408.test_anisse.avg_org_position_par_jour_samboat` AS
SELECT
  org_res.domain as domain,
  org_res.date as date,
  avg(org_res.position) as avg_organic_position
FROM
  `test-startperf-469408.test_anisse.ScaleserpData` as sed,
  UNNEST(result.organic_results) as org_res
WHERE
  org_res.domain like "%www.samboat.fr%"
  and org_res.date is not null
  and org_res.date not like "%Location%"
GROUP BY
  domain, date;
