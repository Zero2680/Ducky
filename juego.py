from pygame import *
from random import*
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
		self.disparo1 = Disparo(self.x, 100, 20, 20, (255,0,0), 1, randrange(0,2), randrange(0,2))
		self.disparo2 = Disparo(self.x, 350, 20, 20, (255,0,0), 1, randrange(0,2), randrange(0,2))
		self.disparo3 = Disparo(self.x, 600, 20, 20, (255,0,0), 1, randrange(0,2), randrange(0,2))
		self.disparo4 = Disparo(0, 210, 20, 20, (255,0,0), 1, 1, randrange(0,2))
		self.disparo5 = Disparo(-140, 210, 20, 20, (255,0,0), 1, 1, randrange(0,2))
		self.disparo6 = Disparo(280, 210, 20, 20, (255,0,0), 1, 1, randrange(0,2))
		self.tentaculo1 = Disparo(plataforma.x-250, 0, 20, 720, (255,0,0), 1, 1, 0)
		self.tentaculo2 = Disparo(plataforma.x+250, 0, 20, 720, (255,0,0), 1, 1, 0)
	
	def Movimiento(self): #MOVIMIENTO TORTUGA CAPARAZON
		global boss_attack
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
	
	def Movimiento2(self): #MOVIMIENTO MEDUSA
		global boss_attack
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
	
	def Caparazones(self, enemigo):
		self.disparo1.Movimiento_Caparazon(enemigo)
		self.disparo2.Movimiento_Caparazon(enemigo)
		self.disparo3.Movimiento_Caparazon(enemigo)

	def Murcielagos(self):
		self.disparo1.Movimiento_Murcielago()
		self.disparo2.Movimiento_Murcielago()
		self.disparo3.Movimiento_Murcielago()
		self.disparo4.Movimiento_Murcielago()
		self.disparo5.Movimiento_Murcielago()
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

class Huevo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)

	def Movimiento1(self, plataforma):
		global x1, y1, x2, y2, x3, y3
		if Personaje.check_colisiones(self, enemigo) == True:
			enemigo.vidas -= 1
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
		if self.direccionx == 1:
			self.x += 1
		if self.direccionx == 0:
			self.x -= 1
		if self.direcciony == 1:
			self.y += 1
		if self.direcciony == 0:
			self.y -= 1
		#self.x -= 0.5
		plat += 1
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 720:
			self.direcciony = 0
		if self.x <= 0 and self.direccionx == 0:
			self.x = 1280
		if plat >= 720:
			if self.direccionx == 1:
				self.direccionx = 0
			elif self.direccionx == 0:
				self.direccionx = 1
			plat = 0

estanque = transform.scale(image.load("juego_images/fondo.jpg").convert(), (1280, 857))
fondo = estanque
plataforma = Personaje(50, 260, 20, 20,(255,255,255), 3, 1, 2)
pato01 = transform.scale(image.load("juego_images/pato01.png"), (50, 50))
pato11 = transform.scale(image.load("juego_images/pato11.png"), (50, 50))
pato02 = transform.scale(image.load("juego_images/pato02.png"), (50, 50))
pato12 = transform.scale(image.load("juego_images/pato12.png"), (50, 50))
enemigo = Boss(540, 210, 200, 200,(255,255,255), 1000, 1, 1)
tortuga1 = transform.scale(image.load("juego_images/tortuga1.png"), (300, 300))
tortuga2 = transform.scale(image.load("juego_images/tortuga2.png"), (300, 300))
caparazon_boss1 = transform.scale(image.load("juego_images/caparazon_boss1.png"), (300, 300))
caparazon_boss2 = transform.scale(image.load("juego_images/caparazon_boss2.png"), (300, 300))
caparazon1 = transform.scale(image.load("juego_images/caparazon1.png"), (50, 50))
caparazon2 = transform.scale(image.load("juego_images/caparazon2.png"), (50, 50))
cueva = transform.scale(image.load("juego_images/cueva.jpg").convert(), (1280, 720))
murcielago1 = transform.scale(image.load("juego_images/murcielago1.png"), (50, 50))
murcielago2 = transform.scale(image.load("juego_images/murcielago2.png"), (50, 50))
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
mono = transform.scale(image.load("juego_images/mono.png"), (300, 300))
platano = transform.scale(image.load("juego_images/platano.png"), (50, 50))
animacion_pato = 0
animacion_boss = 0
animacion_disparo = 0
x_boss = 65
y_boss = 65
level = 1
z = 0

