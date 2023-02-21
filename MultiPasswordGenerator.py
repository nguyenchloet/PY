#!/bin/python3
# modified version of raspberrypi password generator project from https://projects.raspberrypi.org/en/projects/password-generator modified

import random
import math
# define 
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
symbols = ';!&%$#'

# pick random length between 8 and 12 inclusive for password
# r = random.randint(8,12)

# check that input values are greater than 0
# check that password is at least 8 characters
length = input("Enter desired password length: ")
length = int(length)
while (length < 8):
    if (length <= 0):
      length = input("Enter a value greater than 0:")
      length = int(length)
    if (length < 8 and length > 0):
      length = input("For a secure password, enter a value greater than 8:")
      length = int(length)

num_pw = input("How many passwords would you like to create?")
num_pw = int(num_pw)
while (num_pw <= 0):
  num_pw = input("Enter a value greater than 0:")
  num_pw = int(num_pw)

# get a certain amount of chars, nums, and symbols in the password based on length
# 70% chars, 20% nums, 10%symbols
num_chars = length * .7
num_chars = math.floor(num_chars)
#print("number of chars: ",num_chars)

num_nums = length * .2
num_nums = math.ceil(num_nums)
#print("number of nums: ",num_nums)

num_symbols = length - num_chars - num_nums;
#print("num symbols: ", num_symbols)


for p in range(num_pw):
  password = ''
  for c in range(num_chars):
    password += random.choice(chars)
  for c in range(num_nums):
    password += random.choice(nums)
  for c in range(num_symbols):
    password += random.choice(symbols)

  # password with a certain ration of elements, but in order
  # print("Password before shuffle: ",password)

  # shuffle ordered password
  randomize = list(password)
  random.shuffle(randomize)
  result = ''.join(randomize)
  print("Password",p+1,": ",result)
