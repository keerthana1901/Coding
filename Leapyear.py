usr=int(raw_input())
if( (usr%400==0) or ((usr%4==0) and (usr%100 !=0)) ):
	print "yes"
else:
	print "no"
