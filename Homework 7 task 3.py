import os
import shutil

MAI = os.path.join(os.getcwd(), 'templates', 'mainapp')
AUT = os.path.join(os.getcwd(), 'templates', 'authapp')
MAI_DATA = os.path.join(os.getcwd(), 'mainapp', 'templates', 'mainapp')
AUT_DATA = os.path.join(os.getcwd(), 'authapp', 'templates', 'authapp')


os.makedirs(MAI, exist_ok=True)
os.makedirs(AUT, exist_ok=True)

for data in os.scandir(MAI_DATA):
    shutil.copy2(os.path.join(MAI_DATA, data.name), os.path.join(MAI, data.name))
for data_aut in os.scandir(AUT_DATA):
    shutil.copy2(os.path.join(AUT_DATA, data_aut.name), os.path.join(AUT, data_aut.name))