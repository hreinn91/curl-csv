#!/bin/bash

touch response.output
csv_content=$(curl -sb -H "Accept: application/text" "http://localhost:5000/generate")

echo $csv_content >> response.output
#echo $'\n' >> response.output
cat response.output
