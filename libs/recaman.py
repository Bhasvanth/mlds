
def recamanSeries(l):
    series = []
    n = 0
    for i in range(1,(l+1)):
        if ( (n-i) > 0 and (n-i)  not in series ):
            series.append(str(n-i))
            n = n-i
        elif ( n+i > 0):
            series.append(str(n+i))
            n = n + i

    return list(series)
	
if __name__ == "__main__":
    seriesLength  = input("Please enter length of the series :")
    series = recamanSeries(int(seriesLength))
    print (", ".join(series))
    
