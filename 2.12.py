print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

import re 
value = [] 
items=[x for x in input("Nhập mật khẩu: ").split(',')] 
# ############ 
for p in items: 
    if len(p)<6 or len(p)>12: 
        continue 
    else: 
        pass 
    if not re.search("[a-z]",p): 
       continue 
    elif not re.search("[0-9]",p): 
       continue 
    elif not re.search("[A-Z]",p): 
       continue 
    elif not re.search("[$#@]",p): 
       continue 
    elif re.search("\s",p): 
       continue 
    else: 
       pass 
    value.append(p) 
print (",".join(value))
