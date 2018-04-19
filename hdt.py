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
sv1 = SV()
sv2 = SV()
sv3 = SV()
k1 = Khoa()
k2 = Khoa()
sv1.setMSSV("001")
sv1.setHoTen("Mai A")
sv1.setMaKhoa("01")
sv2.setMSSV("002")
sv2.setHoTen("Van C")
sv2.setMaKhoa("02")
sv3.setMSSV("003")
sv3.setHoTen("Thi K")
sv3.setMaKhoa("01")
sv1.ina()
sv2.ina()
sv3.ina()
k1.setMKhoa("01")
k1.setTKhoa("CNTT")
k2.setMKhoa("02")
k2.setTKhoa("Toan")
k1.ink()
k2.ink()



		
	
