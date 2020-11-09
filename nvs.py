import os


print("\t\t\t WELCOME TO MY MENU !!!!")


print("""
\n
press(1)  : to run date
press(2)  : to cal
press(3)  : to reboot
press(4)  : to add any two numbers
press(5)  : to sub any two numbers
press(6)  : to shutdown
press(7)  : to configure hdfs
press(8)  : to configure core
press(9)  : to install a software
press(10) : to unistall a software 
press(11) : to hadoop start/stop sevrice of name/data node
press(12) : To open partitions menu !!
""")
ch=input("Enter your choice : ")
print(ch)


if int(ch) == 1:
	os.system("date")
elif int(ch) == 2:
	os.system("cal")
elif int(ch) == 3:
	os.system("reboot")
elif int(ch) == 4:
	os.system("python3 add.py")

elif int(ch) == 5:
	os.system("python3 sub.py")
elif int(ch) == 6:
	os.system("halt")
elif int(ch) == 7:
	os.system("cd //var//www//html && vim hdfs-site.xml")
elif int(ch) == 8:
	os.system("cd //var//www//html && vim core-site.xml")
elif int(ch) == 9:
	soft=input("Enter the soft you want to install : ")
	os.system("yum install {}".format(soft))
elif int(ch) == 10:
	soft=input("Enter the soft you want to uninstall : ")
	os.system("yum unistall {}".format(soft))
elif int(ch) == 11:
	function=input("Enter the function : ")
	typ=input("Enter the type of node : ")
	os.system("hadoop-daemon.sh {} {}node --force".format(function,typ))
elif int(ch) == 12: 
	os.system("python3 part.py")

else:
	print("not supported")
           

