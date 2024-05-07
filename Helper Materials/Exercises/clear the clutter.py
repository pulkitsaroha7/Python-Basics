import random , string , os

def png(file):
    global png_counter
    if(not os.path.exists(f'{png_counter}.png')):
        os.rename(f'{file}' , f'{png_counter}.png')
        png_counter += 1
    png_counter += 1
    
def pdf(file):
    global pdf_counter
    if(not os.path.exists(f'{pdf_counter}.pdf')):
        os.rename(file , f'{pdf_counter}.pdf')
        pdf_counter += 1
    pdf_counter += 1

def jpg(file):
    global jpg_counter
    if(not os.path.exists(f'{jpg_counter}.jpg')):
        os.rename(file , f'{jpg_counter}.jpg')
        jpg_counter += 1
    jpg_counter += 1

png_counter = 1
pdf_counter = 1
jpg_counter = 1
if(not os.path.exists("Clutter File")):
    os.mkdir("Clutter file")

for i in range(15):
    xtn = random.sample(('.png' , '.pdf' , '.jpg') , 1)
    name = ''.join(random.sample(string.ascii_letters , 5))
    if(not os.path.exists(f'Clutter File/{name+str(xtn[0])}')):
        os.mkdir(f'Clutter File/{name+str(xtn[0])}')

ans = input("Do you want to clear the clutter(yes to clear and no to exit) : ")
if(ans == 'yes'):
    print("Clearing the clutter...")
    files = os.listdir('Clutter File')
    os.chdir('Clutter File')
    for file in files:
        xtn = str(os.path.splitext(f'{file}')[1])
        png(file) if xtn =='.png' else pdf(file) if xtn == '.pdf' else jpg(file)
    print("Clutter cleared")
