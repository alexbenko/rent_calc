def calculate_rent(difference,months=1):
  return (difference * .25) + (675 * months)

def get_last(current=0):
  with open('last_month.txt','r') as f:
    last = f.read()

  #with open('last_month.txt','w+') as file:
    #file.write(current)

  return last

print(get_last('2834'))
