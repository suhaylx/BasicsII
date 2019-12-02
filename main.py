is_old = True
is_licenced = True

if is_licenced and is_old:
    print("check you have license and you are old you can drive ")
else:
    print("you can not drink ! ")

#exercise

is_magician = False
is_expert = True 

if is_expert and is_magician:
  print("you are a master magician")
elif is_magician and not is_expert:
  print("at least you are getting here ")
elif not is_magician:
  print ("if you are not magician \"you need magic powers \" ")