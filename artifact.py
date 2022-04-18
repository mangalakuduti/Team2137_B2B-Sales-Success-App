from GoogleNews import GoogleNews
'''
Language: lang as English
Period: period as number, N, representing news from last N days
'''
googlenews = GoogleNews(lang='en', period='`5d')
cont = input("Would you like to search for a company?: y/n ")
while cont == "y":
    val = input("Enter a company: ")
    googlenews.search(val)
    results = googlenews.results()
    for result in results:
        print("\n\nTITLE: ", result["title"], "\n\nDESC: ", result["desc"], "\n\nURL: ", result["link"])
    googlenews.clear()
    
    cont = input("Would you like to search for a company?: y/n ")
