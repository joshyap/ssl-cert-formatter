# ssl-cert-formatter
This CLI program should take an input string and format it as an certificate. There are 3 main format requirements for a valid certificate:

1. Starts with -----BEING CERTIFICATE-----
2. Ends with -----END CERTIFICATE-----
3. Each line has a maximum of 65 characters
4. Remove spaces (even though they are technically allowed in base 64 encoding)
 
