# magic-formula-scraper

Python script for scraping [magicformulainvesting.com](https://www.magicformulainvesting.com/) using selenium.


My brother and I make investments by following Joel Greenblatt's Magic Formula.
The site mentioned above uses this formula and outputs the top X companies that fit within
the criteria of the formula. However, the site does not allow one to copy the information of
these companies directly. Manually typing out the names of 30+ companies and their information
is a time-suck, so I created this script to scrape this information instead.

Features to Implement
------
+ have user enter email and password from command line rather than having it hardcoded in
+ write company info to csv
+ have a file of companies already researched/invested in, check this list before writing to csv
+ (optional) log in to google sheets and append data to our spreadsheet
+ make the script a cronjob every 3 months
