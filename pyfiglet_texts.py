import pyfiglet as pyf

def figletty(){
  pyf_text =  pyf.figlet_format("How are y'all")
  # Converting string into figlet component
  
  print(pyf_text)
  # Printing the figlet component

}
figletty()
pfy_choice = str(input('Type yes if you want to try it out').lower())
if(pfy_choice == 'yes'):
  figletty()
  
