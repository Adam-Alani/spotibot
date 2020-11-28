from youtubesearchpython import SearchVideos

def searchYT(name):
    search = SearchVideos(name , offset = 1 , mode="list", max_results=1)
    searchDict = search.result()

    return searchDict[0][2]

