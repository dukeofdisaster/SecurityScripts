# A simle python script for generating a variety of hashes of functions
import hashlib
import sys

# First we take in the second argument passed to the system and use it as our
# designated program to hash. sys.argv will return any arguments last supplied to the system. 
# For example sys.argv[0] will return the call to the script, the string 'allHash.py', thus
# we want sys.argv[1], the designated filename passed by the user

programToHash = sys.argv[1]

HashesList = []

HashesList.append("SHA256: "+ hashlib.sha256(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA3_256: "+hashlib.sha3_256(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA512: "+ hashlib.sha512(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("MD5: " + hashlib.md5(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA3_512: "+hashlib.sha3_512(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("BLAKE2B: "+hashlib.blake2b(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA3_384: "+hashlib.sha3_384(open(programToHash, 'rb').read()).hexdigest())

# Uncomment these two lines for testing on your own system. On mine, they throw an error

#HashesList.append("SHA3_224: "+hashlib.sha3_224(open(programToHash, 'rb').read()).hexdigest())
#HashesList.append("SHAKE_128: "+hashlib.shake_128(open(programToHash, 'rb').read()).hexdigest())

HashesList.append("SHA1: "+hashlib.sha1(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("BLAKE2S: "+hashlib.blake2s(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA384: "+hashlib.sha384(open(programToHash, 'rb').read()).hexdigest())
HashesList.append("SHA224: "+hashlib.sha224(open(programToHash, 'rb').read()).hexdigest())

for i in HashesList:
    print(i+'\n')

