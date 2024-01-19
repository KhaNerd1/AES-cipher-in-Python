from Crypto.Cipher import AES

plain_text = "This is a top secret."
padded_plain_text = plain_text + "\v" * (AES.block_size - len(plain_text) % AES.block_size) # padding the plain text
padded_plain_text = bytes(padded_plain_text, 'utf-8') # converting the plain text to bytes

cipher_text = "764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2" # cipher text in hex format
iv = bytes.fromhex('aabbccddeeff00998877665544332211') # initial vector coverted to bytes
found = False # a boolean flag indecating whether the key is found to break from the loop or not

with open('words.txt','r') as file: 
     
    for line in file:  # reading each line 
      
      for key in line.split(): # reading each word
        
        if len(key) < 16: # if the length is less than 16 characters append (#)
          
          append = 16 - len(key)
          key = key + (append * "#")

        if len(key) > 16: # discarding the words that are more than 16 characters
            continue

        print("\nThe key: " + key) # displaying every key 
        cipher = AES.new(bytes(key, 'utf-8'), AES.MODE_CBC,iv)  # generating the cipher with the key, CBC mode and iv
        decrypted_text = cipher.encrypt(padded_plain_text) # encrypting the plain text
        decrypted_text = decrypted_text.hex()  # convert the decrypted text to hex 
        print("The tested cipher text: \n" + decrypted_text)
        
        if decrypted_text == cipher_text: # checking if the decrypted text is the given cipher text
          print('\nTHISSSSSSS ISSSSSSS THEEEEEE KEYYYYYYY!!!!!!!!')
          found = True 
          break # exit the inner loop
          
      if found == True:
        break  # exit the outer loop


