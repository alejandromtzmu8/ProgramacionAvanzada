# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oDFrNjrrXi-INOC9Gpg06-L2u8SSTKK0
"""

import time
import random

##implementación del algoritmo de ordenamiento burbuja
def dubble_sort(arr):
  n=len(arr)
  for i in range(n):
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
#Implementacion del algoritmo de ordenamiento QuickSort
def quicksort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[len(arr)//2]
  left=[x for x in arr if x<pivot]
  middle=[x for x in arr if x==pivot]
  right=[x for x in arr if x>pivot]
  return quicksort(left)+middle+quicksort(right)

#Funcion que mide tiempo de ejecución
def measure_time(sort_algorithm,data):
   start_time=time.time()
   sort_algorithm(data)
   end_time=time.time()
   return end_time-start_time

#Pruebas de rendimientos con dif. tamaños
tamaños=[100, 500, 1000, 5000, 10000]
resultados={}
for tamaño in tamaños:
  random_lista=[random.randint(1,10000) for _ in range(tamaño)]

  #Tiempo con Bubble Sort
  bubble_data=random_lista.copy()
  bubble_time=measure_time(dubble_sort,bubble_data)
  lista_ordenadaS = dubble_sort(bubble_data)

  #Tiempo con Qicksort
  quick_data=random_lista.copy()
  quick_time=measure_time(lambda arr: quicksort(arr),quick_data)
  lista_ordenada = quicksort(quick_data)

  resultados[tamaño]={"Bubble Sort":bubble_time,"Quick Sort":quick_time}

#Mostrar resultados
for tamaño, times in resultados.items():
  print(f"Tamaño de la lista: {tamaño}")
  if tamaño==10000:
    print(f"Lista original (primeros 10 elementos): {random_lista[:10]}")
    print(f"Lista ordenada BS (10 primeros): {bubble_data[:10]}")
    print(f"Tiempo Bubble Sort: {times['Bubble Sort']:.6f} segundos")
    print(f"Lista ordenada QS (10 primeros): {lista_ordenada[:10]}")
    print(f"Tiempo Quick Sort: {times['Quick Sort']:.6f} segundos")
  else:
    print(f"Tiempo Bubble Sort: {times['Bubble Sort']:.6f} segundos")
    print(f"Tiempo Quick Sort: {times['Quick Sort']:.6f} segundos")
  print()

