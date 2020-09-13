import sys
import argparse
import textwrap


parser = argparse.ArgumentParser(description='Specify the institution this cert is for and pass an x509 certificate string for formatting.')
parser.add_argument('-I', '--institution', required=True, help='Enter the shortname for the institution')
parser.add_argument('-cert', type=str, required=True, help='Enter the x509 cert string wrapped by quotes', nargs=argparse.REMAINDER)
args = vars(parser.parse_args())

# write new file if not existing or write over existing file with same institution name
output = open(str(args['institution'] + '.cert'), "w+")
output.write('-----BEGIN CERTIFICATE-----' + '\n')
# join all the cert input strings to remove white spaces
text = ''.join(args['cert']) 
# limit each line to 64 characters as per certificate format rules
text = textwrap.fill(text, 64)
output.write(text)
output.write('\n' + '-----END CERTIFICATE-----')
output.close()

print ("")
print ("---------------------------------------")
print ("Formatted cert file has been generated.")
print ("---------------------------------------")
print ("")

