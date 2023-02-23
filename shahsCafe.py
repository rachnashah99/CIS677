


limit = 50.00
bev= ["mocha", "Water", "fruit juice", "chailatte"]
amt = [4.25, 1.00, 3.25, 3.00, 14.25, 16.75, 12.70, 11.80, 3.15, 4.90, 3.50]

bev_ch = int(input("Hello and welcome to the Shah's Cafe.\nWhat would you like to drink/?" 
+"For drinks:\n[0] mocha..... 4.25\n[1] water..... 1.00\n[2] fruit juice..... 3.25\n[3]"
 +"chailatte..... 3.00\n"))

flag_drinks = False
while flag_drinks == False:
  if bev_ch== 0:
    limit = limit-(amt[0])
    print("Thank you, {} sounds perfect! You have ${} remaining.\n".format(bev[0], limit))
    flag_drinks = True
  elif bev_ch== 1:
    limit = limit-(amt[1])
    print("Thank you, {} sounds perfect! You have ${} remaining.\n".format(bev[1], limit))
    flag_drinks = True
  elif bev_ch== 2:
    limit = limit-(amt[2])
    print("Thank you, {} sounds perfect! You have ${} remaining.\n".format(bev[2], limit))
    flag_drinks = True
  elif bev_ch== 3:
    limit = limit-(amt[3])
    print("Thank you, {} sounds perfect! You have ${} remaining.\n".format(bev[3], limit))
    flag_drinks = True
  else:
    bev_ch = int(input("Sorry, that doesn't seem to be an option. Try again:\n"))
main_course= ["chana naan", "enchiladas", "noodles and katsu", "grilled cheese"]
main_ch = int(input("Great! Now, what can I get you for the main course?\n"
+"For meals:\n[0]  chana naan..... 14.25\n[1] enchiladas..... 16.75\n[2]"
+"noodles and katsu..... 12.70\n[3] grilled cheese..... 11.80\n"))
flag_meal = False
while flag_meal == False:
  if main_ch== 0:
    limit = limit-(amt[4])
    print("Yum, {} sounds good! You have ${} remaining.\n".format(main_course[0], limit))
    flag_meal = True
  elif main_ch == 1:
    limit = limit-(amt[5])
    print("Yum, {} sounds good! You have ${} remaining.\n".format(main_course[1], limit))
    flag_meal = True
  elif main_ch == 2:
    limit = limit-(amt[6])
    print("Yum, {} sounds good! You have ${} remaining.\n".format(main_course[2], limit))
    flag_meal = True
  elif main_ch == 3:
    limit = limit-(amt[7])
    print("Yum, {} sounds good! You have ${} remaining.\n".format(main_course[3], limit))
    flag_meal = True
  else:
    main_ch = int(input("Sorry, that doesn't seem to be an option. Try again:\n"))
dess= ["oreo trouble", "blueberry cheesecake", "Gulabjamoon"]
dess_ch = int(input("And finally, what would you like for dessert?\n"
+ "For dess:\n[0] oreo trouble..... 3.15\n[1] blueberry cheesecake..... 4.90"
+"\n[2] Gulabjamoon..... 3.50\n"))
flag_dess = False
while flag_dess == False:
  if dess_ch == 0:
    limit = limit-(amt[8])
    print("Delicious {} coming right up! You have ${} remaining.\n".format(dess[0], limit))
    flag_dess = True
  elif dess_ch == 1:
    limit = limit-(amt[9])
    print("Delicious {} coming right up! You have ${} remaining.\n".format(dess[1], limit))
    flag_dess = True
  elif dess_ch == 2:
    limit = limit-(amt[10])
    print("Delicious {} coming right up! You have ${} remaining.\n".format(dess[2], limit))
    flag_dess = True
  else:
    dess_ch = int(input("Sorry, that doesn't seem to be an option. Try again:\n"))
print("{}.....${}\n{}.....${}\n{}.....${}\n".format(bev[bev_ch]
, amt[bev_ch], main_course[main_ch], amt[main_ch+4], dess[dess_ch]
, amt[dess_ch+ 8]))
print("Total.....${}\n......................".format(50-limit))
print("Thank you for visiting Shah's Cafe! See you again")


print("new commit")