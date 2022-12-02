from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time


def keyword_to_titles(metadata):
    keyword_map = dict()

    for i in range(len(metadata)):

        if metadata[i][4] == []:
            continue

        for keyword in metadata[i][4]:
            if keyword not in keyword_map:
                keyword_map[keyword] = [metadata[i][0]]
            else:
                if metadata[i][0] not in keyword_map[keyword]:
                    keyword_map[keyword].append(metadata[i][0])
    
    return keyword_map


def title_to_info(metadata):
    title_map = dict()

    for i in range(len(metadata)):

        if len(metadata[i]) != 5:
            continue

        temp_map = {
            'author': metadata[i][1],
            'timestamp': metadata[i][2],
            'length': metadata[i][3]
        }
        title_map[metadata[i][0]] = temp_map
    
    return title_map


def search(keyword, keyword_to_titles):

    if keyword in keyword_to_titles:
        return keyword_to_titles[keyword]
    else:
        return []


def article_length(max_length, article_titles, title_to_info):
    
    rslt = []

    if max_length <= 0:
        return rslt

    for article in article_titles:
        if title_to_info[article]['length'] <= max_length:
            rslt.append(article)
    
    return rslt


def key_by_author(article_titles, title_to_info):
    
    rslt = {}
    for article in article_titles:
        if article in title_to_info:
            if title_to_info[article]['author'] not in rslt:
                rslt[title_to_info[article]['author']] = [article]
            else:
                rslt[title_to_info[article]['author']].append(article)
        else:
            continue
    
    return rslt


def filter_to_author(author, article_titles, title_to_info):
    
    rslt = []
    for article in article_titles:
        if title_to_info[article]['author'] == author:
            rslt.append(article)
    
    return rslt


def filter_out(keyword, article_titles, keyword_to_titles):
    rslt = []

    if keyword not in keyword_to_titles:
        return article_titles

    for article in article_titles:
        if article not in keyword_to_titles[keyword]:
            rslt.append(article)
    
    return rslt


def unix_time(year):
    year = datetime.date(year, 1, 1)
    unix_time = time.mktime(year.timetuple())
    return int(unix_time)


def articles_from_year(year, article_titles, title_to_info):

    rslt = []

    if year < 0:
        return rslt

    year_start = unix_time(year)
    year_end = unix_time(year+1)

    for article in article_titles:
        if article not in title_to_info:
            continue
            
        curr_time = title_to_info[article]['timestamp']
        if curr_time in range(year_start, year_end):
            rslt.append(article)
    
    return rslt


# Prints out articles based on searched keyword and advanced options
def display_result():
    # Preprocess all metadata to dictionaries
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search(), keyword_to_titles_dict)

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 2:
        # Update articles to be a dictionary keyed by author
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 3:
        # value stores author name
        # Update article metadata to only contain titles and timestamps
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 4:
        # value stores a second keyword
        # Filter articles to exclude those containing the new keyword.
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 5:
        # value stores year as an int
        # Update article metadata to contain only articles from that year
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))


if __name__ == "__main__":
    display_result()
