CREATE VIEW `test-startperf-469408.test_anisse.nbr_search_domain_pour_location_bateau` AS
SELECT
  count(*) as nbr_search_domain,
  org_res.domain as domain,
  sed.search.q as q
FROM
  `test-startperf-469408.test_anisse.ScaleserpData` as sed
CROSS JOIN UNNEST(result.organic_results) as org_res
WHERE
  sed.search.q = "location bateau"
GROUP BY
  q, org_res.domain
ORDER BY nbr_search_domain desc
LIMIT 10;
