temp_cel = float(input("Enter  temperature"))
if (temp_cel >=-273.15):
    temp_far = ((temp_cel*9/5)+32)
    print(f"{temp_cel}°C is equivalent to  {temp_far}°K")  
else:
    print ("Enter valid value!!! Temperature must be more than -273.15°")