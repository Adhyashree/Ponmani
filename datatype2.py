#Data type:set and dictionart
set_int={1,4,7,8,1} #not allow the duplicata value
set_float={1.1,3.3,6.6}
set_complex={9j,5+7j}
set_str={"a","b","c"}
set_mixed={1,7+6j,5.5,"name"}
dic_int={1:10,2:20,3:30,1:10} # not allow the duplicate value
dic_float={2.0:2.3,4.4:5.6}
dic_complex={2j:3.4+5j}
dic_str={"name":"abc","class":"first"}
dic_mixed={1:3.4,"complex":10+5j}
#print datatype
print(type(set_int))
print(type(set_float))
print(type(set_complex))
print(type(set_str))
print(type(set_mixed))
print(type(dic_int))
print(type(dic_float))
print(type(dic_complex))
print(type(dic_str))
print(type(dic_mixed))
#print the variable value
print(set_int)
print(set_float)
print(set_complex)
print(set_str)
print(set_mixed)
print(dic_int)
print(dic_float)
print(dic_complex)
print(dic_str)
print(dic_mixed)
print(dic_str["name"])
#end 