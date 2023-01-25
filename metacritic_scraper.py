from bs4 import BeautifulSoup
import requests
import pandas as pd


class MetaCriticScrapper:

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }


    title_array = []
    scores_array = []

    #fetch the webpage and print response code. response code [200] is a sucessful fetch
    def fetch(self,url):
        response = requests.get(url,headers=self.header,allow_redirects=False)
        print(response)
        return response

    
    def parse(self,response):
        content = BeautifulSoup(response,'html.parser')
        titles = content.find_all('a',{'class':'title'})
        #get the game titles, clean, and store in a list
        for game in titles:
            self.title_array.append(game.text)
            #print(game.text)
        scores = content.find_all('div',{'class':'metascore_w large game positive'})
        for score in scores:
            self.scores_array.append(score.text)
            #print(score.text)

    def run(self):
        url = 'https://www.metacritic.com/browse/games/score/metascore/all/xboxone/filtered'
        result = self.fetch(url)
        self.parse(result.content)

    #export the results to CSV
    def make_table_csv(self):
        df = pd.DataFrame(list(zip(self.title_array,self.scores_array)),columns=['Game_Title','Score'])
        df.to_csv('Top_Xbox_Games.csv')

    

if __name__ == '__main__':
    
    scraper = MetaCriticScrapper()
    scraper.run()
    scraper.make_table_csv()




