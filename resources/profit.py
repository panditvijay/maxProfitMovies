from flask import jsonify
from datetime import date as Date



def getDay(date):
    monthDictionary = {
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
    }

    date = date.split()
    day = int(date[0])
    month = monthDictionary[date[1].lower()]
    year = Date.today().year
    timetupleDay = Date(year, month, day).timetuple()[7] #Its calculating the accumulated date starting from 1st Jan
    return timetupleDay



def getMaximumProfit(movies):
    allMovie = []

    for movie in movies:
        allMovie.append([getDay(movies[movie]['endDate']), getDay(movies[movie]['startDate']), movie ])
        

    allMovie.sort() #sorting on the basis of endDate, a greedy choice which lead to optimal solution

    #print(movies[allMovie[0][2]])

    maxProfitMovies={}
    maxProfitMovies[allMovie[0][2]]=movies[allMovie[0][2]]

    selectMovie=0 #index of selected movie
    
    costOfMovie=1
    totalProfit=costOfMovie

    for i in range(1, len(allMovie)):
        if(allMovie[i][1]>allMovie[selectMovie][0]):
            maxProfitMovies[allMovie[i][2]]=movies[allMovie[i][2]]
            selectMovie=i
            totalProfit=totalProfit+costOfMovie


    

    return {"movies":maxProfitMovies, "maxAmount":str(totalProfit) + " Crore"}

    #return "testing"