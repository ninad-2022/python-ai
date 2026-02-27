city = "Mumxai"
match city:
    case "Mumbai"|"Pune" :print("city of maharashtra")
    case "Banglore"|"Karnatak" :print("city of south")
    case _:print("invalid city")


age = 18
match age:
    case a if a < 18:
        print("your too yound, to get liscance")
    case a if a >= 18 and a<=65:
        print("your eligibile for the liscance")
    case a if a > 65:
        print("your too old to get the liscane")
    case _:print("Invlalid")