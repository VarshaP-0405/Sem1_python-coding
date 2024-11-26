dict={"Lakme":["Eyeconic kajal","Liquid EyeLiner","Argan Oil Serum","3D cover foundation"],"L Oreal Paris":["paradise Masksra","Conceler bisque","Brow Artist expert Eyebrow"],"Dior":["lip glow oil","transfer proof lipstick","lip glow balm"],"bobby brown":["mini highlightining","vitamin base","luxe lipstick"],"Maybelline":["multi use liquidblush","washable mascara makeup","lifter liner lip","glue clear eyebrow gel"]}
brand=input()
if brand in dict:
    product=(dict[brand])
    print("The Products under the brand",brand,"\n","is",product)
else:
    print("brand not available")

n1=int(input())
n2=int(input())
oper=int(input())
match oper:
    case 1:
        add=n1+n2
        print("addition",add)
    case 2:
        sub=n1-n2
        print("subtraction",sub)
    case 3:
        multiply=n1*n2
        print("multiplication",multiply)
    case 4:
        div=n1/n2
        print("division",div)
    case 5:
        exp=n1**n2
        print("exponent",exp)
    case _:
        print("invalid operation")

      
    
