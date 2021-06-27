
* link reffered => https://gist.github.com/fntlnz/cf14feb5a46b2eda428e000157447309
 # STEP-1
 `


 # Create Root CA 

 ## Create Root Key

 ```
 cd /etc/nginx
 ```
 > Attention: this is the key used to sign the certificate requests, anyone holding this can sign certificates on your behalf. So keep it in a safe place!
 ```bash
 openssl genrsa -des3 -out rootCA.key 4096
 ```

 ## Create and self sign the Root Certificate

 ```
 openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
 ```
 * Here we used our root key to create the root certificate that needs to be distributed in all the computers that have to trust us.


 # Create a certificate (Done for each server)

 * This procedure needs to be followed for each server/appliance that needs a trusted certificate from our CA

 ## Create the certificate key

 ```
 openssl genrsa -out nginx.mesos.com.key 2048
 ```

 ## Create the signing  (csr)

 The certificate signing request is where you specify the details for the certificate you want to generate.
 This request will be processed by the owner of the Root key (you in this case since you create it earlier) to generate the certificate.

 **Important:** Please mind that while creating the signign request is important to specify the `Common Name` providing the IP address or domain name for the service, otherwise the certificate cannot be verified.


 ### Method A (Interactive)

 If you generate the csr in this way, openssl will ask you questions about the certificate to generate like the organization details and the `Common Name` (CN) that is the web address you are creating the certificate for, e.g `nginx.mesos.com`.

 ```
 openssl req -new -key nginx.mesos.com.key -out nginx.mesos.com.csr
 ```


 ## Verify the csr's content

 ```
 openssl req -in nginx.mesos.com.csr -noout -text
 ```

 ## Generate the certificate using the `nginx.mesos` csr and key along with the CA Root key

 ```
 openssl x509 -req -in nginx.mesos.com.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out nginx.mesos.com.crt -days 500 -sha256
 ```

 ## Verify the certificate's content

 ```
 openssl x509 -in mydomain.com.crt -text -noout
 ```

 # 2. Install nginx
 # 1. Install nginx


 > sudo apt-get update

# Install nginx

```
sudo apt-get update
sudo apt-get install nginx
```


