#!bin/bash
x=5
y=10
z=$x
add=$(($x + $y))
echo "$x + $y = $add"
sub=$(($y - $x))
echo "$y - $x = $sub"
mul=$(($y * $x))
echo "$x * $y = $mul"
div=$(($y / $x))
echo "$y / $x = $div"
