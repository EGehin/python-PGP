#!/usr/bin/python

import os, gnupg

pub = '''-----BEGIN PGP PUBLIC KEY BLOCK-----

mQENBFtg57gBCAC0qEOPsIv8hPyun4qH66/Q1ZrlfzjYIaYqNWIlogKDkC1GAZm9
tWjdCV2pKR0O7eNd2CSx563eDMaJ8pT133+lgYuGw56RIFXK8elyI5EHrRUAiHrs
RpstgImsVnlS3qlAaahDikqIKYyAITncFdhKfuuxYX0xcpTb2sqxPvExgu28fRvq
ECShWZg9RJc74XQKrQIS9VyIcNWeIR8cpR4dpfkvZynGGLb8Znevn6+IF+NNVzTo
fd1jI+g33LHzfCIV86Kd0jGZ2jSlPa0ohvBE3HIa988L/YBYCFy1wB2DyToRma9v
TExz9wRj6Sgti4W/Nga8PLccgbA0/8m6CLNjABEBAAG0EG5vIG5vIDxub0Buby5u
bz6JAU4EEwEIADgWIQRLjilMRqr/Vn2GsT6XEh4n4idVcQUCW2DnuAIbAwULCQgH
AgYVCgkICwIEFgIDAQIeAQIXgAAKCRCXEh4n4idVcZzEB/9y9TpdM2T8uk0EMzOM
OMOMC6R0guHo7necWC/9zIzRyocJzW5H8tI251jxMwJjVM+bHraYR85ZOtTljDmp
Fpt2mmG87w8NOFjVzUqMf+vjWOz4rK0fcDU6rc3MQUKwbYVWgM3zLtGJemmRP2Pw
gPlh3Van3OjIYTDGuRVHbOfYIweer46SomsNAP5oeCWKk+CnUSb2ef/2B69bfsAH
fl5X4AyHCbFbz8Qq7Twm1xgsb5fsS8b6lv7/Q0KbK27DihVVvOJOAdXtsFSYiH5a
plWpF9dWy2tYkaX4aN2sZgVhRwd5QUKq1tsrbDj6Xr8aPNIbGLKGYgfPzkfUaV8V
T9J8uQENBFtg57gBCADA5rQAfzPJcax4ckUISNaAnFJZr+V6kkEHAtMbNEI2zDdS
pzoyUCjUlDgt2M2UYxiFZgQIlAsn6WnUA+HrKiGE90Kt85pu1lSJ2T9Kx2vgHM8c
SQAFQ76OjyWurDz/psICFZa4onofNcMYShKzT4Ms7P6Yx19lfNibkL0xuCiRjEBu
BlqkZqPWElyG5pkrUH8rxCky+9HLhOmXNEsNiPzjbrOnvf1wK4+USQdaHXiEEx9Z
ibVZ1J3UmVzrLOB0T3GWMEiyq1lrIW+BSorq2A5wLFXw8ybGGS2btftzldV2svF7
4dFp3Or2MY7XS1Kjg0P5QQWnyppUb8/aEe4eGYtPABEBAAGJATYEGAEIACAWIQRL
jilMRqr/Vn2GsT6XEh4n4idVcQUCW2DnuAIbDAAKCRCXEh4n4idVcQVdB/4iSPTk
QLUl1qrnI5EWQUq9cPMVJ2Tpu4Ye3opkqyp55acoC9Yl/O6q2OcWryK/vNnrIP5/
RpjWXH0rOfnBFmDYAHrWLW9arp/gSrbbvVpEEZFs8AMyqkcRm7XYhAsNOvP+nSBH
Wqig0G5uH2zSrRYfwN+jDknyc5tUC35vT+rufv9Kz8YApUpfxxDYnRze1KXFWzNR
Bb99je2I8LSgE3dyfy5uRT2rKGiZIlTZjyNLJs6KqXGGbyBeyeupGHP7/UECuzOE
12ckBg5EQO68pK4I7Cd/oTo/xqESwg8Co6SbFp8LT4pOeETKeTebHO8OdxeAKang
VaaPseCgcArQpX7N
=JK5P
-----END PGP PUBLIC KEY BLOCK-----'''


priv = '''-----BEGIN PGP PRIVATE KEY BLOCK-----

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
qeBVpo+x4KBwCtClfs0=
=urvm
-----END PGP PRIVATE KEY BLOCK-----
'''


encryptedMessage = '''-----BEGIN PGP MESSAGE-----
Version: GnuPG v2.0.22 (GNU/Linux)

hQEMAxdNWm3a0IsOAQf+MdoyEj3juB//uk5TvdATRLFb6sjojCR5NVbbUjjYK5E2
vMob7WrWQThHYUE+8fGxTuY9foqDDXL3Gn7JvIGIUMH7l5Bhw1xRV0irNujSKPei
O+4OATVjlwf62+gBuBsq7GC+SC0MYFAzIKl1eMVlq9R76a7++Dmdvu0r9DaqHB6y
0XYfHmJKoCS1Kj/DYzbhqW3kb76xqiNlL7hfNiualdQuQkGvt1YHBF83EHrNhtxT
OuJO3jgoy9/w/7NP0CZRLORjuwD4o1MhyVcjmoRgYz5weMzjIGSkXG2ByTDEJU41
Dbvgrz4teY7tY2M15QOQcwkA4TFDWCih1Mnm4GFIMdJGAeE+/mIRj8uJwnyvvSEI
IGQJUa+YsDelcDmufsa4S11xzXl9oHYnWqJhR7kJ6Cm9CNX/j3sO3EOM9TVpk4uI
rCTrMX00OQ==
=vLy3
-----END PGP MESSAGE-----
'''


def encrypt(key, src):
	print "Cleartext string:\n", message
	print "Public key:\n", pub
	keys = gpg.import_keys(pub)
	result = gpg.encrypt(src, keys.fingerprints[0], always_trust=True)
	print "Encrypted string:\n", str(result)
	return str(result)

	if not result:
		raise RuntimeError(result.status)


def decrypt(key, src):
    keys = gpg.import_keys(priv)
    dec = gpg.decrypt(src, passphrase='no@no.no')

    print "Decrypted string:\n", str(dec)
    if not dec:
        raise RuntimeError(dec.status)

if __name__ == "__main__":
	home = os.path.join(os.getcwd(), "gnupg")
	gpg = gnupg.GPG(gnupghome=home,)

	message = "new message"

	newEncryptedMessage = encrypt(pub, message)
	decrypt(priv, newEncryptedMessage)