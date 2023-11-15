inventory0 = 'key'
inventory1 = '+1 thing'
inventory2 = 'coins'
inventory3 = 'potion'

print ('variable example:', inventory1)
# all arrays start at 0
inventory = ['key', '+1 thing']
print ('Inventory array: ', inventory[0])
inventory.append ('swaord-1')
print ('new time:' , inventory[2])
# created a variable for how much items in inventory
inventoryItems = len(inventory)
print ('You have: ', inventoryItems)

#print out entire inventory
#/n adds a space after print statement
print ('This is your iinventory:/n')
for inventoryItems in inventory:
    print(inventoryItems)
