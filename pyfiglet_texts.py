import pyfiglet as pyf



pyf_text = pyf.figlet_format("How are y'all")
print(pyf_text)
pyf_choice = str(input('Type yes if you want to try it\n').lower())
if pyf_choice == 'yes':
   pyf_text = pyf.figlet_format(input('Enter data :\n')
else:
     print('Arigatou')
     break
