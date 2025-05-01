import wikipedia
from yake import KeywordExtractor

# build a function to return the summary of a wikipedia page
def get_wiki_summary(page):
    """Get the summary of a wikipedia page"""
    return wikipedia.summary(page)

# build a function to search wikipedia pages for a match
def search_wiki_pages(page):
    """Search wikipedia for a query"""
    return wikipedia.search(page)

# build a function scrape content from a wikipedia page using the wikipedia library
def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result

# build a function to get top 10 keywords from a wikipedia page
def get_wiki_keywords(page):
    """Get the keywords from a wikipedia page"""
    content = get_wiki_keywords(page).content
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    # returns a dictionary of keywords and their scores
    return {keyword: score for keyword, score in keywords[:10]}






