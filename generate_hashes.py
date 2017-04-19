import argparse
import hashlib

parser=argparse.ArgumentParser()
parser.add_argument('filename' ,help='Enter any file')
args=parser.parse_args()

def generate_hashes(filename):
	dict_hashes = {}
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	hasher1=hashlib.sha1()
	hasher2=hashlib.sha256()
	with open(filename, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while (len(buf) > 0):
			hasher.update(buf)
			hasher1.update(buf)
			hasher2.update(buf)
			buf = afile.read(BLOCKSIZE)
	dict_hashes["sha1"] = str(hasher1.hexdigest())
	dict_hashes["md5"] = str(hasher.hexdigest())
	dict_hashes["sha256"] = str(hasher2.hexdigest())
	return dict_hashes
	
	
filename = args.filename

# This part generates hashes. 
print("[+] Generating Hashes...")
hashes_out = generate_hashes(filename)
for x in hashes_out.keys():
	print("%s: %s" % (x, hashes_out[x]))
	
