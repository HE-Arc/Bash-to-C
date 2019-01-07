#!bin/bash
if [1 -ne 3]
then
  echo "a and c are not equal !"
fi

if [2 -eq 2]
then
  echo "a and b are equal !"
  echo "hello"
else
  echo "a and c are not equal !"
fi
