
if 
```
[SSL: CERTIFICATE_VERIFY_FAILED]
```

```
/Applications/Python\ 3.6/Install\ Certificates.command
```




```
curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
```
or 
```
sh sh curl_shell.sh

```

The -X flag and POST value indicates we're performing a POST request.

We supply -F image=@dog.jpg to indicate we're submitting form encoded data. The image key is then set to the contents of the dog.jpg file. Supplying the @ prior to dog.jpg implies we would like cURL to load the contents of the image and pass the data to the request.