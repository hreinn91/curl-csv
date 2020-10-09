#!/bin/bash

touch response.output
csv_content=$(curl -sb -H "Accept: application/text" "http://localhost:5000/generate")

echo $csv_content >> response.output
#echo $'\n' >> response.output
cat response.output


# Some simple sftp commands
#sftp -i /path/to/ssh-key -b /path/to/sftp-commands.txt root@remote:/root/dropoff
