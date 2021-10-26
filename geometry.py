# Geometry Calculator
from math import sqrt

typeCalc = input("What Calculator? {Pythagoras, Area, Parameter, Volume} ")
tyoeCalc = typeCalc.lower()

# VOLUME
def volume():
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
def parameter():
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
def area():
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
def pythagoras():
  formula = input('Which side (O, A, H) do you wish to calculate? ')
  formula = formula.lower()

  if formula == 'h':
	  side_a = int(input('o: '))
	  side_b = int(input('a: '))

	  side_c = sqrt(side_a * side_a + side_b * side_b)
	
	  print("H = " + str(side_c))

  elif formula == 'o':
    side_b = int(input('a: '))
    side_c = int(input('h: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print("O = " + str(side_a))

  elif formula == 'a':
    side_a = int(input('o: '))
    side_b = int(input('h: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print("A = " + str(side_c))

  else:
	  print('fck off')

if typeCalc == "Volume":
    volume()
elif typeCalc == "parameter":
    parameter()
elif typeCalc == "area":
    area()
elif typeCalc == "pythagoras":
    pythagoras()