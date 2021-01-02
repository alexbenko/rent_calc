from datetime import datetime

#my rent is $675 a month
monthly_rate = 675

def calculate_electricity(current,last):
  #electricity formula defined by landlord
  return (current - last) * .25

def get_last(current=0):
  #Get Last Months Electricity
  with open('last_month.txt','r') as f:
    last = f.read()

  #Update new reading
  with open('last_month.txt','w+') as file:
    file.write(current)

  return int(last)

def save_history(total,elec,months,reading):
  date = datetime.today().strftime('[%Y-%m-%d]')

  with open('history.txt','a') as f:
    f.write(f'\n{date} Total Rent Paid was {str(total)}, electricity was {str(elec)} with a reading of {reading}. Total months paid for was {str(months)}.\n')

  print('Successfully Saved Rent Payment to history.txt')


def start_calculator():
  current = float(input('What is the current electricity reading? '))
  months_paying  = int(input('How many months are you paying for? '))

  last = get_last(str(current))
  electricity = calculate_electricity(current,last)

  total_rent = str((monthly_rate * months_paying) + electricity)
  print(f'Total Due This Month is: ${total_rent}, electricity was ${electricity}. The Amount of months payed for was: {months_paying}.')
  save_history(total_rent,electricity,months_paying,current)


start_calculator()

#print('-' * 10)
#print('|' + ' ' * 8 + '|')
#print('-' * 10)
