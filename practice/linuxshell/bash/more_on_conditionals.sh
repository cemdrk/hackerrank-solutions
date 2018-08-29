read x
read y
read z


if [ "$x" -eq "$y" ] || [ "$x" -eq "$z" ] || [ "$y" -eq "$z" ] ; then
    if [ "$x" -eq "$z" ] && [ "$x" -eq "$y" ] && [ "$y" -eq "$z" ]; then
        echo EQUILATERAL;
    else
        echo ISOSCELES;
    fi
else
    echo SCALENE;
fi
