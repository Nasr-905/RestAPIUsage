from pprint import pprint
import requests
from tkinter import *
import webbrowser
from os import path

def card(x, datajson, ofile):
    ofile.write('<div class="cards-list">')
    ofile.write('  <link rel = "stylesheet"')
    ofile.write('   type = "text/css"')
    ofile.write('   href = "ZomatoAPI.css" />')
    ofile.write('<div class="card 1">')
    ofile.write('  <div class="card_title title-gray ">')
    resto = datajson['restaurants'][x]['restaurant']['name']
    ofile.write('    <h6>' + str(resto) + '</h6>')
    ofile.write('    <br>')
    adds = datajson['restaurants'][x]['restaurant']['location']['address']
    ofile.write('        <font size="2"align="center", style="font-family:Courier New">Address:'+str(adds)+'</font>')
    ofile.write('    <br>')
    ofile.write('    <br>')
    highs = datajson['restaurants'][x]['restaurant']['highlights']
    ofile.write('    <font size="2"align="center", style="font-family:Courier New">Highlights:'+str(highs)+'</font>')
    ofile.write('    <br>')
    ofile.write('    <br>')
    cost = str(datajson['restaurants'][x]['restaurant']['average_cost_for_two'])
    cur = datajson['restaurants'][x]['restaurant']['currency']
    ofile.write('    <font size="2"align="center", style="font-family:Courier New">Average Price for Two:' + str(cur) + str(cost)+ '</font>')
    ofile.write('</div>')
    ofile.write('</div>')
    ofile.write('</div>')
    ofile.write('    <br>')
    ofile.write('    <br>')
    ofile.write('    <br>')
    ofile.write('    <br>')
    
