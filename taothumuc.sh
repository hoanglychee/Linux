clear
echo "Nhap ten thu muc: "
read tentm
mkdir $tentm
if test $? -eq 0 
then
	clear
	echo "Thu muc $tentm da duoc tao "
else
	clear
	echo "Khong the tao thu muc ten $tentm"
fi
