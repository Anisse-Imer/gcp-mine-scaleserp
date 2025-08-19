CREATE VIEW `test-startperf-469408.test_anisse.nbr_urls_par_site_device_jour` AS
SELECT
  count(gsc.url) as nb_url,
  gsc.site as site,
  gsc.device as device,
  gsc.date as date
FROM
  `test-startperf-469408.test_anisse.GscData` as gsc
GROUP BY
  gsc.site, gsc.device, gsc.date;