def check_bit4(input):
  mask = 0b1000
  desired=input & mask
  if desired > 0:
    return "on"
  else:
    return "off"
	
#############################
# turn 3rd bit on
a = 0b10111011
mask = 0b0100
desired =  a | mask
print bin(desired)

###############################
# Flip the bits
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

##############################
#slip and slide, flip n th bit

def flip_bit(number, n):
  mask= (0b1 << n-1)
  result = number ^ mask
  return bin(result)