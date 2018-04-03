import sys
idaapi.autoWait()
funcs = []
for func in Functions():
    if SegName(func) != 'extern':
        FuncName= GetFunctionName(func)
        funcs.append((func, FuncName))
print "idafunctions = ", funcs
f = open('functions.txt','w')
f.write(str(funcs))
f.close()


