# import os
import sys
import argparse


parser = argparse.ArgumentParser(description='Specify the institution this cert is for and pass an x509 certificate string for formatting.')
parser.add_argument('-I', '--institution', required=True, help='Enter the shortname for the institution')
parser.add_argument('-cert', type=str, required=True, help='Enter the x509 cert string wrapped by quotes', nargs=argparse.REMAINDER)
args = vars(parser.parse_args())


print(args)
print(args['institution'])
# print(args['I'])

# output = open("test.cert", "w+")
output = open("test.cert", "w+")
# text = str(args['cert'])
output.write('-----BEGIN CERTIFICATE-----' + '\n')
text = ''.join(args['cert'])
output.write(text)
output.write('\n' + '-----END CERTIFICATE-----')
output.close()

print ("")
print ("----------------------------------")
print ("Formatted cert file has been generated.")
print ("----------------------------------")
print ("")

