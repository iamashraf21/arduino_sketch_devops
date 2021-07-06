import argparse
import logging as log
import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1


def print_byte_array(byte_array):
	if(log.getLogger().getEffectiveLevel()==log.DEBUG):
		i = 0
		for data in byte_array:
			print("%0.2X " % data, end = "") 
			i = i+1
			if (i == 32):
				print(" ")
				i = 0
		print("\n\n")



def verify(public_key,input_file):
	# Read public key
	with open(public_key) as f:
	   vk = VerifyingKey.from_pem(f.read())
	log.info("===============PUblic key===========");
	print_byte_array(vk.to_string())
	
	# Read signed file
	with open(input_file, "rb") as f:
	    message = f.read()
	
	data_length = len(message)
	data = message[:(data_length-128)]
	
	log.info("===============Data =============");
	print_byte_array(data)
	
	
	log.info("==========Signature =============");
	sig =  message[(data_length-64):data_length]
	print_byte_array(sig)

	try:
		a = vk.verify(sig, data, hashfunc=hashlib.sha256)
		print ("GOOD SIGNATURE\n\n")
	except  Exception as e:
		print("Exception - {}\n\n".format(e))
	    
	
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("PUBLIC_PEM", help="purblic key/Verify Key pem file")
	parser.add_argument("SIGNED_FILE", help="Signed file where last 64 bytes is the signature")
	parser.add_argument("-v", help="for verbose -v 1")
	args = parser.parse_args()
	if args.v:
		log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
	else:
		log.basicConfig(format="%(levelname)s: %(message)s")
	verify(args.PUBLIC_PEM,args.SIGNED_FILE)

if __name__ == "__main__":
	main()




