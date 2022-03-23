from Solved_OneWayEnigma import *

settings = getSettings()
encryptor = Enigma(settings)

# print(Encrypt("VISHWACTF{4SSYM37R1C_3NCRYP710N_W17H_3NI6M4}", encryptor))
print(Decrypt("GHORMW5HTDVGOB4FACKXX2GY1CMIGRZSFTWKI98YA0V2", encryptor))

# No. of rotors = 5, sequence = (5,3,1,2,4), positions = (1,4,9,25,36)