import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1 

def print_byte_array(byte_array):
	i = 0
	for data in byte_array:
		print("%0.2X " % data, end = "") 
		i = i+1
		if (i == 16):
			print(" ")
			i = 0
	print("\n\n")
	
#Generate keyPair and save both to disk

def main():
	print("Generating random private key & public key pair with SECP256k1 curve")
	sk = SigningKey.generate(curve=SECP256k1, hashfunc=hashlib.sha256)
	print("==========Private======================")
	print_byte_array(sk.to_string())
	print("==========Public======================")
	vk = sk.verifying_key
	print_byte_array(vk.to_string())

	with open("private.pem", "wb") as f:
		f.write(sk.to_pem())
	with open("public.pem", "wb") as f:
		f.write(vk.to_pem())
	print("private.pem , public.pem saved")


if __name__ == "__main__":
	main()
