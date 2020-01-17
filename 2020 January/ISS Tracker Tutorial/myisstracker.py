import requests, json, turtle, time

def move_iss(lat,long):
    global iss, pointer_inplace
    if pointer_inplace == False:
        iss.penup()
    if long > 172 or long < -172:
        iss.penup()
    iss.goto(long,lat)
    iss.pendown()
    
    time.sleep(10)

screen = turtle.Screen()
screen.setup(1000,500)
screen.bgpic("earth.gif")
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape("spaceman.gif")
iss.shape("spaceman.gif")
iss.shapesize(0.2,0.2)




pointer_inplace = False
url = "http://api.open-notify.org/iss-now.json"


for i in range(10000):
    response = requests.get(url)
    if (response.status_code == 200):
        response_dictionary = json.loads(response.text)
        position = response_dictionary["iss_position"]
        lat = float(position["latitude"])
        long = float(position["longitude"])
        move_iss(lat, long)
        
        if i != 0:
            pointer_inplace = True
    else:
        print("Houston, we have a problem:", response.status_code)
    
turtle.mainloop()