aclNum = int(input("Cual es el numero IPV4 para ACL? "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPV4 estandar.")
elif aclNum >=100 and aclNum <= 199:
    print("Este es un ACL IPV4 Extendido.")
else:
    print("Esta ACL IPV4 no es extendida o estandar.")
    
