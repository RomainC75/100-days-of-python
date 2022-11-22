from scrape import Scrape

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdtU3ma9fIZw80sYk9ZnZbOBYquNr-NIPdbyku2AwyAy9_7OQ/viewform?usp=sf_link"

# scrape = Scrape()

# scrape.get_infos_on_page()



from handelingData import DataHandler

handler = DataHandler()
handler.get_infos_on_page()

handler.goto_quizz_and_fill()


while True:
    pass