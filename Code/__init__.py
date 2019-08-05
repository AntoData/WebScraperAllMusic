from Code import WrapperForWebScraper as wfws
def main():
    try:
        artist = input("Give me the name of an artist:\n")
        wfws.getDiscography(artist)
    except Exception as e:
        print("Something went wrong, check the error")
        print(e)
        
if __name__== "__main__":
    main()
