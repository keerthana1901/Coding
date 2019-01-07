usr_1=int(raw_input())
usr_2=int(raw_input())
usr_3=int(raw_input())
if (usr_1 >= usr_2) and (usr_1 >= usr_3):
	print usr_1
elif (usr_2>=usr_1) and (usr_2>=usr_3):
	print usr_2
else:
	print usr_3