while True:
	global x1, y1, x2, y2, x3, y3, boss_attack, y_medusa_aux, tent, plat
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
		plat = 0
		z = 1
	animacion_pato += 1
	animacion_boss += 1
	animacion_disparo += 1
	boss_attack += 1
	plataforma.Movimiento()
	if level == 1 and z == 1:
		boss1 = tortuga1
		boss2 = tortuga2
		next_boss1 = murcielago3
		next_boss2 = murcielago4
		disparo1 = caparazon1
		disparo2 = caparazon2
		z = 2
	if level == 2 and z == 2:
		fondo = cueva
		enemigo.x = 540
		enemigo.y = 50
		enemigo.disparo1.x = 1260
		enemigo.disparo2.x = 1400
		enemigo.disparo3.x = 1540
		enemigo.disparo1.direccionx = 0
		enemigo.disparo2.direccionx = 0
		enemigo.disparo3.direccionx = 0
		boss1 = murcielago3
		boss2 = murcielago4
		next_boss1 = medusa_boss1
		next_boss2 = medusa_boss2
		disparo1 = murcielago1
		disparo2 = murcielago2
		z = 3
	if level == 3 and z == 3:
		enemigo.ancho = 50
		enemigo.largo = 175
		x_boss = 125
		fondo = mar
		boss1 = medusa_boss1
		boss2 = medusa_boss2
		disparo1 = medusa1
		disparo2 = medusa2
		next_boss1 = mono
		next_boss2 = mono
		z = 4
	if level == 4 and z == 4:
		fondo = selva
		enemigo.x = 540
		enemigo.y = 50
		boss1 = mono
		boss2 = mono
		disparo1 = platano
		disparo2 = platano
		enemigo.disparo1.y = 0
		enemigo.disparo1.x = 640
		plat = enemigo.disparo1.x
		z = 5
	if enemigo.vidas <= 0:
		level = 2
	if level == 1:
		screen.blit(next_boss1, [0, 0])
		screen.blit(next_boss2, [0, 0])
	screen.blit(fondo, [0, 0])
	#NIVELES
	if level == 1:
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
	if level == 2:
		enemigo.Murcielagos()
	if level == 3:
		enemigo.Medusas()
		enemigo.Movimiento2()
		plataforma.DibujarObjeto()
		enemigo.DibujarObjeto()
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
		enemigo.Platanos()
	#ANIMACION HUEVO
	screen.blit(huevo, [plataforma.huevo1.x-20, plataforma.huevo1.y-20])
	screen.blit(huevo, [plataforma.huevo2.x-20, plataforma.huevo2.y-20])
	screen.blit(huevo, [plataforma.huevo3.x-20, plataforma.huevo3.y-20])
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
	#ANIMACION DISPARO
	if animacion_disparo <= 25:
		screen.blit(disparo1, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
	if animacion_disparo > 25:
		screen.blit(disparo2, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
		if animacion_disparo >= 50:
			animacion_disparo = 0
	if animacion_disparo <= 25:
		screen.blit(disparo1, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
	if animacion_disparo > 25:
		screen.blit(disparo2, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
		if animacion_disparo >= 50:
			animacion_disparo = 0
	if animacion_disparo <= 25:
		screen.blit(disparo1, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
	if animacion_disparo > 25:
		screen.blit(disparo2, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
		if animacion_disparo >= 50:
			animacion_disparo = 0
	if level == 2 or level == 3:
		if animacion_disparo <= 25:
			screen.blit(disparo1, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
		if animacion_disparo > 25:
			screen.blit(disparo2, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
			if animacion_disparo >= 50:
				animacion_disparo = 0
		if animacion_disparo <= 25:
			screen.blit(disparo1, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
		if animacion_disparo > 25:
			screen.blit(disparo2, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
			if animacion_disparo >= 50:
				animacion_disparo = 0
		if animacion_disparo <= 25:
			screen.blit(disparo1, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
		if animacion_disparo > 25:
			screen.blit(disparo2, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
			if animacion_disparo >= 50:
				animacion_disparo = 0
	#ANIMACION BOSS
	if boss_attack >= 1000:
		if animacion_boss <= 100:
			screen.blit(boss1, [enemigo.x-x_boss, enemigo.y-y_boss])
		if animacion_boss > 100:
			screen.blit(boss2, [enemigo.x-x_boss, enemigo.y-y_boss])
			if animacion_boss >= 200:
				animacion_boss = 0
	plataforma.Disparar(plataforma)
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
