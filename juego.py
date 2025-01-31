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
		self.DibujarObjeto()

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
		if Personaje.check_colisiones(self, plataforma) == True:
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
		global boss_attack
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
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
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
		if self.direcciony == 0:
			self.y -= 0.5
			if self.y == -200:
				pos = randrange(0,2)
				self.direcciony = 1
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
				self.direcciony = 2
			
	def Movimiento5(self): #MOVIMIENTO DEMONIO
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
		if self.direcciony == 0:
			self.y -= 0.5
			if self.y == -250 or self.x > 1280:
				self.x = 540
				self.y = -250
				self.direcciony = 1
		if self.direcciony == 1:
			self.y += 0.5
			if self.y == 260:
				self.direcciony = 2
	
	def Movimiento6(self, enemigo2, enemigo3): #MOVIMIENTOS DEMONIOS
		global e1, e2, e3
		if e1 == e2 or e1 == e3 or e2 == e3:
			e1 = randrange(0,2)
			e2 = randrange(0,2)
			e3 = randrange(0,2)
		else:
			if e1 == 0:
				self.x = 160
			elif e1 == 1:
				self.x = 540
			elif e1 == 2:
				self.x = 920
			if e2 == 0:
				enemigo2.x = 160
			elif e2 == 1:
				enemigo2.x = 540
			elif e2 == 2:
				enemigo2.x = 920
			if e3 == 0:
				enemigo3.x = 160
			elif e3 == 1:
				enemigo3.x = 540
			elif e3 == 2:
				enemigo3.x = 920

	def Caparazones(self, enemigo):
		self.disparo1.Movimiento_Caparazon(enemigo)
		self.disparo2.Movimiento_Caparazon(enemigo)
		self.disparo3.Movimiento_Caparazon(enemigo)

	def Murcielagos(self):
		self.disparo1.Movimiento_Murcielago()
		#self.disparo2.Movimiento_Murcielago()
		self.disparo3.Movimiento_Murcielago()
		self.disparo4.Movimiento_Murcielago()
		#self.disparo5.Movimiento_Murcielago()
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
		global x1, y1, x2, y2, x3, y3
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
				y1 = 0
		elif plataforma.direcciony == 0:
			y1 += 2
			self.y = plataforma.y + y1
			self.x = plataforma.x
			if (y1 == 100):
				self.y = plataforma.y
				y1 = 0
		else:
			if plataforma.direccionx == 1:
				x1 += 2
				self.x = plataforma.x + x1
				self.y = plataforma.y
				if (x1 == 100):
					self.x = plataforma.x
					x1 = 0
			if plataforma.direccionx == 0:
				x1 += 2
				self.x = plataforma.x - x1
				self.y = plataforma.y
				if (x1 == 100):
					self.x = plataforma.x
					x1 = 0

	def Movimiento2(self, plataforma):
		global x1, y1, x2, y2, x3, y3
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
		global x1, y1, x2, y2, x3, y3
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
		self.DibujarObjeto()
	
	def Movimiento_Murcielago(self):
		if Personaje.check_colisiones(self, plataforma) == True:
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
		global tent
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
		if self.y < 1300 and tent != 2:
			if self.direccionx == 1:
				self.x += 1
			if self.direccionx == 0:
				self.x -= 1
		if self.x > 1280 or self.x < 0:
			tent = 2
		self.DibujarObjeto()
	
	def Movimiento_Platano(self): #GIROS
		global plat
		if Personaje.check_colisiones(self, plataforma) == True:
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
		#self.x -= 0.5
		self.vidas += 1
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 720:
			self.direcciony = 0
		'''if self.x <= 0 and self.direccionx == 0:
			self.x = 1280'''
		if self.vidas == 360 or self.vidas == 1080:
			if self.direccionx == 1:
				self.direccionx = 0
			elif self.direccionx == 0:
				self.direccionx = 1
		if self.vidas == 1440:
			self.vidas = 0
			if self.x >= 1500:
				self.x -= 1500

