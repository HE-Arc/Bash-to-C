a=1
b=1

if [$(($a + $b)) -ne 3]
then
  echo "a and c not equals !"
fi

if [$a -eq $b]
then
  echo "Equal !"
else
  echo "Not equal !"
fi
