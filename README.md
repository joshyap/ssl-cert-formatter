# X509-cert-formatter
This CLI program should take an input string and format it as an certificate. There are 3 main format requirements for a valid certificate:

1. Starts with -----BEING CERTIFICATE-----
2. Ends with -----END CERTIFICATE-----
3. Each line has a maximum of 64 characters
4. Remove spaces (even though they are technically allowed in base 64 encoding)
 

This script takes two required inputs in this specific order:
1. `-I` or `-institution` (This should be the customer name. The output file will be named based on this input and appended with a trailing ".cert")
2. `-cert` (This should be the actual X509 certificate text. It is usually provided by the customer in either an XML file or via a URL that contains the certificate.)

Note that any whitespace passed after the `-cert` will be stripped out. Since the certificates are often formatted in 2-3 columns of text, this means you can copy/paste the certificate text into this tool's command without any issues. 


Example command:
>python3 x509-cert-formatter.py -I customername -cert MIIDyzCCArOgAwIBAgIEKZuuezANBgkqhkiG9w0BAQsFADCBlTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEfMB0GA1UECgwWVGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMgQSZNIFVuaXZlcnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2EuZWR1MB4XDTE5MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoMFlRleGFzIEEgJiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2ZXJzaXR5LVNhbiBBbnRMIIDyzCCArOgAwIBAgIEKZuezANBgkqhkiG9w0BAQsFADCBlTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEfMB0GA1UECgwWVGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMgQSZNIFVuaXZlcnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2EuZWR1MB4XDTE5MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoMFlRleGFzIEEgJiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2ZXJzaXR5LVNhbiBBbnRMIIDyzCCArOgAwBAgIEKZuuezANBgkqhkiG9w0BAQsFADCBlTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEfMB0GA1UECgwWVGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMgQSZNIFVuaXZlcnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2EuZWR1MB4XDTE5MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoMFlRleGFzIEEgJiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2ZXJzaXR5LVNhbiBBbnR

Example output of a success:
```
---------------------------------------
Formatted cert file has been generated.
---------------------------------------
```

You should also see a `customername.cert` file in the directory you ran the command. 

The `customername.cert` file will look like: 
>-----BEGIN CERTIFICATE-----
<br>MIIDyzCCArOgAwIBAgIEKZuuezANBgkqhkiG9w0BAQsFADCBlTELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEfMB0GA1UECgwW
VGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMgQSZNIFVuaXZl
cnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2EuZWR1MB4XDTE5
MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYTAlVTMQswCQYD
VQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoMFlRleGFzIEEg
JiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2ZXJzaXR5LVNh
biBBbnRMIIDyzCCArOgAwIBAgIEKZuezANBgkqhkiG9w0BAQsFADCBlTELMAkGA1
UEBhMCVVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEfMB0GA1
UECgwWVGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMgQSZNIF
VuaXZlcnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2EuZWR1MB
4XDTE5MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYTAlVTMQ
swCQYDVQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoMFlRleG
FzIEEgJiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2ZXJzaX
R5LVNhbiBBbnRMIIDyzCCArOgAwBAgIEKZuuezANBgkqhkiG9w0BAQsFADCBlTEL
MAkGA1UEBhMCVVMxCzAJBgNVBAgTAlRYMRQwEgYDVQQHEwtTYW4gQW50b25pbzEf
MB0GA1UECgwWVGV4YXMgQSAmIE0gVW5pdmVyc2l0eTEpMCcGA1UECwwgVGV4YXMg
QSZNIFVuaXZlcnNpdHktU2FuIEFudG9uaW8xFzAVBgNVBAMTDmVlaS50YW11c2Eu
ZWR1MB4XDTE5MDYwNTE0NDc1OVoXDTM0MDYwMTE0NDc1OVowgZUxCzAJBgNVBAYT
AlVTMQswCQYDVQQIEwJUWDEUMBIGA1UEBxMLU2FuIEFudG9uaW8xHzAdBgNVBAoM
FlRleGFzIEEgJiBNIFVuaXZlcnNpdHkxKTAnBgNVBAsMIFRleGFzIEEmTSBVbml2
ZXJzaXR5LVNhbiBBbnR
<br>-----END CERTIFICATE-----


Once a correctly formatted certificate is generated, you can use it to generate a SHA1 fingerprint:

```openssl x509 -noout -fingerprint -in certname.cert```