def writeHTML(datajson):
    ofile = open("ZomatoAAPI.html","w")
    ofile.write("<style>")
    ofile.write("body {background-color: #e6e9ed;}")
    ofile.write("</style>")
    count = int(d.get())
    
    

    if count == 1:
        card(0, datajson, ofile)
    elif count == 2:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
    elif count == 3:
        card(0)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
    elif count == 4:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
    elif count == 5:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
    elif count == 6:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
    elif count == 7:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
    elif count == 8:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
    elif count == 9:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
    elif count == 10:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
    elif count == 11:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
    elif count == 12:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
    elif count == 13:
        count(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
    elif count == 14:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
    elif count == 15:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
    elif count == 16:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
        card(15, datajson, ofile)
    elif count == 17:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
        card(15, datajson, ofile)
        card(16, datajson, ofile)
    elif count == 18:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
        card(15, datajson, ofile)
        card(16, datajson, ofile)
        card(17, datajson, ofile)
    elif count == 19:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
        card(15, datajson, ofile)
        card(16, datajson, ofile)
        card(17, datajson, ofile)
        card(18, datajson, ofile)
    else:
        card(0, datajson, ofile)
        card(1, datajson, ofile)
        card(2, datajson, ofile)
        card(3, datajson, ofile)
        card(4, datajson, ofile)
        card(5, datajson, ofile)
        card(6, datajson, ofile)
        card(7, datajson, ofile)
        card(8, datajson, ofile)
        card(9, datajson, ofile)
        card(10, datajson, ofile)
        card(11, datajson, ofile)
        card(12, datajson, ofile)
        card(13, datajson, ofile)
        card(14, datajson, ofile)
        card(15, datajson, ofile)
        card(16, datajson, ofile)
        card(17, datajson, ofile)
        card(18, datajson, ofile)
        card(19, datajson, ofile)
    ofile.close()
    b2 = Button(root,text="complete - view your file",command=webbrowser.open('file://' + path.realpath('ZomatoAAPI.html')))
    '''
        ofile.write('  </div>')
    ofile.write('</div>')
    ofile.write('<div class="card 1">')
    ofile.write('    <div class="card_title title-gray">')
    ofile.write('    <h6>Address</h6>')
    ofile.write('    <br>')
    ofile.write('    <div class="w3-card w3-yellow">')
    adds = datajson['restaurants'][0]['restaurant']['location']['address']
    for add in adds:
        ofile.write('        <font size="2"align="center", style="font-family:Courier New">'+str(add)+'</font>')
        #ofile.write('    <br>')
    ofile.write('    </div>')
    ofile.write('    </div>')
    ofile.write('</div>')
    ofile.write('<div class="card 1">')
    ofile.write('  <div class="card_title title-gray">')
    ofile.write('    <h6>Highlights</h6>')
    ofile.write('    <br>')
    highs = datajson['restaurants'][0]['restaurant']['highlights']
    for high in highs:
        ofile.write('    <font size="2"align="center", style="font-family:Courier New">'+str(high)+'</font>')
        #ofile.write('    <br>')
    ofile.write('  </div>')
    ofile.write('</div>')
    ofile.write('<div class="card 1">')
    ofile.write('  <div class="card_title title-gray">')
    ofile.write('    <h6>Cost</h6>')
    ofile.write('    <br>')
    higs = str(datajson['restaurants'][0]['restaurant']['average_cost_for_two'])
    for hig in higs:
        ofile.write('    <font size="2"align="center", style="font-family:Courier New">'+str(hig)+'</font>')
        #ofile.write('    <br>')
    ofile.write('  </div>')
    ofile.write('</div>')

 
    ofile.close()
    '''
#put  max of 4 for count
    
def getAPI():
    #close the window
    #Mak the Comment neccesary
    search = a.get()
    lat = b.get()
    lon = c.get()
    count = d.get()
    radius = e.get()
    sort = f.get()
    
    str_search = str(search)
    str_lat = str(lat)
    str_lon = str(lon)
    str_count = str(count)
    str_radius = str(radius)
    str_sort = str(sort)

    if str_search == "Keyword (bar, salad, etc.)":
        search1 = ""
    elif str_search == "":
        search1 = ""
    else:
        search1 = "q=" + str_search + "&"

    if str_sort == "cost":
        sort1 = "sort=cost"
    elif str_sort == "rating":
        sort1 = "sort=rating"
    else:
        sort1 = "sort=real_distance"

    if str_radius == "Radius (meters)":
        radius1 = "radius=2000&"
    elif str_radius == "":
        radius1 = "radius=2000&"
    else:
        radius1 = "radius=" + str_radius + "&"
    #fix URL
    if str_lat == "Latitude (required)":
        lat1 = ""
    elif str_lat == "":
        lat1 = ""
    else:
        lat1 = "lat=" + str_lat + "&"
        
    if str_lon == "Longitude (required)":
        lon1 = ""
    elif str_lon == "":
        lon1 = ""
    else:
        lon1 = "lon=" + str_lon + "&"
        
    if str_count == "# of Results (1-20)":
        count1 = "count=10&"
    elif str_count == "":
        count1 = "count=10&"
    else:
        count1 = "count=" + str_count + "&"
        
    #https://developers.zomato.com/api/v2.1/search?q=Something&count=20&lat=lat&lon=lon&radius=meters&sort=cost&order=asc
    locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/search?" + search1 + count1 + lat1 + lon1 + radius1 + sort1 + "&order=asc"

    print(locationUrlFromLatLong)
    
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "2ea43591e94f21392f720dcdb43a9ff7"}
    response = requests.get(locationUrlFromLatLong, headers=header)
    
    response = requests.get(locationUrlFromLatLong, headers=header)
    datajson = response.json()
    print(str(response.json()))

    writeHTML(datajson)
    
root = Tk()
root.geometry("500x350")
root.title("Zomato Restaurant Finder")


a = Entry(root)

a.pack()
a.delete(0, END)
a.insert(0, "Keyword (bar, salad, etc.)")

b = Entry(root)
b.pack()
b.delete(0, END)
b.insert(0, "Latitude (required)")

c = Entry(root)

c.pack()
c.delete(0, END)
c.insert(0, "Longitude (required)")

d = Entry(root)

d.pack()
d.delete(0, END)
d.insert(0, "# of Results (1-20)")

e = Entry(root)

e.pack()
e.delete(0, END)
e.insert(0, "Radius (meters)")


f = StringVar(root)
f.set("cost")
g = OptionMenu(root, f, "cost", "rating", "real distance")
g.pack()


b1 = Button(root, text="Submit", command=getAPI)
b1.pack()
