#Copyright TheSqueeker 2021
#Squeeker & RustAutoBuy have no afiliations with Facepunch Studios Ltd or Rust

#Welcome to RustAutoBuy, making your life a bit more fun!

#How it works:
#   When you run this script you tab into your game and hover over the 
#   buy button and then after the "Captured" message printed in the terminal (You have 5 seconds to do so). Move to the sell amount
#   and the same message will be printed (This one is a bit shorter at 2 seconds till capture), then you will have 5 seconds to start
#   a movie or show and click into your game. Once it starts you cant use your mouse till you press and hold 'F' to stop the script.


from time import sleep
import keyboard, mouse
hold = True
vending_time= 0

print(
    '|Welcome to RustAutoBuy\n'
    '|======================\n'
    '|Go to a vending mechine and open it\n'
    '|Follow all promts after this\n'
    '|This script will Auto Buy the max amount of the selected item\n\n'
    '|To STOP the script press and hold "f" on your keyboard\n'
)

timeset= input('Going to Outpost? (yes/no): ')
if timeset == 'Yes' or timeset == 'yes' or timeset == 'YES':
    vending_time= 2.7
else:
    vending_time= 1.43
#buy_button means Buy Button then the Cordanent Plane
#AMT means amount then the Cordanent Plane
print('Please hover over the Buy button.\nYou have 5 seconds until mouse capture.')
sleep(5)
buy_button= mouse.get_position()
print('Captured\n')
sleep(0.3)
print('Now hover over the numbers below!\n You have 2 seconds until capture.')
sleep(2)
ammount= mouse.get_position()
print('Captured')
print('Ok!\nStarting in 5 seconds')
sleep(5)

buy_button_x= buy_button[0]
buy_button_y= buy_button[1]
ammount_x= ammount[0]
ammount_y= ammount[1]

cycle_count= 0
#2.8 Outpost
#1.43 Bandet Camp
cycle_time= vending_time + 0.66
while hold == True and keyboard.is_pressed('f') == False:
    #print('Count:',cycle_count,'\nSeconds:',round(cycle_count* cycle_time, 2))
    #if count == 5:
    #    exit()
    mouse.move(ammount_x,ammount_y,duration=0.1)
    sleep(0.2)
    mouse.click(button='left')
    sleep(0.235)
    keyboard.write('99')
    sleep(0.2311)
    mouse.move(buy_button_x,buy_button_y,duration=0.15)
    mouse.click(button='left')
    sleep(vending_time)
    cycle_count= cycle_count+ 1
