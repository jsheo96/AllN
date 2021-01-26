from korea_news_crawler.articlecrawler import ArticleCrawler

Crawler = ArticleCrawler()
Crawler.set_category( '정치', '경제', '사회', '생활문화', 'IT과학', '세계', '오피니언')
Crawler.set_date_range(2019, 1, 2020,12)
Crawler.start()