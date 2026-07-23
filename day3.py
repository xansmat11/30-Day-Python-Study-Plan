# Area of trianlge 
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is ', area)

#Perimeter of triangle
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is', perimeter)

#Weekly earning
hours = int(input('Enter hours: '))
raterPerHours = int(input('Enter rate per hours: '))
weeklyEarning = hours * raterPerHours
print('Your weekly earning is', weeklyEarning)

#Number of seconds live
numOfYears = int(input('Enter number of years you have lived: '))
totalSeconds = numOfYears * 31536000
print('You have live for', totalSeconds, 'seconds')