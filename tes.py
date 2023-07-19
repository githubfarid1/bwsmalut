def calPercent(x, y, integer = False):
   percent = x / y * 100
   
   if integer:
       return int(percent)
   return percent

print("Percentage: ",calPercent(33, 200, True))