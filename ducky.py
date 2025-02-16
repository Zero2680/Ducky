from pygame import *
from random import *
from cut_scenes import *
screen = display.set_mode((1280, 720), FULLSCREEN)
display.set_caption('Juego')

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.color = color
		self.vidas = vidas
		self.direccionx = direccionx
		self.direcciony = direcciony

	def DibujarObjeto(self):
		draw.rect(screen, self.color, (self.x,self.y,self.ancho,self.largo))

class Personaje(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
		self.huevo1 = Huevo(self.x, self.y, 10, 10, (255,0,0), 1, 0, 0)
		self.huevo2 = Huevo(self.x, self.y, 10, 10, (255,0,0), 1, 0, 0)
		self.huevo3 = Huevo(self.x, self.y, 10, 10, (255,0,0), 1, 0, 0)
	
	def Movimiento(self):
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if keys[K_w]==1:
			self.direcciony = 1
			if y > 0:
				self.y -= 1
		if keys[K_s]:
			self.direcciony = 0
			if y < 700:
				self.y += 1
		if keys[K_a]==1:
			self.direccionx = 0
			self.direcciony = 2
			if x > 0:
				self.x -= 1
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			if x < 1260:
				self.x += 1

	def Disparar(self, plataforma):
		keys = key.get_pressed()
		self.huevo1.Movimiento1(plataforma)
		if keys[K_w]==0 and keys[K_s]==0 and keys[K_a]==0 and keys[K_d]==0:
			self.huevo2.Movimiento2(plataforma)
			self.huevo3.Movimiento3(plataforma)
			if self.direcciony != 2:
				self.huevo2.y = self.huevo1.y
				self.huevo3.y = self.huevo1.y
			else:
				self.huevo2.x = self.huevo1.x
				self.huevo3.x = self.huevo1.x
		else:
			self.huevo2.y = 10000
			self.huevo3.y = 10000

	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Boss(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
		self.disparo1 = Disparo(920, 0, 20, 20, (255,0,0), 0, 0, 1)
		self.disparo2 = Disparo(560, 360, 20, 20, (255,0,0), 360, 1, 1)
		self.disparo3 = Disparo(920, 720, 20, 20, (255,0,0), 720, 1, 0)
		self.disparo4 = Disparo(1280, 360, 20, 20, (255,0,0), 1080, 0, 0)
		self.disparo5 = Disparo(360, 0, 20, 20, (255,0,0), 0, 1, 1)
		self.disparo6 = Disparo(0, 360, 20, 20, (255,0,0), 360, 1, 0)
		self.disparo7 = Disparo(360, 720, 20, 20, (255,0,0), 720, 0, 0)
		self.disparo8 = Disparo(720, 360, 20, 20, (255,0,0), 1080, 0, 1)
		self.disparo9 = Disparo(640, 0, 20, 20, (255,0,0), 0, 0, 1)
		self.disparo10 = Disparo(280, 360, 20, 20, (255,0,0), 360, 1, 1)
		self.disparo11 = Disparo(640, 720, 20, 20, (255,0,0), 720, 1, 0)
		self.disparo12 = Disparo(1000, 360, 20, 20, (255,0,0), 1080, 0, 0)
		self.tentaculo1 = Disparo(plataforma.x-250, 0, 20, 720, (255,0,0), 1, 1, 0)
		self.tentaculo2 = Disparo(plataforma.x+250, 0, 20, 720, (255,0,0), 1, 1, 0)
	
	def Movimiento(self): #MOVIMIENTO TORTUGA CAPARAZON
		global sonido
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if self.direccionx == 0:
			self.x -= 2
		if self.direccionx == 1:
			self.x += 2
		if self.direcciony == 0:
			self.y -= 2
		if self.direcciony == 1:
			self.y += 2
		if self.x <= 0:
			self.direccionx = 1
		if self.x >= 1080:
			self.direccionx = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 520:
			self.direcciony = 0
	
	def Movimiento2(self): #MOVIMIENTO MURCIELAGO
		global boss_attack, sonido
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if sonido == False:
			sound.play()
			sonido = True
		if self.direccionx == 0:
			if self.direcciony == 1:
				self.x = 1500
				self.y = 50
				self.direcciony = 0
			if self.y == 50:
				self.x -= 2
				self.y = 50
				if self.x < -100:
					self.y = 400
			else:
				self.x += 2
				self.y = 400
		if self.direccionx == 1:
			if self.direcciony == 1:
				self.x = 1500
				self.y = 400
				self.direcciony = 0
			if self.y == 400:
				self.x -= 2
				self.y = 400
				if self.x < -100:
					self.y = 50
			else:
				self.x += 2
				self.y = 50

	def Movimiento3(self): #MOVIMIENTO MEDUSA
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if self.direccionx == 0:
			self.x -= 0.5
		if self.direccionx == 1:
			self.x += 0.5
		if self.direcciony == 0:
			self.y -= 0.5
		if self.direcciony == 1:
			self.y += 0.5
		if self.x <= 0:
			self.direccionx = 1
		if self.x >= 1080:
			self.direccionx = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 520:
			self.direcciony = 0
	
	def Movimiento4(self): #MOVIMIENTO MONO
		global sonido, movimiento
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if sonido == False:
			sound.play()
			sonido = True
		if self.direcciony == 0:
			self.y -= 0.5
			if self.y == -200:
				pos = randrange(0,2)
				self.direcciony = 1
				sonido = False
				if self.x == 540:
					if pos == 0:
						self.x = 260
					if pos == 1:
						self.x = 820
				elif self.x == 260:
					if pos == 0:
						self.x = 540
					if pos == 1:
						self.x = 820
				elif self.x == 820:
					if pos == 0:
						self.x = 260
					if pos == 1:
						self.x = 540
		if self.direcciony == 1:
			self.y += 0.5
			if self.y == 50:
				movimiento = False
				self.direcciony = 2
			
	def Movimiento5(self): #MOVIMIENTO DEMONIO
		global boss_attack
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if self.direcciony == 0:
			self.y -= 0.5
			sound.play()
			if self.y == -250 or self.x > 1280:
				self.x = 540
				self.y = -250
				self.direcciony = 1
				sound.stop()
		if self.direcciony == 1:
			self.y += 0.5
			if self.y == 260:
				self.direcciony = 2

	def Caparazones(self, enemigo):
		self.disparo1.Movimiento_Caparazon(enemigo)
		self.disparo2.Movimiento_Caparazon(enemigo)
		self.disparo3.Movimiento_Caparazon(enemigo)

	def Murcielagos(self):
		self.disparo1.Movimiento_Murcielago()
		self.disparo3.Movimiento_Murcielago()
		self.disparo4.Movimiento_Murcielago()
		self.disparo6.Movimiento_Murcielago()

	def Medusas(self):
		self.disparo1.Movimiento_Medusa()
		self.disparo2.Movimiento_Medusa()
		self.disparo3.Movimiento_Medusa()
		self.disparo4.Movimiento_Medusa()
		self.disparo5.Movimiento_Medusa()
		self.disparo6.Movimiento_Medusa()

	def Tentaculos(self):
		self.tentaculo1.Movimiento_Tentaculo()
		self.tentaculo2.Movimiento_Tentaculo()
	
	def Platanos(self):
		self.disparo1.Movimiento_Platano()
		self.disparo2.Movimiento_Platano()
		self.disparo3.Movimiento_Platano()
		self.disparo4.Movimiento_Platano()
		self.disparo5.Movimiento_Platano()
		self.disparo6.Movimiento_Platano()
		self.disparo7.Movimiento_Platano()
		self.disparo8.Movimiento_Platano()
		self.disparo9.Movimiento_Platano()
		self.disparo10.Movimiento_Platano()
		self.disparo11.Movimiento_Platano()
		self.disparo12.Movimiento_Platano()

class Huevo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)

	def Movimiento1(self, plataforma):
		global x1, y1, x2, y2, x3, y3, sonido_huevo
		if (Personaje.check_colisiones(self, enemigo) == True or Personaje.check_colisiones(self, enemigo2) == True or Personaje.check_colisiones(self, enemigo3) == True) and sonido_huevo == False:
			sound_huevo.play()
			sonido_huevo = True
		if Personaje.check_colisiones(self, enemigo) == True:
			enemigo.vidas -= 1
		if Personaje.check_colisiones(self, enemigo2) == True:
			enemigo2.vidas -= 1
		if Personaje.check_colisiones(self, enemigo3) == True:
			enemigo3.vidas -= 1
		if plataforma.direcciony == 1:
			y1 += 2
			self.y = plataforma.y - y1
			self.x = plataforma.x
			if (y1 == 100):
				self.y = plataforma.y
				sonido_huevo = False
				y1 = 0
		elif plataforma.direcciony == 0:
			y1 += 2
			self.y = plataforma.y + y1
			self.x = plataforma.x
			if (y1 == 100):
				self.y = plataforma.y
				sonido_huevo = False
				y1 = 0
		else:
			if plataforma.direccionx == 1:
				x1 += 2
				self.x = plataforma.x + x1
				self.y = plataforma.y
				if (x1 == 100):
					self.x = plataforma.x
					sonido_huevo = False
					x1 = 0
			if plataforma.direccionx == 0:
				x1 += 2
				self.x = plataforma.x - x1
				self.y = plataforma.y
				if (x1 == 100):
					self.x = plataforma.x
					sonido_huevo = False
					x1 = 0

	def Movimiento2(self, plataforma):
		global x1, y1, x2, y2, x3, y3, sonido_huevo
		if (Personaje.check_colisiones(self, enemigo) == True or Personaje.check_colisiones(self, enemigo2) == True or Personaje.check_colisiones(self, enemigo3) == True) and sonido_huevo == False:
			sound_huevo.play()
			sonido_huevo = True
		if Personaje.check_colisiones(self, enemigo) == True:
			enemigo.vidas -= 1
		if Personaje.check_colisiones(self, enemigo2) == True:
			enemigo2.vidas -= 1
		if Personaje.check_colisiones(self, enemigo3) == True:
			enemigo3.vidas -= 1
		if plataforma.direcciony == 1:
			y2 += 2
			self.y = plataforma.y - y2
			self.x -= 1
			if (y2 == 100):
				self.x = plataforma.x
				self.y = plataforma.y
				y2 = 0
		elif plataforma.direcciony == 0:
			y2 += 2
			self.y = plataforma.y + y2
			self.x -= 1
			if (y2 == 100):
				self.x = plataforma.x
				self.y = plataforma.y
				y2 = 0
		else:
			if plataforma.direccionx == 1:
				x2 += 2
				self.x = plataforma.x + x2
				self.y -= 1
				if (x2 == 100):
					self.x = plataforma.x
					self.y = plataforma.y
					x2 = 0
			if plataforma.direccionx == 0:
				x2 += 2
				self.x = plataforma.x - x2
				self.y -= 1
				if (x2 == 100):
					self.x = plataforma.x
					self.y = plataforma.y
					x2 = 0
	
	def Movimiento3(self, plataforma):
		global x1, y1, x2, y2, x3, y3, sonido_huevo
		if (Personaje.check_colisiones(self, enemigo) == True or Personaje.check_colisiones(self, enemigo2) == True or Personaje.check_colisiones(self, enemigo3) == True) and sonido_huevo == False:
			sound_huevo.play()
			sonido_huevo = True
		if Personaje.check_colisiones(self, enemigo) == True:
			enemigo.vidas -= 1
		if Personaje.check_colisiones(self, enemigo2) == True:
			enemigo2.vidas -= 1
		if Personaje.check_colisiones(self, enemigo3) == True:
			enemigo3.vidas -= 1
		if plataforma.direcciony == 1:
			y3 += 2
			self.y = plataforma.y - y3
			self.x += 1
			if (y3 == 100):
				self.x = plataforma.x
				self.y = plataforma.y
				y3 = 0
		elif plataforma.direcciony == 0:
			y3 += 2
			self.y = plataforma.y + y3
			self.x += 1
			if (y3 == 100):
				self.x = plataforma.x
				self.y = plataforma.y
				y3 = 0
		else:
			if plataforma.direccionx == 1:
				x3 += 2
				self.x = plataforma.x + x3
				self.y += 1
				if (x3 == 100):
					self.x = plataforma.x
					self.y = plataforma.y
					x3 = 0
			if plataforma.direccionx == 0:
				x3 += 2
				self.x = plataforma.x - x3
				self.y += 1
				if (x3 == 100):
					self.x = plataforma.x
					self.y = plataforma.y
					x3 = 0

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def Movimiento_Caparazon(self, enemigo):
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
			self.x = enemigo.x
			self.y = enemigo.y
		if self.direccionx == 0:
			self.x -= 2
		if self.direccionx == 1:
			self.x += 2
		if self.direcciony == 0:
			self.y -= 2
		if self.direcciony == 1:
			self.y += 2
		if self.x <= 0:
			self.direccionx = 1
		if self.x >= 1260:
			self.direccionx = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 700:
			self.direcciony = 0
	
	def Movimiento_Murcielago(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
			self.x = 1280
			self.y = 210
		if self.direccionx == 0:
			self.x -= 2
		if self.direccionx == 1:
			self.x += 2
		if self.direcciony == 0:
			self.y -= 5
		if self.direcciony == 1:
			self.y += 5
		if self.x <= 0 and self.direccionx == 0:
			self.x = 1260
		if self.x >= 1280 and self.direccionx == 1:
			self.x = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 700:
			self.direcciony = 0

	def Movimiento_Medusa(self):
		global y_medusa_aux
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
			self.y = 0
		self.y += 0.2
		y_medusa_aux += 0.1
		if y_medusa_aux >= 600:
			self.y -= 0.6
			if self.direccionx == 0:
				self.x -= 1
			elif self.direccionx == 1:
				self.x += 1
			if y_medusa_aux >= 660:
				y_medusa_aux = 0
				self.direccionx = randrange(0,2)
		if self.y >= 700:
			self.y = -50
		if self.x <= 0:
			self.direccionx = 1
		if self.x >= 1260:
			self.direccionx = 0
	
	def Movimiento_Tentaculo(self):
		global tent, sonido
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if sonido == False:
			sound.play()
			sonido = True
		if tent != 2:
			if self.direccionx == 1:
				self.x += 1
			if self.direccionx == 0:
				self.x -= 1
		if self.x > 1280 or self.x < 0:
			tent = 2
	
	def Movimiento_Platano(self): #GIROS
		global plat
		if Personaje.check_colisiones(self, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
			self.x += 1500
		if self.direccionx == 1:
			self.x += 1
		if self.direccionx == 0:
			self.x -= 1
		if self.direcciony == 1:
			self.y += 1
		if self.direcciony == 0:
			self.y -= 1
		self.vidas += 1
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 720:
			self.direcciony = 0
		if self.vidas == 360 or self.vidas == 1080:
			if self.direccionx == 1:
				self.direccionx = 0
			elif self.direccionx == 0:
				self.direccionx = 1
		if self.vidas == 1440:
			self.vidas = 0
			if self.x >= 1500:
				self.x -= 1500

estanque = transform.scale(image.load("ducky_images/fondo.jpg").convert(), (1280, 857))
plataforma = Personaje(625, 350, 20, 20,(255,255,255), 3, 1, 2)
pato01 = transform.scale(image.load("ducky_images/pato01.png"), (50, 50))
pato11 = transform.scale(image.load("ducky_images/pato11.png"), (50, 50))
pato02 = transform.scale(image.load("ducky_images/pato02.png"), (50, 50))
pato12 = transform.scale(image.load("ducky_images/pato12.png"), (50, 50))
corazon1 = transform.scale(image.load("ducky_images/corazon1.png"), (40, 40))
corazon2 = transform.scale(image.load("ducky_images/corazon2.png"), (40, 40))
enemigo = Boss(540, 210, 200, 200,(255,255,255), 10000, 1, 1)
enemigo2 = Boss(160, -250, 200, 200,(255,255,255), 250, 1, 0)
enemigo3 = Boss(920, -250, 200, 200,(255,255,255), 250, 1, 0)
tortuga1 = transform.scale(image.load("ducky_images/tortuga1.png"), (300, 300))
tortuga2 = transform.scale(image.load("ducky_images/tortuga2.png"), (300, 300))
caparazon_boss1 = transform.scale(image.load("ducky_images/caparazon_boss1.png"), (300, 300))
caparazon_boss2 = transform.scale(image.load("ducky_images/caparazon_boss2.png"), (300, 300))
caparazon1 = transform.scale(image.load("ducky_images/caparazon1.png"), (50, 50))
caparazon2 = transform.scale(image.load("ducky_images/caparazon2.png"), (50, 50))
cueva = transform.scale(image.load("ducky_images/cueva.jpg").convert(), (1280, 720))
murcielago1 = transform.scale(image.load("ducky_images/murcielago1.png"), (50, 50))
murcielago2 = transform.scale(image.load("ducky_images/murcielago2.png"), (50, 50))
murcielago1r = transform.scale(image.load("ducky_images/murcielago1r.png"), (50, 50))
murcielago2r = transform.scale(image.load("ducky_images/murcielago2r.png"), (50, 50))
murcielago1_boss = transform.scale(image.load("ducky_images/murcielago1.png"), (300, 300))
murcielago2_boss = transform.scale(image.load("ducky_images/murcielago2.png"), (300, 300))
murcielago1r_boss = transform.scale(image.load("ducky_images/murcielago1r.png"), (300, 300))
murcielago2r_boss = transform.scale(image.load("ducky_images/murcielago2r.png"), (300, 300))
murcielago3 = transform.scale(image.load("ducky_images/murcielago3.png"), (300, 300))
murcielago4 = transform.scale(image.load("ducky_images/murcielago4.png"), (300, 300))
huevo = transform.scale(image.load("ducky_images/huevo.png"), (50, 50))
mar = transform.scale(image.load("ducky_images/mar.jpg").convert(), (1280, 720))
medusa_boss1 = transform.scale(image.load("ducky_images/medusa_boss1.png"), (300, 300))
medusa_boss2 = transform.scale(image.load("ducky_images/medusa_boss2.png"), (300, 300))
medusa1 = transform.scale(image.load("ducky_images/medusa1.png"), (50, 50))
medusa2 = transform.scale(image.load("ducky_images/medusa2.png"), (50, 50))
medusa3 = transform.scale(image.load("ducky_images/medusa3.png"), (50, 50))
tentaculo = transform.scale(image.load("ducky_images/tentaculo.png"), (300, 720))
selva = transform.scale(image.load("ducky_images/selva.jpg").convert(), (1280, 720))
mono1 = transform.scale(image.load("ducky_images/liana1.png"), (300, 300))
mono2 = transform.scale(image.load("ducky_images/liana2.png"), (300, 300))
platano = transform.scale(image.load("ducky_images/banana.png"), (50, 50))
mazmorra = transform.scale(image.load("ducky_images/mazmorra2.jpg").convert(), (1280, 720))
penguin = transform.scale(image.load("ducky_images/demonio.png"), (300, 300))
platanop = transform.scale(image.load("ducky_images/bananap.png"), (50, 50))
caparazon1p = transform.scale(image.load("ducky_images/caparazon1p.png"), (50, 50))
caparazon2p = transform.scale(image.load("ducky_images/caparazon2p.png"), (50, 50))
medusa1p = transform.scale(image.load("ducky_images/medusa1p.png"), (50, 50))
medusa2p = transform.scale(image.load("ducky_images/medusa2p.png"), (50, 50))
medusa3p = transform.scale(image.load("ducky_images/medusa3p.png"), (50, 50))
murcielago1p = transform.scale(image.load("ducky_images/murcielago1p.png"), (50, 50))
murcielago2p = transform.scale(image.load("ducky_images/murcielago2p.png"), (50, 50))
tentaculop = transform.scale(image.load("ducky_images/tentaculop.png"), (300, 720))
orbe = transform.scale(image.load("ducky_images/orbe.png"), (50, 50))
patop = transform.scale(image.load("ducky_images/patop.png"), (50, 50))
sound_mono = mixer.Sound('ducky_sounds/mono.ogg')
sound_tortuga = mixer.Sound('ducky_sounds/tortuga.ogg')
sound_medusa = mixer.Sound('ducky_sounds/medusa.ogg')
sound_murcielago = mixer.Sound('ducky_sounds/murcielago.ogg')
sound_demonio = mixer.Sound('ducky_sounds/demonio.ogg')
sound_huevo = mixer.Sound('ducky_sounds/huevo.ogg')
sound_huevo.set_volume(0.75)
sound_lose = mixer.Sound('ducky_sounds/lose.ogg')
sound_golpe = mixer.Sound('ducky_sounds/golpe.ogg')
sound_texto = mixer.Sound('ducky_sounds/texto.ogg')
disparo1_1 = caparazon1p
disparo1_2 = caparazon2p
disparo2_1 = medusa1p
disparo2_2 = medusa2p
disparo3_1 = murcielago1p
disparo3_2 = murcielago2p
disparo4_1 = platanop
animacion_pato = 0
animacion_boss = 0
animacion_disparo = 0
animacion_disparo2 = 0
animacion_corazon = 0
x_boss = 65
y_boss = 65
level = 1
z = 0
w = 0
orbe_x = 540
orbe_y = 50
cut_scene_manager = CutSceneManager(screen)

while True:
	global x1, y1, x2, y2, x3, y3, boss_attack, y_medusa_aux, tent, sonido, sonido_huevo, movimiento
	if z == 0:
		x1 = 0
		y1 = 0
		x2 = 0
		y2 = 0
		x3 = 0
		y3 = 0
		boss_attack = 0
		y_medusa_aux = 0
		tent = 0
		sonido = False
		sonido_huevo = False
		movimiento = False
		mixer.music.set_volume(0.25)
		cut_scene_manager.start_cut_scene(CutSceneZero(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 1
	animacion_pato += 1
	animacion_boss += 1
	animacion_disparo += 1
	animacion_corazon += 1
	boss_attack += 1
	plataforma.Movimiento()
	if level == 1 and z == 1:
		fondo = selva
		plataforma.x = 625
		plataforma.y = 350
		plataforma.direccionx = 1
		enemigo.x = 540
		enemigo.y = 50
		enemigo.largo = 200
		enemigo.direcciony = 0
		enemigo.disparo1.x = 920
		enemigo.disparo1.y = 0
		enemigo.disparo1.vidas = 0
		enemigo.disparo1.direccionx = 0
		enemigo.disparo1.direcciony = 1
		enemigo.disparo2.x = 560
		enemigo.disparo2.y = 360
		enemigo.disparo2.vidas = 360
		enemigo.disparo2.direccionx = 1
		enemigo.disparo2.direcciony = 1
		enemigo.disparo3.x = 920
		enemigo.disparo3.y = 720
		enemigo.disparo3.vidas = 720
		enemigo.disparo3.direccionx = 1
		enemigo.disparo3.direcciony = 0
		enemigo.disparo4.x = 1280
		enemigo.disparo4.y = 360
		enemigo.disparo4.vidas = 1080
		enemigo.disparo4.direccionx = 0
		enemigo.disparo4.direcciony = 0
		enemigo.disparo5.x = 360
		enemigo.disparo5.y = 0
		enemigo.disparo5.vidas = 0
		enemigo.disparo5.direccionx = 1
		enemigo.disparo5.direcciony = 1
		enemigo.disparo6.x = 0
		enemigo.disparo6.y = 360
		enemigo.disparo6.vidas = 360
		enemigo.disparo6.direccionx = 1
		enemigo.disparo6.direcciony = 0
		enemigo.disparo7.x = 360
		enemigo.disparo7.y = 720
		enemigo.disparo7.vidas = 720
		enemigo.disparo7.direccionx = 0
		enemigo.disparo7.direcciony = 0
		enemigo.disparo8.x = 720
		enemigo.disparo8.y = 360
		enemigo.disparo8.vidas = 1080
		enemigo.disparo8.direccionx = 0
		enemigo.disparo8.direcciony = 1
		enemigo.disparo9.x = 640
		enemigo.disparo9.y = 0
		enemigo.disparo9.vidas = 0
		enemigo.disparo9.direccionx = 0
		enemigo.disparo9.direcciony = 1
		enemigo.disparo10.x = 280
		enemigo.disparo10.y = 360
		enemigo.disparo10.vidas = 360
		enemigo.disparo10.direccionx = 1
		enemigo.disparo10.direcciony = 1
		enemigo.disparo11.x = 640
		enemigo.disparo11.y = 720
		enemigo.disparo11.vidas = 720
		enemigo.disparo11.direccionx = 1
		enemigo.disparo11.direcciony = 0
		enemigo.disparo12.x = 1000
		enemigo.disparo12.y = 360
		enemigo.disparo12.vidas = 1080
		enemigo.disparo12.direccionx = 0
		enemigo.disparo12.direcciony = 0
		boss1 = mono1
		boss2 = mono2
		disparo1 = platano
		disparo2 = platano
		disparo3 = platano
		disparo4 = platano
		next_boss1 = tortuga1
		next_boss2 = tortuga2
		mixer.music.load('ducky_sounds/musica_mono.ogg')
		mixer.music.set_volume(mixer.music.get_volume())
		sound = sound_mono
		sound.set_volume(0.5)
		sonido = False
		cut_scene_manager.start_cut_scene(CutSceneOneStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			mixer.music.play(-1)
			z = 2
	if level == 2 and z == 2:
		plataforma.x = 50
		plataforma.y = 260
		plataforma.direccionx = 1
		enemigo.x = 540
		enemigo.y = 210
		enemigo.direcciony = 1
		enemigo.disparo1.x = enemigo.x
		enemigo.disparo1.y = 100
		enemigo.disparo1.direccionx = randrange(0,2)
		enemigo.disparo1.direcciony = randrange(0,2)
		enemigo.disparo2.x = enemigo.x
		enemigo.disparo1.y = 350
		enemigo.disparo1.direccionx = randrange(0,2)
		enemigo.disparo1.direcciony = randrange(0,2)
		enemigo.disparo3.x = enemigo.x
		enemigo.disparo1.y = 600
		enemigo.disparo1.direccionx = randrange(0,2)
		enemigo.disparo1.direcciony = randrange(0,2)
		fondo = estanque
		boss1 = tortuga1
		boss2 = tortuga2
		next_boss1 = medusa_boss1
		next_boss2 = medusa_boss2
		disparo1 = caparazon1
		disparo2 = caparazon2
		mixer.music.load('ducky_sounds/musica_tortuga.ogg')
		mixer.music.set_volume(mixer.music.get_volume())
		sound = sound_tortuga
		sound.set_volume(0.5)
		sonido = False
		w = 0
		cut_scene_manager.start_cut_scene(CutSceneTwoStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			boss_attack = 0
			mixer.music.play(-1)
			z = 3
	if level == 3 and z == 3:
		plataforma.x = 400
		plataforma.y = 390
		plataforma.direccionx = 1
		enemigo.x = 650
		enemigo.y = 290
		enemigo.ancho = 50
		enemigo.largo = 175
		enemigo.direccionx = 1
		x_boss = 125
		enemigo.disparo4.direcciony = randrange(0,2)
		enemigo.disparo5.direcciony = randrange(0,2)
		enemigo.disparo6.direcciony = randrange(0,2)
		fondo = mar
		boss1 = medusa_boss1
		boss2 = medusa_boss2
		disparo1 = medusa1
		disparo2 = medusa2
		disparo3 = medusa1
		disparo4 = medusa2
		next_boss1 = murcielago3
		next_boss2 = murcielago4
		mixer.music.load('ducky_sounds/musica_medusa.ogg')
		mixer.music.set_volume(mixer.music.get_volume())
		sound = sound_medusa
		sound.set_volume(0.1)
		sonido = False
		w = 0
		movimiento = False
		cut_scene_manager.start_cut_scene(CutSceneThreeStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			mixer.music.play(-1)
			z = 4
	if level == 4 and z == 4:
		fondo = cueva
		plataforma.x = 625
		plataforma.y = 350
		plataforma.direccionx = 1
		enemigo.x = 540
		enemigo.y = 50
		enemigo.ancho = 160
		x_boss = 65
		enemigo.direccionx = 0
		enemigo.direcciony = 1
		enemigo.disparo1.x = 0
		enemigo.disparo3.x = -280
		enemigo.disparo4.x = 1260
		enemigo.disparo6.x = 1540
		enemigo.disparo1.direccionx = 1
		enemigo.disparo3.direccionx = 1
		enemigo.disparo4.direccionx = 0
		enemigo.disparo6.direccionx = 0
		boss1 = murcielago3
		boss2 = murcielago4
		next_boss1 = penguin
		next_boss2 = penguin
		disparo1 = murcielago1
		disparo2 = murcielago2
		disparo3 = murcielago1r
		disparo4 = murcielago2r
		enemigo.disparo2.x = -100
		enemigo.disparo5.x = -100
		mixer.music.load('ducky_sounds/musica_murcielago.ogg')
		mixer.music.set_volume(mixer.music.get_volume())
		sound = sound_murcielago
		sound.set_volume(0.25)
		sonido = False
		w = 0
		cut_scene_manager.start_cut_scene(CutSceneFourStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			boss_attack = 0
			mixer.music.play(-1)
			z = 5
	if level == 5 and z == 5:
		fondo = mazmorra
		plataforma.x = 625
		plataforma.y = 625
		plataforma.direccionx = 1
		enemigo.x = 540
		enemigo.y = 260
		x_boss = 50
		y_boss = 50
		enemigo.direcciony = 0
		enemigo.ancho = 200
		enemigo.largo = 200
		enemigo.vidas = 5000
		enemigo.direcciony = 0
		enemigo.disparo1.x = 920
		enemigo.disparo1.y = 0
		enemigo.disparo1.vidas = 0
		enemigo.disparo1.direccionx = 0
		enemigo.disparo1.direcciony = 1
		enemigo.disparo2.x = 560
		enemigo.disparo2.y = 360
		enemigo.disparo2.vidas = 360
		enemigo.disparo2.direccionx = 1
		enemigo.disparo2.direcciony = 1
		enemigo.disparo3.x = 920
		enemigo.disparo3.y = 720
		enemigo.disparo3.vidas = 720
		enemigo.disparo3.direccionx = 1
		enemigo.disparo3.direcciony = 0
		enemigo.disparo4.x = 1280
		enemigo.disparo4.y = 360
		enemigo.disparo4.vidas = 1080
		enemigo.disparo4.direccionx = 0
		enemigo.disparo4.direcciony = 0
		enemigo.disparo5.x = 360
		enemigo.disparo5.y = 0
		enemigo.disparo5.vidas = 0
		enemigo.disparo5.direccionx = 1
		enemigo.disparo5.direcciony = 1
		enemigo.disparo6.x = 0
		enemigo.disparo6.y = 360
		enemigo.disparo6.vidas = 360
		enemigo.disparo6.direccionx = 1
		enemigo.disparo6.direcciony = 0
		enemigo.disparo7.x = 360
		enemigo.disparo7.y = 720
		enemigo.disparo7.vidas = 720
		enemigo.disparo7.direccionx = 0
		enemigo.disparo7.direcciony = 0
		enemigo.disparo8.x = 720
		enemigo.disparo8.y = 360
		enemigo.disparo8.vidas = 1080
		enemigo.disparo8.direccionx = 0
		enemigo.disparo8.direcciony = 1
		enemigo.disparo9.x = 640
		enemigo.disparo9.y = 0
		enemigo.disparo9.vidas = 0
		enemigo.disparo9.direccionx = 0
		enemigo.disparo9.direcciony = 1
		enemigo.disparo10.x = 280
		enemigo.disparo10.y = 360
		enemigo.disparo10.vidas = 360
		enemigo.disparo10.direccionx = 1
		enemigo.disparo10.direcciony = 1
		enemigo.disparo11.x = 640
		enemigo.disparo11.y = 720
		enemigo.disparo11.vidas = 720
		enemigo.disparo11.direccionx = 1
		enemigo.disparo11.direcciony = 0
		enemigo.disparo12.x = 1000
		enemigo.disparo12.y = 360
		enemigo.disparo12.vidas = 1080
		enemigo.disparo12.direccionx = 0
		enemigo.disparo12.direcciony = 0
		boss1 = penguin
		boss2 = penguin
		disparo4_1 = platanop
		mixer.music.load('ducky_sounds/musica_demonio.ogg')
		mixer.music.set_volume(mixer.music.get_volume())
		sound = sound_demonio
		sound.set_volume(0.5)
		sonido = False
		enemigo.vidas = 20000
		w = 0
		cut_scene_manager.start_cut_scene(CutSceneFiveStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			mixer.music.play(-1)
			z = 6
	if z > 0:
		screen.blit(next_boss1, [0, 0])
		screen.blit(next_boss2, [0, 0])
		screen.blit(fondo, [0, 0])
	else:
		screen.fill((0,0,0))
	#NIVELES
	if cut_scene_manager.cut_scene is None:
		if Personaje.check_colisiones(enemigo, plataforma) == True:
			sound_golpe.play()
			plataforma.vidas -= 1
		if level == 1:
			enemigo.Platanos()
			if (enemigo.vidas <= 8000 and w == 0) or (enemigo.vidas <= 6000 and w == 1) or (enemigo.vidas <= 4000 and w == 2) or (enemigo.vidas <= 2000 and w == 3):
				movimiento = True
				sonido = False
				enemigo.direcciony = 0
				w += 1
			if movimiento == True:
				enemigo.Movimiento4()
		if level == 2:
			if enemigo.vidas < 7000 and w == 0:
				boss_attack = 0
				w = 1
			if enemigo.vidas < 7000:
				if boss_attack >= 2000:
					sonido = False
					boss_attack = 0
				if sonido == False:
					sound.play()
					sonido = True
				if boss_attack < 1100:
					if boss_attack > 100:
						if animacion_boss <= 100:
							screen.blit(caparazon_boss1, [enemigo.x-65, enemigo.y-65])
						if animacion_boss > 100:
							screen.blit(caparazon_boss2, [enemigo.x-65, enemigo.y-65])
							if animacion_boss >= 200:
								animacion_boss = 0
					if boss_attack > 200:
						enemigo.Movimiento()
			enemigo.Caparazones(enemigo)
		if level == 3:
			enemigo.Medusas()
			enemigo.Movimiento3()
			animacion_boss -= 0.5
			animacion_disparo -= 1
			if (enemigo.vidas <= 8500 and w == 0) or (enemigo.vidas <= 7000 and w == 1) or (enemigo.vidas <= 5500 and w == 2) or (enemigo.vidas <= 4000 and w == 3) or (enemigo.vidas <= 3000 and w == 4) or (enemigo.vidas <= 2000 and w == 5) or (enemigo.vidas <= 1000 and w == 6):
				movimiento = True
				w += 1
			if movimiento == False and tent == 2:
				sonido = False
				tent = 0
			if movimiento == True:
				if tent == 0:
					enemigo.tentaculo1.x = plataforma.x - 200
					enemigo.tentaculo2.x = plataforma.x + 200
					if plataforma.x < 640:
						enemigo.tentaculo1.direccionx = 1
						enemigo.tentaculo2.direccionx = 1
					if plataforma.x >= 640:
						enemigo.tentaculo1.direccionx = 0
						enemigo.tentaculo2.direccionx = 0
					tent = 1
				if tent == 2:
					enemigo.tentaculo1.x = 1300
					enemigo.tentaculo2.x = 1300
					sound.stop()
					movimiento = False
				sound.play()
				enemigo.Tentaculos()
				screen.blit(tentaculo, [enemigo.tentaculo1.x-150, enemigo.tentaculo1.y])
				screen.blit(tentaculo, [enemigo.tentaculo2.x-150, enemigo.tentaculo2.y])
			if y_medusa_aux < 600:
				animacion_disparo = 30
			elif y_medusa_aux >= 600:
				animacion_disparo = 0
		if level == 4:
			enemigo.Murcielagos()
			if enemigo.vidas < 9000 and w == 0:
				boss_attack = 0
				w = 1
			if enemigo.vidas < 9000:
				if boss_attack < 2000:
					enemigo.Movimiento2()
					enemigo.largo = 150
					if animacion_boss <= 100:
						if enemigo.direccionx == 0:
							if enemigo.y == 50:
								screen.blit(murcielago1r_boss, [enemigo.x-65, enemigo.y-65])
							elif enemigo.y == 400:
								screen.blit(murcielago1_boss, [enemigo.x-65, enemigo.y-65])
						elif enemigo.direccionx == 1:
							if enemigo.y == 50:
								screen.blit(murcielago1_boss, [enemigo.x-65, enemigo.y-65])
							elif enemigo.y == 400:
								screen.blit(murcielago1r_boss, [enemigo.x-65, enemigo.y-65])
					if animacion_boss > 100:
						if enemigo.direccionx == 0:
							if enemigo.y == 50:
								screen.blit(murcielago2r_boss, [enemigo.x-65, enemigo.y-65])
							elif enemigo.y == 400:
								screen.blit(murcielago2_boss, [enemigo.x-65, enemigo.y-65])
						if enemigo.direccionx == 1:
							if enemigo.y == 50:
								screen.blit(murcielago2_boss, [enemigo.x-65, enemigo.y-65])
							elif enemigo.y == 400:
								screen.blit(murcielago2r_boss, [enemigo.x-65, enemigo.y-65])
						if animacion_boss >= 200:
							animacion_boss = 0
				else:
					if boss_attack < 3000:
						enemigo.x = 540
						enemigo.y = 50
						enemigo.largo = 200
					else:
						if enemigo.direccionx == 0:
							enemigo.direccionx = 1
						else:
							enemigo.direccionx = 0
						enemigo.direcciony = 1
						boss_attack = 0
						sonido = False
		if level == 5:
			if 16000 < enemigo.vidas <= 19000: #LEVEL 1
				if enemigo.y != 260 and enemigo.direcciony == 2:
					enemigo.y += 0.5
				enemigo.Platanos()
				if (enemigo.vidas <= 18500 and w == 0) or (enemigo.vidas <= 18000 and w == 1) or (enemigo.vidas <= 17500 and w == 2) or (enemigo.vidas <= 17000 and w == 3) or (enemigo.vidas <= 16500 and w == 3):
					movimiento = True
					sonido = False
					enemigo.direcciony = 0
					w += 1
				if movimiento == True:
					enemigo.Movimiento4()
			if enemigo.vidas <= 16000: #DESCANSO
				if z == 6:
					enemigo.direcciony = 0
					w = 0
					z = 7
				enemigo.disparo9.Movimiento_Platano()
				enemigo.disparo10.Movimiento_Platano()
				enemigo.disparo11.Movimiento_Platano()
				enemigo.disparo12.Movimiento_Platano()
				if enemigo.vidas > 15000:
					enemigo.Movimiento5()
			if 12000 < enemigo.vidas <= 15000: #LEVEL 2
				if z == 7:
					enemigo.direcciony = 1
					boss_attack = 0
					z = 8
				if boss_attack >= 2000:
					sonido = False
					boss_attack = 0
				if sonido == False:
					sound.play()
					sonido = True
				if boss_attack < 1100:
					if boss_attack > 200:
						enemigo.Movimiento()
					else:
						enemigo.y = 260
				enemigo.Caparazones(enemigo)
			if enemigo.vidas <= 12000: #DESCANSO
				if z == 8:
					enemigo.direcciony = 0
					w = 0
					z = 9
				enemigo.disparo1.Movimiento_Caparazon(enemigo)
				enemigo.disparo2.Movimiento_Caparazon(enemigo)
				if enemigo.vidas > 11000:
					enemigo.Movimiento5()
			if 8000 < enemigo.vidas <= 11000: #LEVEL 3
				if z == 9:
					enemigo.direcciony = 1
					z = 10
				enemigo.disparo3.Movimiento_Medusa()
				enemigo.disparo4.Movimiento_Medusa()
				enemigo.disparo5.Movimiento_Medusa()
				enemigo.Movimiento3()
				animacion_boss -= 0.5
				if (enemigo.vidas <= 10500 and w == 0) or (enemigo.vidas <= 10000 and w == 1) or (enemigo.vidas <= 9500 and w == 2) or (enemigo.vidas <= 9000 and w == 3) or (enemigo.vidas <= 8750 and w == 4) or (enemigo.vidas <= 8500 and w == 5) or (enemigo.vidas <= 8250 and w == 6):
					movimiento = True
					w += 1
				if movimiento == False and tent == 2:
					sonido = False
					tent = 0
				if movimiento == True:
					if tent == 0:
						enemigo.tentaculo1.x = plataforma.x - 200
						enemigo.tentaculo2.x = plataforma.x + 200
						if plataforma.x < 640:
							enemigo.tentaculo1.direccionx = 1
							enemigo.tentaculo2.direccionx = 1
						if plataforma.x >= 640:
							enemigo.tentaculo1.direccionx = 0
							enemigo.tentaculo2.direccionx = 0
						tent = 1
					if tent == 2:
						enemigo.tentaculo1.x = 1300
						enemigo.tentaculo2.x = 1300
						sound.stop()
						movimiento = False
					sound.play()
					enemigo.Tentaculos()
					screen.blit(tentaculo, [enemigo.tentaculo1.x-150, enemigo.tentaculo1.y])
					screen.blit(tentaculo, [enemigo.tentaculo2.x-150, enemigo.tentaculo2.y])
				if y_medusa_aux < 600:
					animacion_disparo2 = 30
				elif y_medusa_aux >= 600:
					animacion_disparo2 = 0
			if enemigo.vidas <= 8000: #DESCANSO
				if z == 10:
					enemigo.direcciony = 0
					w = 0
					z = 11
				enemigo.disparo3.Movimiento_Medusa()
				enemigo.disparo4.Movimiento_Medusa()
				enemigo.disparo5.Movimiento_Medusa()
				if y_medusa_aux < 600:
					animacion_disparo2 = 30
				elif y_medusa_aux >= 600:
					animacion_disparo2 = 0
				if enemigo.vidas > 7000:
					enemigo.Movimiento5()		
			if 4000 < enemigo.vidas <= 7000: #LEVEL 4
				if z == 11:
					enemigo.direcciony = 1
					boss_attack = 0
					z = 12
				enemigo.disparo6.Movimiento_Murcielago()
				enemigo.disparo7.Movimiento_Murcielago()
				enemigo.disparo8.Movimiento_Murcielago()
				if boss_attack < 2000:
					enemigo.Movimiento2()	
				else:
					if boss_attack < 5000:
						enemigo.Movimiento5()
					else:
						if enemigo.direccionx == 0:
							enemigo.direccionx = 1
						else:
							enemigo.direccionx = 0
						enemigo.direcciony = 1
						boss_attack = 0
						sonido = False
			if enemigo.vidas <= 4000: #DESCANSO
				if z == 12:
					enemigo.direcciony = 0
					z = 13
				enemigo.disparo6.Movimiento_Murcielago()
				enemigo.disparo7.Movimiento_Murcielago()
				enemigo.disparo8.Movimiento_Murcielago()
				if enemigo.vidas > 3000:
					enemigo.Movimiento5()
					if z == 14:
						enemigo2.y = enemigo.y
						enemigo3.y = enemigo.y
					if enemigo.y <= -200:
						z = 14
			if 0 < enemigo.vidas <= 3000: #LEVEL FINAL
				if z == 14:
					boss_attack = 0
					enemigo.direcciony = 1
					z = 15
				if boss_attack >= 3000:
					boss_attack = 0
					enemigo.direcciony = 0
				if boss_attack < 1000:
					if boss_attack > 100:
						enemigo.Movimiento()
						enemigo2.Movimiento()
						enemigo3.Movimiento()
				if enemigo2.vidas <= 0:
					enemigo2.y = -250
				if enemigo3.vidas <= 0:
					enemigo3.y = -250
				if enemigo2.vidas <= 0 and enemigo3.vidas <= 0:
					boss_attack = 0
					enemigo.Movimiento5()
					if enemigo.y <= -200:
						z = 16
				if z == 16:
					boss_attack = 0
					enemigo.Movimiento5()
					enemigo2.x = 160
					enemigo3.x = 920
					enemigo2.y = enemigo.y
					enemigo3.y = enemigo.y
					enemigo2.vidas = 500
					enemigo3.vidas = 500
					if enemigo.y == 260:
						enemigo.direcciony = 1
						z = 17
			if 16000 < enemigo.vidas <= 19000:
				disparo1_1 = disparo4_1
				disparo1_2 = disparo4_1
				disparo2_1 = disparo4_1
				disparo2_2 = disparo4_1
				disparo3_1 = disparo4_1
				disparo3_2 = disparo4_1
			if 12000 < enemigo.vidas <= 15000:
				disparo1_1 = caparazon1p
				disparo1_2 = caparazon2p
			if 8000 < enemigo.vidas <= 11000:
				disparo2_1 = medusa1p
				disparo2_2 = medusa2p
			if 4000 < enemigo.vidas <= 7000:
				disparo3_1 = murcielago1p
				disparo3_2 = murcielago2p
			if enemigo.vidas <= 19000:
				screen.blit(disparo4_1, [enemigo.disparo9.x-15, enemigo.disparo9.y-15])
				screen.blit(disparo4_1, [enemigo.disparo10.x-15, enemigo.disparo10.y-15])
				screen.blit(disparo4_1, [enemigo.disparo11.x-15, enemigo.disparo11.y-15])
				screen.blit(disparo4_1, [enemigo.disparo12.x-15, enemigo.disparo12.y-15])
			if (16000 < enemigo.vidas <= 19000) or (enemigo.vidas <= 15000):
				if animacion_disparo <= 25:
					screen.blit(disparo1_1, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
					screen.blit(disparo1_1, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
					if enemigo.vidas > 12000:
						screen.blit(disparo1_1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo1_2, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
					screen.blit(disparo1_2, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
					if enemigo.vidas > 12000:
						screen.blit(disparo1_2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
			if (16000 < enemigo.vidas <= 19000) or (enemigo.vidas <= 11000):
				if animacion_disparo2 <= 25:
					screen.blit(disparo2_1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
					screen.blit(disparo2_1, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
					screen.blit(disparo2_1, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo2 > 25:
					screen.blit(disparo2_2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
					screen.blit(disparo2_2, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
					screen.blit(disparo2_2, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
			if (16000 < enemigo.vidas <= 19000) or (enemigo.vidas <= 7000):
				if animacion_disparo <= 25:
					screen.blit(disparo3_1, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
					screen.blit(disparo3_1, [enemigo.disparo7.x-15, enemigo.disparo7.y-15])
					screen.blit(disparo3_1, [enemigo.disparo8.x-15, enemigo.disparo8.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo3_2, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
					screen.blit(disparo3_2, [enemigo.disparo7.x-15, enemigo.disparo7.y-15])
					screen.blit(disparo3_2, [enemigo.disparo8.x-15, enemigo.disparo8.y-15])
		#ANIMACION HUEVO
		screen.blit(huevo, [plataforma.huevo1.x-20, plataforma.huevo1.y-20])
		screen.blit(huevo, [plataforma.huevo2.x-20, plataforma.huevo2.y-20])
		screen.blit(huevo, [plataforma.huevo3.x-20, plataforma.huevo3.y-20])
		#ANIMACION DISPARO
		if level != 5:
			if animacion_disparo <= 25:
				screen.blit(disparo1, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
			if animacion_disparo > 25:
				screen.blit(disparo2, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
			if animacion_disparo <= 25:
				screen.blit(disparo1, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
			if animacion_disparo > 25:
				screen.blit(disparo2, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
			if animacion_disparo <= 25:
				screen.blit(disparo1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
			if animacion_disparo > 25:
				screen.blit(disparo2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
			if level == 1 or level == 3 or level == 4 or (level == 5 and 4000 < enemigo.vidas <= 4900):
				if animacion_disparo <= 25:
					screen.blit(disparo3, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo4, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
				if animacion_disparo <= 25:
					screen.blit(disparo3, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo4, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo <= 25:
					screen.blit(disparo3, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo4, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
			if level == 1 or level == 5:
				if level == 1 or (level == 5 and 16000 < enemigo.vidas <= 19000):
					screen.blit(disparo1, [enemigo.disparo7.x-15, enemigo.disparo7.y-15])
					screen.blit(disparo1, [enemigo.disparo8.x-15, enemigo.disparo8.y-15])
				screen.blit(disparo1, [enemigo.disparo9.x-15, enemigo.disparo9.y-15])
				screen.blit(disparo1, [enemigo.disparo10.x-15, enemigo.disparo10.y-15])
				screen.blit(disparo1, [enemigo.disparo11.x-15, enemigo.disparo11.y-15])
				screen.blit(disparo1, [enemigo.disparo12.x-15, enemigo.disparo12.y-15])
		if animacion_disparo >= 50:
			animacion_disparo = 0
		#ANIMACION CORAZON
		if animacion_corazon <= 75:
			if plataforma.vidas >= 1:
				screen.blit(corazon1, [1060, 10])
				if plataforma.vidas >= 2:
					screen.blit(corazon2, [1140, 10])
					if plataforma.vidas == 3:
						screen.blit(corazon1, [1220, 10])
		if animacion_corazon > 75:
			if plataforma.vidas >= 1:
				screen.blit(corazon2, [1060, 10])
				if plataforma.vidas >= 2:
					screen.blit(corazon1, [1140, 10])
					if plataforma.vidas == 3:
						screen.blit(corazon2, [1220, 10])
			if animacion_corazon >= 150:
				animacion_corazon = 0
		plataforma.Disparar(plataforma)
	#ANIMACION PATO
	if plataforma.direccionx == 0:
		if animacion_pato <= 25:
			screen.blit(pato01, [plataforma.x-15, plataforma.y-15])
		if animacion_pato > 25:
			screen.blit(pato02, [plataforma.x-15, plataforma.y-15])
			if animacion_pato >= 50:
				animacion_pato = 0
	if plataforma.direccionx == 1:
		if animacion_pato <= 25:
			screen.blit(pato11, [plataforma.x-15, plataforma.y-15])
		if animacion_pato > 25:
			screen.blit(pato12, [plataforma.x-15, plataforma.y-15])
			if animacion_pato >= 50:
				animacion_pato = 0
	#ANIMACION BOSS
	if z > 0:
		if (level != 2 and level != 4) or (((boss_attack < 100 or boss_attack >= 1100) and level == 2) or w == 0) or ((boss_attack >= 2000 and level == 4) or w == 0):
			if animacion_boss <= 100:
				screen.blit(boss1, [enemigo.x-x_boss, enemigo.y-y_boss])
			if animacion_boss > 100:
				screen.blit(boss2, [enemigo.x-x_boss, enemigo.y-y_boss])
				if animacion_boss >= 200:
					animacion_boss = 0
		if level == 5:
			if enemigo2.vidas > 0:
				screen.blit(boss1, [enemigo2.x-x_boss, enemigo2.y-y_boss])
			if enemigo3.vidas > 0:
				screen.blit(boss1, [enemigo3.x-x_boss, enemigo2.y-y_boss])
	#CUT_SCENE
	if enemigo.vidas <= 0:
		mixer.music.stop()
		plataforma.vidas = 3
		if level == 1:
			plataforma.x = 625
			plataforma.y = 350
			plataforma.direccionx = 1
			enemigo.x = 540
			enemigo.y = 50
			cut_scene_manager.start_cut_scene(CutSceneOneFinal(plataforma))
		if level == 2:
			plataforma.x = 400
			plataforma.y = 390
			plataforma.direccionx = 1
			enemigo.x = 650
			enemigo.y = 290
			cut_scene_manager.start_cut_scene(CutSceneTwoFinal(plataforma))
		if level == 3:
			plataforma.x = 400
			plataforma.y = 390
			plataforma.direccionx = 1
			enemigo.x = 650
			enemigo.y = 290
			cut_scene_manager.start_cut_scene(CutSceneThreeFinal(plataforma))
		if level == 4:
			plataforma.x = 625
			plataforma.y = 350
			plataforma.direccionx = 1
			enemigo.x = 540
			enemigo.y = 50
			cut_scene_manager.start_cut_scene(CutSceneFourFinal(plataforma))
		if level == 5:
			plataforma.x = 625
			plataforma.y = 350
			plataforma.direccionx = 0
			enemigo.x = 540
			enemigo.y = 50
			enemigo2.vidas = 0
			enemigo3.vidas = 0
			if orbe_y < plataforma.y-25:
				orbe_y += 0.5
			if orbe_y >= plataforma.y-25 and orbe_y != 1000:
				orbe_y = 1000
				pato01 = patop
				pato11 = patop
				pato02 = patop
				pato12 = patop
			screen.blit(orbe, [orbe_x+75, orbe_y])
			cut_scene_manager.start_cut_scene(CutSceneFiveFinal(plataforma))
		if cut_scene_manager.cut_scene is None:
			enemigo.vidas = 10000
			level += 1
			if level == 5:
				enemigo.vidas = 20000
	if level == 6:
		screen.fill((0, 0, 0))
		cut_scene_manager.start_cut_scene(CutSceneSix(plataforma))
		if cut_scene_manager.cut_scene is None:
			quit()
			exit()
	cut_scene_manager.update()
	cut_scene_manager.draw()
	display.flip()
	if plataforma.vidas <= 0:
		sound_lose.play()
		cut_scene_manager.cut_scenes_complete = []
		z -= 1
		enemigo.vidas = 10000
		if level == 5:
			enemigo.vidas = 20000
			z = 5
		plataforma.vidas = 3
	for evento in event.get():
		if evento.type==QUIT:
				quit()
				exit()
		if evento.type==KEYDOWN:
			if evento.key == K_ESCAPE:
				quit()
				exit()
			if evento.key == K_SPACE:
				if cut_scene_manager.cut_scene is not None:
					sound_texto.play()
			if evento.key == K_DOWN and mixer.music.get_volume() > 0.0:
				mixer.music.set_volume(mixer.music.get_volume() - 0.1)
			if evento.key == K_UP and mixer.music.get_volume() > 0.0:
				mixer.music.set_volume(mixer.music.get_volume() + 0.1)
