#!/usr/bin/env python3
import sys
import requests
import hashlib
import random
import string

rand_s = list(string.ascii_letters)
random.shuffle(rand_s)
USER = "".join(rand_s[:6])
PW = hashlib.md5("".join(rand_s[6:12]).encode()).hexdigest()

def reg(s):
	data = {
		"username": USER,
		"password": PW }
	resp = s.post(f"{URL}/register", data=data)
	assert resp.status_code == 200
	return


def login(s, username, pw):
	data = {
		"username": username,
		"password": pw}
	resp = s.post(f"{URL}/login", data=data)
	return resp


def main():
    s = requests.Session()
    data = { "debugMode": True, "language": 0 }
    resp = s.post(f"{URL}/config", json=data)
    # pw =hashlib.md5("".encode()).hexdigest()
    pw = hashlib.sha1("".encode()).hexdigest()

    resp = login(s, "admin", pw)

    print(resp.text)
    # import ipdb; ipdb.set_trace()



def usage():
	print(f"{sys.argv[0]} host")


if __name__ == "__main__":
	# if len(sys.argv) < 2:
		# usage()
		# sys.exit(0)

	host = "localhost"
	URL = f"http://{host}:9090"
	main()
