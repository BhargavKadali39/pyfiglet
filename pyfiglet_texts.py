import pyfiglet as pyf


def figletty():
    print(pyf_text)

pyf_text = pyf.figlet_format("How are y'all")

figletty()

while True:
    pyf_choice = str(input('Type yes if you want to try it\n').lower())
    if pyf_choice == 'yes':
        pyf_text = pyf.figlet_format(input('Enter data :\n'))
        figletty()
    else:
        print('Arigatou')
        break
