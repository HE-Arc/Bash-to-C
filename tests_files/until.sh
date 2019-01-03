COUNTER=20
until [  $COUNTER -lt 10 ]; do
    echo "COUNTER $COUNTER"
    COUNTER=$(($COUNTER - 1 ))
done
