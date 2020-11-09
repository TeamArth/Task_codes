import os 
print("\t\t\tWelcome to partitions menu")
print("\t\t\t--------------------------")
print("""
\n
Press 1 : To show all partitions 
Press 2 : To create a physical volume
Prres 3 : To display all the physical volume
Press 4 : To create a volume group 
Press 5 : To display all the volume groups
Press 6 : To create a lv partition
Press 7 : To display all the lv partitions
Press 8 : To format the partition
Press 9 : To mount the partition
Press 10 : To resize a lv partition
Press 11 : To format only the resized partition
""")
ch = input("Enter your choice:")

if int(ch)==1:
	os.system("fdisk -l")
elif int(ch)==2:
	disk1= input("Enter disk name:")
	disk2= input("Enter disk name:")
	os.system("pvcreate {} {}".format(disk1,disk2))
elif int(ch)==3:
	os.system("pvdisplay")
elif int(ch)==4:
	vg= input("Enter volume group name:")
	diskvg1= input("Enter disk to create vg with:")
	diskvg2= input("Enter disk to create vg with:")
	os.system("vgcreate {} {} {}".format(vg,diskvg1,diskvg2))
elif int(ch)==5:
	os.system("vgdisplay")
elif int(ch)==6:
	lv= input("Enter vg name:")
	size= input("Enter size of the lv to create:")
	name= input("Enter name of the lv:")
	os.system("lvcreate --size {} --name {} {}".format(size,name,lv))
elif int(ch)==7:
	os.system("lvdisplay")
elif int(ch)==8:
	dir= input("Enter the location to be formatted:")
	os.system("mkfs.ext4 {}".format(dir))
elif int(ch)==9:
	mount= input("Enter a partition to mount:")
	node= input("Enter a dir to mount:")
	os.system("mount {} {}".format(mount,node))
elif int(ch)==10:
	um= input("Enter partition to unmount:")
	dis= input("Enter disk name to resize again:")
	os.system("umount {}".format(um))
	os.system("fdisk {}".format(dis))
elif int(ch)==11:
	di= input("Enter partition to examine filesystems and format:")
	os.system("e2fsck -f {}".format(di))
	os.system("resize2fs {}".format(di))
else:
	print("Enter valid number")
