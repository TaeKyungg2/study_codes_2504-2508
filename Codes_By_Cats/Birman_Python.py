from math import exp,sin
from sympy import latex,symbols
from random import uniform
import pyautogui
import time
import jax.numpy as jnp
from jax import jit,grad
from time import time

def warpper(func,*arg,**kwg):
    def inn(*arg,**kwg):
        first=time()
        func()
        second=time()
        return second-first
@warpper
@jit
def time10000(n):
    sum=0
    for i in range(n):
        sum+=sin(n)
    return sum

print(time10000(10000))