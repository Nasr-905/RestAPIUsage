import requests

def HTML(datajson):
    APIfile = open("My_API_Project.html","w+")
    APIfile.write('<div class="widget_wrap" style="width:320px;height:797px;display:inline-block;"><iframe src="https://www.zomato.com/widgets/res_search_widget.php?city_id=89&language_id=1&theme=red&hideCitySearch=on&hideResSearch=on&sort=popularity" style="position:relative;width:100%;height:100%;" border="0" frameborder="0"></iframe></div>')
    APIfile.close()
APIfile = open
