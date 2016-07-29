class ipBlock:

# init method, throw an error if the syntax of the block is wrong
# self.block is the instance holding the decimal IPV4 address
# self.prefix is the instance holding the block prefix (in binary)
# self.number is the length of the block prefix
  def __init__(self, block):
    self.block = block
    try:
      self.prefix, self.number = self.findPrefix()
    except:
      print "wrong block syntax"

# method indicating whether the address in in the block
# address is the input of the function, address to be checked whether it is in the block
  def isInBlock(self, address):
    if not self.IsValidAddress(address):
      print "wrong IP address"
      return
    parseAddress = '$ ./ipblock ' + self.block + ' ' + address
    print parseAddress
    binAddress = self.toBianryAddress(address) # convert the address into binary
    if self.prefix == binAddress[:self.number]: # compare the binary address's prefix with the block's prefix
      print 'in block' 
    else:
      print 'not in block'

# method that convert all decimal IPV4 address into binary represenation and return it
  def toBianryAddress(self, address):
    arr = address.split('.')
    binAddress = ''
    temp = '00000000'
    for element in arr:
      binAddress += temp[:8-len(bin(int(element))[2:])] + bin(int(element))[2:]
    return binAddress

# method that returns the prefix of the block in binary representation and the length of the prefix
  def findPrefix(self):
    addressInBlock, number = self.block.split('/')[0], int(self.block.split('/')[1])
    binAddressInBlock = self.toBianryAddress(addressInBlock)
    return binAddressInBlock[:number], number  

# method that list all the possible address in the block
# list all the possibites after the prefix
# for every possibilty, concat with the prefix and then convert back to deciaml(variable currAddress), print it out
  def allAddressInBlock(self):
    parseAddress = '$ ./ipblock ' + self.block
    print parseAddress
    temp = '00000000000000000000000000000000'
    for i in range(2 ** (32 - self.number)):
      currAddress = self.toDecimalAddress(self.prefix + temp[:32 - self.number - len(bin(i)[2:])] + bin(i)[2:])
      print currAddress

# method that convert binary address back to decimal
  def toDecimalAddress(self,binAddress):
    DecAddress = ''
    for i in range(0,len(binAddress),8):
      DecAddress += str(int(binAddress[i:i+8], 2))
      if i != 24:
        DecAddress += '.'
    return DecAddress

# method that check whether a valid address
  def IsValidAddress(self,address):
    arr = address.split('.')
    if len(arr) !=4:
      return False
    for element in arr:
      try: 
        int(element)
      except:
        print 'wrong IP syntax'
      if int(element) >= 256 or int(element) < 0:
        return False
    return True


# Part 1
firstBlock = ipBlock('12.23.34.45/15')
firstBlock.isInBlock('12.22.35.44')

secondBlock = ipBlock('12.23.34.45/16')
secondBlock.isInBlock('12.22.35.44')

thirdBlock = ipBlock('0.0.0.0/12')
thirdBlock.isInBlock('0.100.1.124')

print '\n'

# Part 3
FourthBlock = ipBlock('12.23.34.45/29')
FourthBlock.allAddressInBlock()




