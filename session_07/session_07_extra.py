#!/usr/bin/env python3

import math

var1 = "9.2"
var2 = 17
var3 = 3.4

exercise_1 = print(type(var1), type(var2), type(var3))

var4 = "19"

exercise_2 = int(var4)
print(exercise_2, type(exercise_2))

var5 = -26
exercise_3 = str(var5)
print(exercise_3, type(exercise_3))

var6 = 83
exercise_4 = float(var6)
print(exercise_4, type(exercise_4))

exercise_5 = int(var4) + var5
print(exercise_5)

exercise_6 = var2 - float(var1)
print('%3f' % (exercise_6))

exercise_7 = var5 * var3
print('%3f' % (exercise_7))

exercise_8 = pow(var3, float(var1))
print('%3f' % (exercise_8))

var7 = 9
exercise_9 = math.sqrt(var7)
print(exercise_9)

my_radius = 10
exercise_10 = 2 * math.pi * my_radius
print(exercise_10)

total_min = 33 + 37 + 35 + 31 + 29 + 39
total_hour = total_min/60
exercise_11 = total_hour
print(exercise_11)