import argparse
import os
import logging as log
import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1


def print_byte_array(byte_array):
	if(log.getLogger().getEffectiveLevel()==log.DEBUG):
		i = 0
		for data in byte_array:
			print("%0.2X " % data, end = "") 
			i = i+1
			if (i == 16):
				print(" ")
				i = 0
		print("\n\n")



def sign(private_key, input_file, out_file, key_ID):
	
    #Header
    Algo = "ECDSA_SECP256K1_SHA256"
    len_Algo = len(Algo)
    space_to_filled = 32 - len_Algo
    for x in range(space_to_filled):
        Algo = Algo + "\0"
    Algo = Algo.encode('utf-8')
    
    key_ID = int(key_ID)
    key_ID = key_ID.to_bytes(4, byteorder= 'big')
    
    Payload_size = os.path.getsize(input_file)
    print("Binary Size is :", Payload_size, "bytes")
    
    Payload_size = Payload_size.to_bytes(4, byteorder= 'big')

    #reserve bytes
    reserve_bytes = "\0"
    for x in range(23):
        reserve_bytes = reserve_bytes + "\0"
    reserve_bytes = reserve_bytes.encode('utf-8')


    # Read private key
    with open(private_key) as f:
        sk = SigningKey.from_pem(f.read(), hashlib.sha256) 

    log.info("===============Signkey=============");
    print_byte_array(sk.to_string())

    # Read input file
    with open(input_file, "rb") as f:
        in_data = f.read()

    # calculaete hash
    log.info("=======Input file hash=============");
    print_byte_array(hashlib.sha256(in_data).digest())

    # calcualte Signature	
    sig = sk.sign_deterministic(in_data, hashfunc=hashlib.sha256)
    log.info("===============Signature===========");
    print_byte_array(sig)

    #write to output file
    with open(out_file, "wb") as f:
        f.write(in_data)
        f.write(Algo)
        f.write(key_ID)
        f.write(Payload_size)
        f.write(reserve_bytes)
        f.write(sig)
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("PRIVATE_PEM", help="Private key/Sign Key pem file")
	parser.add_argument("FILE", help="File to be Sign")
	parser.add_argument("KeyID", help="ID of the Key Pair")    
	parser.add_argument("-o","--out", help="Output file")
	parser.add_argument("-v", help="for verbose -v 1")
	args = parser.parse_args()
	if args.v:
		log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
	else:
		log.basicConfig(format="%(levelname)s: %(message)s")
	if args.out:
		out_file_name = args.out
	else:
		out_file_name =  args.FILE +".signed"
	sign(args.PRIVATE_PEM,args.FILE,out_file_name, args.KeyID)
	print("Signed file \"" + out_file_name + "\" is created") 

if __name__ == "__main__":
	main()
