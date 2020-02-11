import pysitemap

DOMAIN_NAME = ""


if __name__ == '__main__':
    url = f'https://{DOMAIN_NAME}/'  # url from to crawl
    logfile = 'sitemap_error_log.log'  # path to logfile
    oformat = 'xml'  # output format
    crawl = pysitemap.Crawler(url=url, logfile=logfile, oformat=oformat)
    crawl.crawl()
