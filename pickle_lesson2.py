import pickle

#1 Initialize an empty dictionary variable, name it all_pod_members
all_pod_members = {}

#2 Initialize a file variable to write data to, name it pod_file, that will
# open a file named hgp_pods that you will write data to the file. 
pod_file = open('all_pods.pkl', 'wb')

#3  Initialize empty dictionary variables, name it as such;
jacore_members = {}
andrew_members = {}

#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD  
jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'

andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'
 
#6 Add all the PODS to the all_pod_members dictionary
all_pod_members['Jacore'] = jacore_members
all_pod_members['Andrew'] = andrew_members

#7 Dump all the 
pickle.dump(jacore_members,pod_file)
pickle.dump(andrew_members,pod_file)

#8 Open the pod_file to read data
pod_file = open('all_pods.pkl', 'rb')

#9 Print all the Pod leaders and POD membership
for key,value in all_pod_members.items():
  print('This POD Leader is',key)
  for key2, value2 in value.items():
    print(key2,value2)
  print('\n')

pod_file.close()

