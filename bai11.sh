clear
#!/bin/bash
#ham nhap mang
function nhap()
{
	echo -n "n="
	read n
	for((i=0;i<n;i++))
	do
		echo -n "a[$i]="
		read a[$i]
	done
}
#ham tim max
function max2so()
{
	if [ "$1" -gt "$2" ]
	then
		max1=$1
		echo $1
	else
		max1=$2
		echo $2
	fi
	return $max1
}
#ham tim max mang
function maxma()
{
	max=${a[0]}
	for((i=1;i<n;i++))
	do
		max=$(max2so ${a[$i]} $max)
	done
	echo "max = $max"
}
nhap
maxma
exit $?
