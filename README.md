# file-hosting-in-python
Working http file hosting in python.
## Usage
Run server.py to start a server.
Use this command to upload a file:

<code>curl -X POST -d "file content here" 127.0.0.1 # replace 127.0.0.1 with server's ip adress</code>

## Notes
- old_server.py has vulnerability that you can execute shell code by sending POST request with body that is "hi; ls /"
