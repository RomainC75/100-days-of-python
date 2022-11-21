from scrape import Scrape
import dotenv
config = dotenv.dotenv_values()

target_account = "chefsteps"
insta_mail = config['IG_MAIL']
insta_pass = config['IG_PASS']

scrape = Scrape( insta_mail, insta_pass )
scrape.login()
scrape.find_followers(target_account)

while True:
    pass