#������ �� 1 �� 20
list_range=[]
for v in range(1,21):
    list_range.append(v)
print(list_range)  

#������ �� 1 �� 1_000_000 � ��� ����������
list_num = []
for v in range(1,1000001):
    list_num.append(v)    
min_l=min(list_num)
max_l=max(list_num)
sum_l=sum(list_num)
print(f'min={min_l}\nmax={max_l}\nsum={sum_l}')

#������ �� 1 �� 20 - �������� �����
list_num_2=[]
for n in range(1,21):
    if n%2!=0:
       list_num_2.append(n)
print(list_num_2)      
      
#������ �� 3 �� 30 - ������� 3
list_num_3=[]
for n in range(3,31):
    if n%3==0:
       list_num_3.append(n)
print(list_num_3)  

#������ �����
list_num_4=[v**3 for v in range(1,11)]
print(list_num_4)