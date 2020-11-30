
#x**5-y**5 - int(input()) = 0


X = int(input()) #X <= 10**9

#x**5-y**5 <= 10**9



count = 0
for l in range(-200,200):
  for i in range(-200,200):
    if(l**5 -i**5 == X):
      print(l,i)
      count += 1
      break
  if(count == 1):
    break
   
	


