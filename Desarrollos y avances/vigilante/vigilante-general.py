import captura
import os

captura.captura()

os.system('cp -r Capture/* Remoto/')
os.system('python3 deep_learning_object_detection.py -i Remoto')

