highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

highlighted_poems_stripped = []
for x in highlighted_poems_list:
    result = x.strip()
    highlighted_poems_stripped.append(result)

#print(highlighted_poems_stripped)
highlighted_poems_details = []
for x in highlighted_poems_stripped:
    eachString = x
    splitHPS = eachString.split(":")
    highlighted_poems_details.append(splitHPS)
#print(highlighted_poems_details)

titles = []
poets = []
dates = []
for x in highlighted_poems_details:
    t = x[0]
    p = x[1]
    d = x[2]
    titles.append(t)
    poets.append(p)
    dates.append(d)
#print(titles)
for x in titles:
    message = "The poem {} was published by {} in {}".format(titles, poets, dates)
    print(message)
