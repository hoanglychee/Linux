clear
#!/bin/sh
echo "Chuong trinh tim xau $1 trong tap tin $2"
{
	dodaitu=`expr length "$1"`
	while read textline
	do
		dodaidong=`expr length "$textline"`
		end=$(($dodaidong-dodaitu+1))
		index=1
		while [ $index -le $end ]
		do
			temp=`expr substr "$textline" $index $dodaitu`
			if [ "$temp" = "$1" ]
			then
				echo "Tim thay $1 tai dong $textline"
				break
			fi
			index=$(($index +1))
		done
	done
}<$2
exit 0
