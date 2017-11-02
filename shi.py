#python3
import re
f1=open('666.txt')
f2=open('shi.md','a')
thing=f1.readlines()
i=0
#pptdog=re.compile(r'[32m(.*)')
pdog=''
for dog in thing:
	if i==0:

		pdog='## '+dog[5:len(dog)-4]+'\n'
		f2.write(pdog)
		#pdog=''
		i=1
	elif i==1:
		pdog=dog[5:len(dog)-4]+r'</br>'+'\n'
		f2.write(pdog)
		i=2
	else:
		pdog=dog[0:len(dog)-1]+r'</br>'+'\n'
		f2.write(pdog)
f2.write('\n')
f1.close()
f2.close()
		
			