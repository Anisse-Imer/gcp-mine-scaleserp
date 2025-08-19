CREATE VIEW `test-startperf-469408.test_anisse.distinct_q` AS
SELECT
  distinct sed.search.q as q
FROM
  `test-startperf-469408.test_anisse.ScaleserpData` sed;
