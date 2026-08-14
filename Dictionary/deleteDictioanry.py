sourav_info={
'name':'sourav',
'age':20,
'address':'jhargram'
}
delete_keys=['name','address']
for i in delete_keys:
    sourav_info.pop(i,None)
print(sourav_info)
