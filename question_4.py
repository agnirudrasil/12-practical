
#file_1=open("STORY.txt","w")
#l1= "The rose is red."
#l2= "A girl is playing there."
#l3= "There is a playground."
#l4= "An aero plane is in the sky."
#l5="Numbers are not allowed in the password."
#file_1.write(l1)
#file_1.write('\n')
#file_1.write(l2)
#file_1.write('\n')
#file_1.write(l3)
#file_1.write('\n')
#file_1.write(l4)
#file_1.write('\n')
#file_1.write(l5)
#file_1.write('\n')
#file_1.close()


file_2=open("STORY.txt","r")
storylist=file_2.readlines()
i=""
count1=0
count2=0
for i in storylist:
    if i[0]!="A" :
        count1+=1
    if "is" in i :
        count2+=1

    

print("Number of lines not startign with A in the file is : ",count1)
print("Number of is's in the file is : ",count2
