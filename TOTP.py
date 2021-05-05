"""
Modified from https://medium.com/analytics-vidhya/understanding-totp-in-python-bbe994606087
Any improvements are considered.
"""
import hmac, base64, struct, hashlib, time
def get_hotp_token(secret, intervals_no):
	key = base64.b32decode(secret, True)
	#decoding our key
	msg = struct.pack(">Q", intervals_no)
	#conversions between Python values and C structs represente
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = o = h[19] & 15
	#Generate a hash using both of these. Hashing algorithm is HMAC
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	#unpacking
	return h
def get_totp_token(secret):
	secret = secret.replace(" ", "")
	#ensuring to give the same otp for 30 seconds
	x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
	#adding 0 in the beginning till OTP has 6 digits
	while len(x)!=6:
		x+='0'
	return x
def is_valid_token(secret, value):
	value = value.replace(" ", "")
	return str(get_totp_token(secret)) == str(value)
if __name__ == '__main__':
	secret = 'TestTest'
	print(get_totp_token(secret))
	#print(is_valid_token(secret, get_totp_token(secret)))