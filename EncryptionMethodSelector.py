# imports the hashlib package into python

import hashlib

# Imports the sys package into python

import sys

# Un comment to use the last two print lines
# the first print available hashes the machine has available but wont use
# Unless certain conditions are met
# The second give's a guarantee of available hashes on a system
# Each systme has diffrent algorithms available to use
# The listed Algorithms in the program are the most common

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

# Ask's the user to choose an encryption method from the list presented 
# or help if they need help

hash = input("Please Choose an Encryption Method.\n" 
             "Please Enter One of The Following.\n" 
             "sha3_384, blake2s, shake_256," 
             "shake_128, sha384, sha512, sha3_512," 
             "\nmd5, blake2b, sha3_256," 
             "sha256, sha3_224, sha224, sha1,\n" 
             "or help for Assistance in Choosing:" )

# If help is entered list's the algorithms and what they are

if hash == ("help"):
    
    print("\nSHA Stand's for Secure Hash Algorithm\n"
          "\nSHA1, SHA2, and SHA3 are all three diffrent algorithms\n"
          "\nsha1 has one hash function and is similar to MD5,\n"
          "sha1 is 10 bytes long.\n"
          "\nsha2 has two hash functions available SHA-224 is 28 bytes,\n" 
          "SHA-256 is 32 bytes/n, SHA-384 is 48 bytes,\n"  
          "\nSHA3 is similar to SHA2 sha3_384, sha384, sha3_512,\n"
          "\nsha3_224 is 28 bytes, sha3_256 is 32 bytes these" 
          "are all sha3 algorithms"
          "\nshake is part of SHA3 shake_128 is 128 bytes," 
          "shake_256 is 256 bytes\n"
          "\nblake2 is a strong encryption which is as fast as md5 and more secure"
          "\nblake2b is 64 bites long, blake2s is 8-32 bytes long\n"
          "\nmd5 is one of the oldest and weakest hashes"
          "\nmd5 produce a 128 bit message\n"
          "\nFor security choose any besides sha1, and md5"
          "\nFor Better encryption from the SHA family choose any sha2 or sha3\n")
    
    
    # Re ask's the user to input encription method if help was chosen

    hash = input("Now Please re Choose an Encryption Method.\n" 
                 "From The List Presented\n" 
                 "sha3_384, blake2s, shake_256," 
                 "shake_128, sha384, sha512, sha3_512," 
                 "\nmd5, blake2b, sha3_256," 
                 "sha256, sha3_224, sha224, sha1,\n" 
                 "or help for Assistance in Choosing:" ) 
    
# Requests the item that the user want's to encrypt

hash_object = input("What Would you Like To Encrypte? Please Enter It Now: ")

# If sha3_384 is chosen it with encode the message in sha3_384 algorithm and
# print the message

if hash == ("sha3_384"):
    
    hash_object = hashlib.sha3_384(hash_object.encode())

    # Change hexdigest to digest to get the byte string hexdigest gives you hex

    print(hash_object.hexdigest())

# If blake2s is chosen it with encode the message in blake2s algorithm and
# print the message    

elif hash == ("blake2s"):
        
    hash_object = hashlib.blake2s(hash_object.encode())

    # Change hexdigest to digest to get the byte string hexdigest gives you hex

    print(hash_object.hexdigest())
    
# If shake_256 is chosen it with encode the message in shake_256 algorithm and
# print the message    
    
elif hash == ("shake_256"):
        
    hash_object = hashlib.shake_256(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex    
    
    print(hash_object.hexdigest())  
     

# If shake_128 is chosen it with encode the message in shake_128 algorithm and
# print the message

elif hash == ("shake_128"):
            
    hash_object = hashlib.shake_128(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
            
    print(hash_object.hexdigest())

# If sha384 is chosen it with encode the message in sha384 algorithm and
# print the message
    
elif hash == ("sha384"):
                
    hash_object = hashlib.sha384(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                
    print(hash_object.hexdigest())

# If sha512 is chosen it with encode the message in sha512 algorithm and
# print the message
    
elif hash == ("sha512"):
            
    hash_object = hashlib.sha512(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
        
    print(hash_object.hexdigest())    

# If sha3_512 is chosen it with encode the message in sha3_512 algorithm and
# print the message
    
elif hash == ("sha3_512"):
                    
    hash_object = hashlib.sha3_512(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                    
    print(hash_object.hexdigest())            
        

# If md5 is chosen it with encode the message in md5 algorithm and
# print the message

elif hash == ("md5"):
        
    hash_object = hashlib.md5(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
        
    print(hash_object.hexdigest())    

# If blake2b is chosen it with encode the message in blake2b algorithm and
# print the message
    
elif hash == ("blake2b"):
                    
    hash_object = hashlib.blake2b(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                    
    print(hash_object.hexdigest())    

# If sha3_256 is chosen it with encode the message in sha3_256 algorithm and
# print the message
        
elif hash == ("sha3_256"):
                        
    hash_object = hashlib.sha3_256(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                        
    print(hash_object.hexdigest())           


# If sha256 is chosen it with encode the message in sha256 algorithm and
# print the message

elif hash == ("sha256"):
        
    hash_object = hashlib.sha256(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
        
    print(hash_object.hexdigest())    


# If sha3_224 is chosen it with encode the message in sha3_224 algorithm and
# print the message

elif hash == ("sha3_224"):
                                
    hash_object = hashlib.sha3_224(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                                
    print(hash_object.hexdigest())      

# If sha224 is chosen it with encode the message in sha224 algorithm and
# print the message
    
elif hash == ("sha224"):
                                    
    hash_object = hashlib.sha224(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                                    
    print(hash_object.hexdigest())
        
# If sha1 is chosen it with encode the message in sha1 algorithm and
# print the message
        
elif hash == ("sha1"):
                                    
    hash_object = hashlib.sha1(hash_object.encode())
    
    # Change hexdigest to digest to get the byte string hexdigest gives you hex
                                    
    print(hash_object.hexdigest())  

# If anything else is entered for encryption the system will exit 
# with an error Message

else:
    
    print("\n\nSorry Wrong Encryption Method Inputed." 
          "\nPlease Try Again. \nNow Exeting!!!")

    sys.exit()
