
name = ''
while name != 'your name':
    print('please enter your name')
    name = input('>>> ')
print('Finally, you got it, Thank you!')


while True:
    print('Please type your name')
    name = input('>>>> ')

    if name == 'your name' :
        break
print('Thank you!')


while True:
    print('Hello, trust you are doing great today')
    print('Who are you? type in your name')

    name = input('>> ')
    if name != 'Joe':
        continue
    print(f"Hello {name}. What is the your Password? (It is a fish.)")

    password = input('??? ')
    if password == 'swordfish':
        break
print('Access granted')

