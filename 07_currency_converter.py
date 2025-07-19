import requests

curr1 = input('Enter base currency: ').upper()
curr2 = input('Enter target currency: ').upper()

data = requests.get(f'https://api.frankfurter.app/latest?from={curr1}&to={curr2}').json()
rate = data['rates']

try:
    if curr2 in rate:
        amt = int(input(f'Enter base amount in {curr1}: '))

        print(f'Current rate: 1 {curr1} = {rate[curr2]} {curr2}')
        total = rate[curr2] * amt

        print(f'{amt} {curr1} = {total} {curr2}')

    else:
        print('Please enter a valid currency!')

except Exception as e:
    print(f"Error: {e}")
