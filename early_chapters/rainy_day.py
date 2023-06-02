import time 

outside = "Yay! Go Outside"
stuck_inside = True
umbrella = None

while stuck_inside:
  raining = input("Is it raining outside? (Y/N) ")
  
  if raining == "N":
    print(outside)
    stuck_inside = False

  elif raining == "Y":
    
    # print(umbrella)
    
    if umbrella is None:
      umbrella = input("Do you have an umbrella? (Y/N) ")
  
    if umbrella == "Y":
      print(outside)
      stuck_inside = False
    
    elif umbrella == "N":
      print("Wait a while...")
      time.sleep(2)

    
    
    
    