estanque = transform.scale(image.load("juego_images/fondo.jpg").convert(), (1280, 857))
plataforma = Personaje(625, 350, 20, 20,(255,255,255), 30000, 1, 2)
pato01 = transform.scale(image.load("juego_images/pato01.png"), (50, 50))
pato11 = transform.scale(image.load("juego_images/pato11.png"), (50, 50))
pato02 = transform.scale(image.load("juego_images/pato02.png"), (50, 50))
pato12 = transform.scale(image.load("juego_images/pato12.png"), (50, 50))
corazon1 = transform.scale(image.load("juego_images/corazon1.png"), (40, 40))
corazon2 = transform.scale(image.load("juego_images/corazon2.png"), (40, 40))
enemigo = Boss(540, 210, 200, 200,(255,255,255), 1000, 1, 1)
enemigo2 = Boss(160, -250, 200, 200,(255,255,255), 250, 1, 0)
enemigo3 = Boss(920, -250, 200, 200,(255,255,255), 250, 1, 0)
tortuga1 = transform.scale(image.load("juego_images/tortuga1.png"), (300, 300))
tortuga2 = transform.scale(image.load("juego_images/tortuga2.png"), (300, 300))
caparazon_boss1 = transform.scale(image.load("juego_images/caparazon_boss1.png"), (300, 300))
caparazon_boss2 = transform.scale(image.load("juego_images/caparazon_boss2.png"), (300, 300))
caparazon1 = transform.scale(image.load("juego_images/caparazon1.png"), (50, 50))
caparazon2 = transform.scale(image.load("juego_images/caparazon2.png"), (50, 50))
cueva = transform.scale(image.load("juego_images/cueva.jpg").convert(), (1280, 720))
murcielago1 = transform.scale(image.load("juego_images/murcielago1.png"), (50, 50))
murcielago2 = transform.scale(image.load("juego_images/murcielago2.png"), (50, 50))
murcielago1_boss = transform.scale(image.load("juego_images/murcielago1.png"), (300, 300))
murcielago2_boss = transform.scale(image.load("juego_images/murcielago2.png"), (300, 300))
murcielago3 = transform.scale(image.load("juego_images/murcielago3.png"), (300, 300))
murcielago4 = transform.scale(image.load("juego_images/murcielago4.png"), (300, 300))
huevo = transform.scale(image.load("juego_images/huevo.png"), (50, 50))
mar = transform.scale(image.load("juego_images/mar.jpg").convert(), (1280, 720))
medusa_boss1 = transform.scale(image.load("juego_images/medusa_boss1.png"), (300, 300))
medusa_boss2 = transform.scale(image.load("juego_images/medusa_boss2.png"), (300, 300))
medusa1 = transform.scale(image.load("juego_images/medusa1.png"), (50, 50))
medusa2 = transform.scale(image.load("juego_images/medusa2.png"), (50, 50))
medusa3 = transform.scale(image.load("juego_images/medusa3.png"), (50, 50))
selva = transform.scale(image.load("juego_images/selva.jpg").convert(), (1280, 720))
mono1 = transform.scale(image.load("juego_images/liana1.png"), (300, 300))
mono2 = transform.scale(image.load("juego_images/liana2.png"), (300, 300))
platano = transform.scale(image.load("juego_images/banana.png"), (50, 50))
mazmorra = transform.scale(image.load("juego_images/mazmorra2.jpg").convert(), (1280, 720))
penguin = transform.scale(image.load("juego_images/demonio.png"), (300, 300))
demon = transform.scale(image.load("juego_images/demon2.png"), (300, 300))
platanop = transform.scale(image.load("juego_images/bananap.png"), (50, 50))
caparazon1p = transform.scale(image.load("juego_images/caparazon1p.png"), (50, 50))
caparazon2p = transform.scale(image.load("juego_images/caparazon2p.png"), (50, 50))
medusa1p = transform.scale(image.load("juego_images/medusa1p.png"), (50, 50))
medusa2p = transform.scale(image.load("juego_images/medusa2p.png"), (50, 50))
medusa3p = transform.scale(image.load("juego_images/medusa3p.png"), (50, 50))
murcielago1p = transform.scale(image.load("juego_images/murcielago1p.png"), (50, 50))
murcielago2p = transform.scale(image.load("juego_images/murcielago2p.png"), (50, 50))
disparo1_1 = caparazon1p
disparo1_2 = caparazon2p
disparo2_1 = medusa1p
disparo2_2 = medusa2p
disparo3_1 = murcielago1p
disparo3_2 = murcielago2p
disparo4 = platanop
animacion_pato = 0
animacion_boss = 0
animacion_disparo = 0
animacion_corazon = 0
x_boss = 65
y_boss = 65
level = 1
z = 0
cut_scene_manager = CutSceneManager(screen)

