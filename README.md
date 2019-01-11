# magic-formula-scraper

Python script for scraping [magicformulainvesting.com](https://www.magicformulainvesting.com/) using [selenium](https://www.seleniumhq.org/).


My brother and I make investments by following Joel Greenblatt's Magic Formula.
The site mentioned above uses this formula and outputs the top X companies that fit within
the criteria of the formula. However, the site does not allow one to copy the information of
these companies directly. Manually typing out the names of 30+ companies and their information
is a time-suck, so I created this script to scrape this information instead.

Features
------
+ opens a safari browser to the magic formula login page, then uses selenium's Keys and the getpass library to enter login information
+ once logged in, selects the number of stocks to view and clicks the corresponding button to display them
+ scrapes information about listed companies, writes to csv file titled 'companies.csv'

I have set up my script to run using a cron job every 3 months on the first of each month at 1 pm. Below is my file, accessed on a Mac by running "crontab -e" at the terminal. I first had to give iTerm and the Terminal apps permission to read/write from my ssd.


```sh
#!/bin/bash
0 1 1 */3 * /path/to/python /path/to/scraper.py
```

From reading online, it sounds as though a cron job cannot read standard input and will generate an end of file error. So for the cronjob, I have hardcoded my username and password, which is really bad practice. However, since this site doesn't really contain sensitive information, I'm okay with that. The provided script in this repository still uses the secure method provided by getpass to deal with the user's password.

Features to Implement
------
+ have a file of companies already researched/invested in, check this list before writing to csv
+ log in to google sheets using the sheets API and append data to our spreadsheet
