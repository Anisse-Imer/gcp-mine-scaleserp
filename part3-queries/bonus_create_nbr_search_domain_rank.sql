-- Site le plus visite pour une query
-- https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls
CREATE VIEW `test-startperf-469408.test_anisse.nbr_search_domain_rank` AS
WITH nbr_search_domain AS (
  SELECT
    count(*) as nbr_search,
    org_res.domain,
    sed.search.q as q
  FROM
    `test-startperf-469408.test_anisse.ScaleserpData` as sed
  CROSS JOIN UNNEST(result.organic_results) as org_res
  GROUP BY
    q, domain
),
nbr_search_domain_rank AS (
  SELECT
    *,
    RANK() OVER (partition by q order by nbr_search desc) as rank
  FROM
    nbr_search_domain
)
SELECT
  *
FROM
  nbr_search_domain_rank
WHERE rank = 1;
