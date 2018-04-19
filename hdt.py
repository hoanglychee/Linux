class SV:
	def _init_(self, MSSV, HoTen, MaKhoa):
		self.MSSV = ma
		self.HoTen = ten
		self.MaKhoa = mak
	def getMSSV(self):
		return self.MSSV
	def getHoTen(self):
		return self.HoTen
	def getMaKhoa(self):
		return self.MaKhoa
	def setMSSV(self,ma):
		self.MSSV = ma
	def setHoTen(self,ten):
		self.HoTen = ten
	def setMaKhoa(self,mak):
		self.MaKhoa = mak
	def ina(self):
		print "MSSV: ", self.MSSV, ",Ho ten: ", self.HoTen, ",Ma Khoa: ", self.MaKhoa
class Khoa:
	def _init_(self, MaKhoa, TenKhoa):
		self.MaKhoa = mak
		self.TenKhoa = tenk
	def getMKhoa(self):
		return self.MaKhoa
	def getTKhoa(self):
		return self.TenKhoa
	def setMKhoa(self,mak):
		self.MaKhoa = mak
	def setTKhoa(self,tenk):
		self.TenKhoa = tenk
	def ink(self):
		print "Ma Khoa: ",self.MaKhoa, ",Ten khoa: ",self.TenKhoa
l=[]
l.append(SV("001","mai a ","57"))
l.append(SV("002","tran b","58"))
l.append(SV("003","le c  ","57"))
l.append(SV("004","pham q","58"))
l.append(SV("005","ngo m ","59"))
for i in l:
    i.ina()
print()
g=[]
g.append(Khoa("56","khoa 56 cntt"))
g.append(Khoa("57","khoa 57 cntt"))
g.append(Khoa("58","khoa 58 cntt"))              
g.append(Khoa("59","khoa 59 cntt"))
for i in g:
    i.ink()        
print()
for i in l:
    if (str(i.getMaKhoa())=="57"):
        i.xuat()



		
	
