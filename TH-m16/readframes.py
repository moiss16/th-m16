import wave
import numpy as np
import matplotlib.pyplot as plt
#cargar archivo wav en la variable

goodmorning = wave.open('good-morningMan.wav', 'r')
goodafternoon = wave.open('good-afternoon.wav', 'r')
hello = wave.open('hello.wav', 'r')
bass = wave.open('bass.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)
framesaf = goodafternoon.readframes(-1)
framesh = hello.readframes(-1)
framesb = bass.readframes(-1)

#mostrar el resultado de frames
#print(frames[:10])

#Convierte el audio good morning de bytes a enteros

ondaconvertida = np.frombuffer(frames, dtype='int16')
ondaconvertidaaf = np.frombuffer(framesaf, dtype='int16')
ondaconvertidah = np.frombuffer(framesh, dtype='int16')
ondaconvertidab = np.frombuffer(framesb, dtype='int16')

frameratemor = goodmorning.getframerate()
framerateaf = goodafternoon.getframerate()
framerateh = hello.getframerate()
framerateb = bass.getframerate()

#Mostrar los primeros 10 int
print(frameratemor)
print(framerateaf)
print(framerateh)
print(framerateb)

timemor = np.linspace(start=0, stop=len(ondaconvertida)/frameratemor, num=len(ondaconvertida))
timeaf = np.linspace(start=0, stop=len(ondaconvertidaaf)/framerateaf, num=len(ondaconvertidaaf))
timeh = np.linspace(start=0, stop=len(ondaconvertidah)/framerateh, num=len(ondaconvertidah))
timeb = np.linspace(start=0, stop=len(ondaconvertidab)/framerateb, num=len(ondaconvertidab))

print(timemor[:10])
print(timeaf[:10])
print(timeh[:10])
print(timeb[:10])

plt.title("Good morning vs good afternoon")

plt.xlabel("Tiempo segundos")
plt.ylabel("Amplitud")

plt.plot(timemor, ondaconvertida, label="good morning")
plt.plot(timeaf, ondaconvertidaaf,label="good afternoon", alpha=0.5)
plt.plot(timeh, ondaconvertidah,label="hello", alpha=0.6)
plt.plot(timeb, ondaconvertidab,label="bass", alpha=0.7)

plt.legend()
plt.show()