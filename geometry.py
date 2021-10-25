# Geometry Calculator
from math import sqrt

typeCalc = input("What Calculator? {Pythagoras, Area, Parameter, Volume} ")
tyoeCalc = typeCalc.lower()

# VOLUME
if typeCalc == "Volume":
    _input_ = input("Shape? [Prism] [Circle] [Triangle: ")
    _input_ = _input_.lower()
    vol = 0
    pie = 3.14
    if _input_ == "prism":
        l = int(input("Enter length: "))
        b = int(input("Enter width: "))
        h = int(input("Enter hight: "))
        vol = vol + (l * b * h)
        
    elif _input_ == "circle":
        r = int(input("Enter radius: "))
        vol = vol + ((4 * pie * (r ** 3) / 3))
        
    elif _input_ == "triangle":
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
        vol = vol +((b * h) / 3)
    else:
        print ("Select a valid shape")
    print ("%.2f" % vol)


# PARAMETER
if typeCalc == "parameter":
    _input_ = input("Shape? [Square] [Circle] [Rectangle] [Triangle: ")
    _input_ = _input_.lower()
    parameter = 0
    pie = 3.14
    if _input_ == "square":
        side = int(input("Enter side: "))
        parameter = parameter + (side * 4)
        
    elif _input_ == "circle":
        r = int(input("Enter radius: "))
        parameter = parameter + (2 * r * pie)
        
    elif _input_ == "rectangle":
        length = int(input("Enter length1: "))
        width = int(input("Enter length2: "))
        parameter = parameter + ((length * 2) * (width * 2))
        
    elif _input_ == "triangle":
        side1 = int(input("Enter side1: "))
        side2 = int(input("Enter side2: "))
        side3 = int(input("Enter side3: "))
        parameter = parameter + (side1 + side2 + side3)
        
    else:
        print ("Select a valid shape")
    print ("%.2f" % parameter)

# AREA
if typeCalc == "area":
  input_ = input("Shape? [Square] [Circle] [Rectangle] [Triangle: ")
  input_ = input_.lower()
    
  area = 0
  pie = 3.14
    if input_ == "square":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
        
    elif input_ == "circle":
        r = int(input("Enter the value of radius: "))
        area = area + (pie * r ** 2)
        
    elif input_ == "rectangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of length: "))
        area = area + (length * width)
        
    elif input_ == "triangle":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = area +(0.5 * base * height)
    else:
        print ("Select a valid shape")
    print ("%.2f" % area)
  
# PYTHAGORAS
if typeCalc == "pythagoras":
  formula = input('Which side (K1, K2, H) do you wish to calculate? ')
  formula = formula.lower()

  if formula == 'h':
	  side_a = int(input('K1: '))
	  side_b = int(input('K2: '))

	  side_c = sqrt(side_a * side_a + side_b * side_b)
	
	  print("H = " + str(side_c))

  elif formula == 'k1':
    side_b = int(input('K2: '))
    side_c = int(input('H: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print("K1 = " + str(side_a))

  elif formula == 'k2':
    side_a = int(input('K1: '))
    side_b = int(input('H: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print("K2 = " + str(side_c))

  else:
	  print('fck off')

