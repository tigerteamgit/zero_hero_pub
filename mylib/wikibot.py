import wikipedia


def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result

#build a function to return the summary of a wikipedia page
def get_wiki_summary(page):
    """Get the summary of a wikipedia page"""
    return wikipedia.summary(page)

#build a function to search wikipedia pages for a match
def search_wiki_pages(page):
    """Search wikipedia for a query"""
    return wikipedia.search(page)