while True:
	global x1, y1, x2, y2, x3, y3, boss_attack, y_medusa_aux, tent, e1, e2, e3
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
		e1 = 0
		e2 = 0
		e3 = 0
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
		enemigo.x = 540
		enemigo.y = 50
		enemigo.largo = 200
		enemigo.direcciony = 0
		boss1 = mono1
		boss2 = mono2
		disparo1 = platano
		disparo2 = platano
		next_boss1 = tortuga1
		next_boss2 = tortuga2
		cut_scene_manager.start_cut_scene(CutSceneOneStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 2
	if level == 2 and z == 2:
		plataforma.x = 50
		plataforma.y = 260
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
		cut_scene_manager.start_cut_scene(CutSceneTwoStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			boss_attack = 0
			z = 3
	if level == 3 and z == 3:
		enemigo.ancho = 50
		enemigo.largo = 175
		x_boss = 125
		enemigo.disparo4.direcciony = randrange(0,2)
		enemigo.disparo5.direcciony = randrange(0,2)
		enemigo.disparo6.direcciony = randrange(0,2)
		fondo = mar
		boss1 = medusa_boss1
		boss2 = medusa_boss2
		disparo1 = medusa1
		disparo2 = medusa2
		next_boss1 = murcielago3
		next_boss2 = murcielago4
		cut_scene_manager.start_cut_scene(CutSceneThreeStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 4
	if level == 4 and z == 4:
		fondo = cueva
		enemigo.x = 540
		enemigo.y = 50
		enemigo.ancho = 160
		x_boss = 65
		enemigo.direccionx = 0
		enemigo.direcciony = 1
		enemigo.disparo1.x = 1260
		enemigo.disparo2.x = 1400
		enemigo.disparo3.x = 1540
		enemigo.disparo1.direccionx = 0
		enemigo.disparo2.direccionx = 0
		enemigo.disparo3.direccionx = 0
		boss1 = murcielago3
		boss2 = murcielago4
		next_boss1 = penguin
		next_boss2 = penguin
		disparo1 = murcielago1
		disparo2 = murcielago2
		enemigo.disparo2.x = -100
		enemigo.disparo5.x = -100
		cut_scene_manager.start_cut_scene(CutSceneFourStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			boss_attack = 0
			z = 5
	if level == 5 and z == 5:
		fondo = mazmorra
		boss1 = penguin
		boss2 = penguin
		cut_scene_manager.start_cut_scene(CutSceneFiveStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 6
	if z > 0:
		screen.blit(next_boss1, [0, 0])
		screen.blit(next_boss2, [0, 0])
		screen.blit(fondo, [0, 0])
	else:
		screen.fill((0,0,0))
	#NIVELES
	if cut_scene_manager.cut_scene is None:
		if level == 1:
			enemigo.Platanos()
			if enemigo.vidas <= 800:
				enemigo.Movimiento4()
		if level == 2:
			if boss_attack >= 3000:
				boss_attack = 0
			if boss_attack < 1000:
				if boss_attack > 100:
					enemigo.Movimiento()
				if animacion_boss <= 100:
					screen.blit(caparazon_boss1, [enemigo.x-65, enemigo.y-65])
				if animacion_boss > 100:
					screen.blit(caparazon_boss2, [enemigo.x-65, enemigo.y-65])
					if animacion_boss >= 200:
						animacion_boss = 0
			enemigo.Caparazones(enemigo)
		if level == 3:
			enemigo.Medusas()
			enemigo.Movimiento3()
			animacion_boss -= 0.5
			animacion_disparo -= 1
			if enemigo.vidas <= 800:
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
				enemigo.Tentaculos()
			if y_medusa_aux < 600:
				animacion_disparo = 30
			elif y_medusa_aux >= 600:
				animacion_disparo = 0
		if level == 4:
			enemigo.Murcielagos()
			if boss_attack < 2000:
				enemigo.Movimiento2()
				enemigo.largo = 150
				if animacion_boss <= 100:
					screen.blit(murcielago1_boss, [enemigo.x-65, enemigo.y-65])
				if animacion_boss > 100:
					screen.blit(murcielago2_boss, [enemigo.x-65, enemigo.y-65])
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
		if level == 5:
			#enemigo.DibujarObjeto()
			if 4000 < enemigo.vidas <= 4900:
				if enemigo.y != 260 and enemigo.direcciony == 2:
					enemigo.y += 0.5
				enemigo.Movimiento4()
				enemigo.Platanos()
			if enemigo.vidas <= 4000:
				if z == 6:
					enemigo.direcciony = 0
					z = 7
				enemigo.disparo9.Movimiento_Platano()
				enemigo.disparo10.Movimiento_Platano()
				enemigo.disparo11.Movimiento_Platano()
				enemigo.disparo12.Movimiento_Platano()
				if enemigo.vidas > 3900:
					enemigo.Movimiento5()
			if 3000 < enemigo.vidas <= 3900:
				if z == 7:
					enemigo.direcciony = 1
					boss_attack = 0
					z = 8
				if boss_attack >= 3000:
					boss_attack = 0
				if boss_attack < 1000:
					if boss_attack > 100:
						enemigo.Movimiento()
				enemigo.Caparazones(enemigo)
			if enemigo.vidas <= 3000:
				if z == 8:
					enemigo.direcciony = 0
					z = 9
				enemigo.disparo1.Movimiento_Caparazon(enemigo)
				enemigo.disparo2.Movimiento_Caparazon(enemigo)
				if enemigo.vidas > 2900:
					enemigo.Movimiento5()
			if 2000 < enemigo.vidas <= 2900:
				if z == 9:
					enemigo.direcciony = 1
					z = 10
				enemigo.disparo3.Movimiento_Medusa()
				enemigo.disparo4.Movimiento_Medusa()
				enemigo.disparo5.Movimiento_Medusa()
				enemigo.Movimiento3()
				animacion_boss -= 0.5
				animacion_disparo -= 1
				if enemigo.vidas <= 800:
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
					enemigo.Tentaculos()
				if y_medusa_aux < 600:
					animacion_disparo = 30
				elif y_medusa_aux >= 600:
					animacion_disparo = 0
			if enemigo.vidas <= 2000:
				if z == 9:
					enemigo.direcciony = 0
					z = 10
				enemigo.disparo3.Movimiento_Medusa()
				enemigo.disparo4.Movimiento_Medusa()
				enemigo.disparo5.Movimiento_Medusa()
				if enemigo.vidas > 1900:
					enemigo.Movimiento5()
			if 1000 < enemigo.vidas <= 1900:
				if z == 10:
					enemigo.direcciony = 0
					z = 11
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
			if enemigo.vidas <= 1000:
				if z == 11:
					enemigo.direcciony = 0
					z = 12
				enemigo.disparo6.Movimiento_Murcielago()
				enemigo.disparo7.Movimiento_Murcielago()
				enemigo.disparo8.Movimiento_Murcielago()
				if enemigo.vidas > 900:
					enemigo.Movimiento5()
					if z == 12:
						enemigo2.y = enemigo.y
						enemigo3.y = enemigo.y
					if enemigo.y <= -200:
						z = 13
			if 0 < enemigo.vidas <= 900:
				if z == 13:
					boss_attack = 0
					enemigo.direcciony = 0
					z = 14
				if boss_attack >= 3000:
					boss_attack = 0
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
					if z == 15:
						enemigo2.x = 160
						enemigo3.x = 920
						enemigo2.y = enemigo.y
						enemigo3.y = enemigo.y
						if enemigo.y == 540:
							enemigo2.vidas = 500
							enemigo3.vidas = 500
					if enemigo.y <= -200:
						z = 15
			if 4000 < enemigo.vidas <= 4900:
				disparo1_1 = disparo4
				disparo1_2 = disparo4
				disparo2_1 = disparo4
				disparo2_2 = disparo4
				disparo3_1 = disparo4
				disparo3_2 = disparo4
			if 3000 < enemigo.vidas <= 3900:
				disparo1_1 = caparazon1p
				disparo1_2 = caparazon2p
			if 2000 < enemigo.vidas <= 2900:
				disparo2_1 = medusa1p
				disparo2_2 = medusa2p
			if 1000 < enemigo.vidas <= 1900:
				disparo3_1 = murcielago1p
				disparo3_2 = murcielago2p
			if enemigo.vidas <= 4900:
				screen.blit(disparo4, [enemigo.disparo9.x-15, enemigo.disparo9.y-15])
				screen.blit(disparo4, [enemigo.disparo10.x-15, enemigo.disparo10.y-15])
				screen.blit(disparo4, [enemigo.disparo11.x-15, enemigo.disparo11.y-15])
				screen.blit(disparo4, [enemigo.disparo12.x-15, enemigo.disparo12.y-15])
			if (4000 < enemigo.vidas <= 4900) or (enemigo.vidas <= 3900):
				if animacion_disparo <= 25:
					screen.blit(disparo1_1, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
					screen.blit(disparo1_1, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
					if enemigo.vidas > 3000:
						screen.blit(disparo1_1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo1_2, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
					screen.blit(disparo1_2, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
					if enemigo.vidas > 3000:
						screen.blit(disparo1_2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
			if (4000 < enemigo.vidas <= 4900) or (enemigo.vidas <= 2900):
				if animacion_disparo <= 25:
					screen.blit(disparo2_1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
					screen.blit(disparo2_1, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
					screen.blit(disparo2_1, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo2_2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
					screen.blit(disparo2_2, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
					screen.blit(disparo2_2, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
			if (4000 < enemigo.vidas <= 4900) or (enemigo.vidas <= 1900):
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
					screen.blit(disparo1, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo2, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
				if animacion_disparo <= 25:
					screen.blit(disparo1, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo2, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
				if animacion_disparo <= 25:
					screen.blit(disparo1, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
				if animacion_disparo > 25:
					screen.blit(disparo2, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
			if level == 1 or level == 5:
				if level == 1 or (level == 5 and 4000 < enemigo.vidas <= 4900):
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
		if (level != 2 and level != 4) or (boss_attack >= 1000 and level == 2) or (boss_attack >= 2000 and level == 4):
			if animacion_boss <= 100:
				screen.blit(boss1, [enemigo.x-x_boss, enemigo.y-y_boss])
			if animacion_boss > 100:
				screen.blit(boss2, [enemigo.x-x_boss, enemigo.y-y_boss])
				if animacion_boss >= 200:
					animacion_boss = 0
		if level == 5:
			if enemigo2.vidas > 0 or z == 15:
				screen.blit(demon, [enemigo2.x-x_boss, enemigo2.y-y_boss])
			if enemigo3.vidas > 0 or z == 15:
				screen.blit(demon, [enemigo3.x-x_boss, enemigo2.y-y_boss])
	#CUT_SCENE
	if enemigo.vidas <= 0:
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
			plataforma.direccionx = 1
			enemigo.x = 540
			enemigo.y = 50
			cut_scene_manager.start_cut_scene(CutSceneFiveFinal(plataforma))
		if cut_scene_manager.cut_scene is None:
			enemigo.vidas = 1000
			level += 1
	cut_scene_manager.update()
	cut_scene_manager.draw()
	display.flip()
	if plataforma.vidas <= 0:
		quit()
		exit()
	for evento in event.get():
		if evento.type==QUIT:
				quit()
				exit()
		if evento.type==KEYDOWN:
			if evento.key == K_ESCAPE:
				quit()
				exit()
			if evento.key == K_DOWN:
				level = 2
			if evento.key == K_UP:
				level = 3
			if evento.key == K_LEFT:
				level = 4
			if evento.key == K_RIGHT:
				fondo = mazmorra
				x_boss = 50
				y_boss = 50
				enemigo.x = 540
				enemigo.y = 260
				enemigo.direcciony = 0
				enemigo.ancho = 200
				enemigo.largo = 200
				enemigo.vidas = 5000
				boss1 = penguin
				boss2 = penguin
				disparo4 = platanop
				level = 5
				z = 6
