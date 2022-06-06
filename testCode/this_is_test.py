Dict = {
     "game1":"Half Life",
     "game2":"NFS Underground",
     "game3":"Dead Space",
     "ShitGame":{
         "SGame":"Escape Dead Island"
     }
          }

if "ShitGame" in Dict:
    print("Yes",Dict["ShitGame"]["SGame"],"is shit")
else:
    print("Nope")