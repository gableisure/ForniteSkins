from scraping import Scraping
from time import time

class Main:
    
    start_time = time()

    print('Running the scraping')

    scraping = Scraping()
    scraping.run()

    print('Finished scraping')

    print('\nScraping completed in %.3f seconds' %(time() - start_time))
    