import csv
import collections as coll

csvfile = open('../data/airbnb/seattle_reviews_01_04_2016.csv', newline = '')
reviewfile = csv.reader(csvfile, delimiter =',')
header = next(reviewfile)
records = list(reviewfile)


def find_listings (records, user_id):
    listings = set()

    # find listings of user
    for row in records:
        if row[3] == user_id:
            listings.add(row[0])
    
    return listings

def find_travelers (records, listings):
    fellow_travelers = set()

    # find fellow traveler 
    for row in records:
        if row[0] in listings:
            fellow_travelers.add(row[3])
    
    return fellow_travelers

def count_triangles(records, fellow_travelers):
    triangles = []

     # find triangles user is a part of
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])
    
    return coll.Counter(triangles)

def recommend_listings(counts, user_listings):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)
    
    return counts.most_common(10)
    