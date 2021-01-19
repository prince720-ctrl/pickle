import pickle

# 1. Leader Numbers
leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Andrew Lubega'] = '(925) 727-4611'
leader['Gabriel Reader'] = '(510) 326-5834'
leader['Richard Kamau'] = '(510) 228-5623'
leader['Aris Carter'] = '(510) 229-6359'

# 2. create/open pod_nbrs.pkl file
pod_file = open('pod_nbrs.pkl', 'wb')

# 3. Write POD Leader and number to a file
pickle.dump(leader,pod_file)

# 4. Member Numbers
member = {}
member['Akari Johnson'] = '(510 500-2206'
member['Morris Jones'] = '(925) 286-5922'
member['Prince Fields'] = '(510) 472-0804'
member['Mousa Ndiaye'] = '(415) 717-8414'
member['Jacore Baptiste'] = '(845) 200-6250'

# 5. Write Member numbers to pod_file
pickle.dump(member,pod_file)

# 6. Close pod_file
pod_file.close()

# 7. Open pod.file
pod_file = open('pod_nbrs.pkl', 'rb')


# 8. Leader numbers
print('Leaders: ')
for key,value in leader.items():
    print(key, value)

print('\n')


# 9. Print POD members
print('Members')
for key,value in member.items():
    print(key,value)
print('\n')

# 10. Close pod_file
pod_file.close()
    
