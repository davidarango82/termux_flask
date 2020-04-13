#!/bin/bash
echo "starting shell script!\n"

# fetch data from sensor_data_db:
echo "reading data from db..."
input="sensor_data_db"
while IFS= read -r line
do
  echo "$line"
  echo "$line" >> temperature.txt

done < "$input"
