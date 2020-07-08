from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>HOME</h1>")

def angka(request, angka):
    Heading = "<h1>Page Angka</h1>"

    str = Heading

    return HttpResponse(Heading)


def date(request, year, month):
    Heading = "<h1>Page Date</h1>"
    strYear = "Year: " +  str(year)
    strMonth = "Month: " +  str(month)
    
    strDate = Heading + "</br>" + "</br>" + strYear +"</br>"+ strMonth
    # strDate = Heading  
    return HttpResponse(strDate)

def date_repath(request, **input):
    Heading = "<h1>Page Date Repath **input</h1>"
    print(input)
    year = input['year']
    month = input['month']
    day = input['day']
    dataTanggal = "{}/{}/{}".format(day,month,year)
    strDate = Heading + "</br>" + "</br>" + dataTanggal
 
    return HttpResponse(strDate)

def link(request, page):
    htmlStr = "<h1>{}</h1>".format(page)
    return HttpResponse(htmlStr)


# def date_repath(request, year, month, day):
#     Heading = "<h1>Page Date Repath</h1>"
#     strYear = "Year: " +  str(year)
#     strMonth = "Month: " +  str(month)
#     strDay = "Day: " +  str(day)
    
#     strDate = Heading + "</br>" + "</br>" + strYear +"</br>"+ strMonth + "</br>"+ strDay
#     # strDate = Heading  
#     return HttpResponse(strDate)
