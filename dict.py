import json
data=json.load(open("data.json")) # enter directory of data.json here
import difflib


def dictionary(n):
  if n in data.keys():
    return(data[n])
  elif len(difflib.get_close_matches(n,data.keys(),cutoff = 0.8)) >0:
    close_word=str(difflib.get_close_matches(n,data.keys(),cutoff=0.8)[0])
    permission2=input("enter 'y' if you meant %s and enter 'n'  otherwise  " %close_word)
    if permission2 =='y':
       return(data[close_word])
    else:
        print(" that cannot be understood")
        return
  else:
      print("no word of this kind exists")




permission="y"
while(permission =="y"):
  n=input("please enter a word ")
  d=dictionary(n)
  if d == None:
    break
  else:
   for x in d:
    print("\n",x)
  permission=input("\nenter 'y' to continue and 'n' to stop ")
