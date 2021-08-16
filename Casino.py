from wx import *
import random
from wx.adv import Animation, AnimationCtrl

## -- difficulty selector + name -- ##

class MyApp(App):
    def OnInit(self):
        self.fontr = Font(pointSize = 15, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.ph = []
        self.dh = []
        self.starting = Frame(None, -1, 'Starting....')
        p = Panel(self.starting)
        imgFondo = Image('img/inicioPlantilla.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        fondoBitmap = StaticBitmap(p,-1,imgFondo)
        dif1 = Image('img/750 c.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        dif1b = BitmapButton(fondoBitmap, 1, dif1,size = (dif1.GetWidth(), dif1.GetHeight()))
        dif1b.Bind(EVT_BUTTON, self.setCoins)
        dif2 = Image('img/500 c.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        dif2b = BitmapButton(fondoBitmap, 2, dif2,size = (dif2.GetWidth(), dif2.GetHeight()))
        dif2b.Bind(EVT_BUTTON, self.setCoins)
        dif3 = Image('img/250 c.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        dif3b = BitmapButton(fondoBitmap, 3, dif3, size = (dif3.GetWidth(), dif3.GetHeight()))
        dif3b.Bind(EVT_BUTTON, self.setCoins)
        dif1b.SetPosition((874,524))
        dif2b.SetPosition((500,524))
        dif3b.SetPosition((110,524))
        self.name = TextCtrl(fondoBitmap, -1,size= Size(394, 22), style = BORDER_NONE, value = 'Player')
        self.name.SetFont(self.fontr)
        self.name.SetPosition((464,368))
        self.starting.SetDimensions(0,0,1280,720)
        self.starting.Show()
        self.starting.SetPosition((320,180))
        return True

    def setCoins(self,event):
        id = event.GetId()
        if id == 1:
            self.coinsInicio = 750
        elif id == 2:
            self.coinsInicio = 500
        elif id == 3:
            self.coinsInicio = 250
        self.panelPrincipal()

## -- Main Background + Game Selector -- ##

    def panelPrincipal(self):
        self.starting.Hide()
        self.mainBackground = Frame(None, 1, 'Casino')
        p = Panel(self.mainBackground)
        self.mainBackground.SetDimensions(0, 0, 1920, 1080)
        backgroundGames = Image('img/BackgroundMain.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        bitmap = StaticBitmap(p,-1, backgroundGames)
        atras = Image('img/atras.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonAtras = BitmapButton(bitmap, 1, atras,size = (atras.GetWidth(), atras.GetHeight()))
        botonAtras.Bind(EVT_BUTTON, self.atras)
        botonAtras.SetPosition((70, 870))
        jugarC = Image('img/jugar.jpg',BITMAP_TYPE_ANY).ConvertToBitmap() 
        botonJugarC = BitmapButton(bitmap, -1, jugarC,size = (jugarC.GetWidth(), jugarC.GetHeight()))
        botonJugarC.Bind(EVT_BUTTON, self.coinflip) 
        botonJugarC.SetPosition((1000, 465))
        reglas = Image('img/reglas.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        botonReglas = BitmapButton(bitmap, -1, reglas,size =  (reglas.GetWidth(), reglas.GetHeight()))
        botonReglas.Bind(EVT_BUTTON, self.reglasC)
        botonReglas.SetPosition((1000, 600))
        reglasB = Image('img/reglas.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        botonReglasB = BitmapButton(bitmap, -1, reglasB,size =  (reglasB.GetWidth(), reglasB.GetHeight()))
        botonReglasB.Bind(EVT_BUTTON, self.reglasB)
        botonReglasB.SetPosition((1610, 497))
        jugarB = Image('img/jugar.jpg',BITMAP_TYPE_ANY).ConvertToBitmap() 
        botonJugarB = BitmapButton(bitmap, -1, jugarB,size = (jugarB.GetWidth(), jugarB.GetHeight()))
        botonJugarB.Bind(EVT_BUTTON, self.blackjack) 
        botonJugarB.SetPosition((1367, 497))
        refresh = Image('img/refresh.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        refreshB = BitmapButton(bitmap,-1, refresh)
        refreshB.Bind(EVT_BUTTON, self.refresh)
        self.coinsView = StaticText(p,-1, label = (str(self.coinsInicio)))
        self.coinsView.SetPosition((1450, 933))
        self.font = Font(pointSize = 45, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.coinsView.SetFont(self.font)
        self.coinsView.SetBackgroundColour('white')
        self.coinsView.SetForegroundColour('black')
        refreshB.SetPosition((1800,780))
        nameMain = StaticText(p,-1,label = (self.name.GetValue()))
        nameMain.SetPosition((1550, 847))
        nameMain.SetFont(self.font)
        nameMain.SetBackgroundColour((234,182,18))
        self.mainBackground.Show()
        self.mainBackground.ShowFullScreen(True)
        return True
    
    def refresh(self,event):
        print('refresh coins actuales')
        return self.coinsView.SetLabel(str(self.coinsInicio))

    def reglasC(self,event):
        print('reglas')
        reglasCoinflip = Frame(None, -1)
        p = Panel(reglasCoinflip)
        s = BoxSizer(VERTICAL)
        st1 = StaticText(p, -1, 'A gambling / betting game based around the flip of a coin.')
        s.Add(st1, 0 ,ALL|EXPAND,10)
        p.SetSizer(s)
        reglasCoinflip.Show()
        return True

    def reglasB(self,event):
        print('reglas')
        reglasBlackjackFrame = Frame(None, -1)
        reglasBlackjackFrame.SetDimensions(0, 0,700,500)
        p = Panel(reglasBlackjackFrame)
        s = BoxSizer(VERTICAL)
        reglasBlackjack = ('Valor de las cartas El As puede valer 1 punto u 11 puntos según el deseo de combinarlo '
            'con la otra carta de la mano.\n'
            'No hay que olvidar que la máxima '
            'puntuación ganadora es de 21 puntos.\n'
            'Los números del 2 al 10, equivalen a su propio valor.'
            'Por ejemplo si tiene dos cartas de 8, '
            'la mano tiene valor de 16 puntos.\n'
            'Cartas con figuras (Jota, Dama, Rey) valen cada una 10 puntos.')
        st1 = StaticText(p, -1, reglasBlackjack)                                                                 
        s.Add(st1, 0 ,ALL|EXPAND,10)
        p.SetSizer(s)
        reglasBlackjackFrame.Show()
        return True

## -- Coinflip -- ##

    def coinflip(self,event):
        self.mainBackground.Hide()
        self.coinflipMain = Frame(None, -1)
        p = Panel(self.coinflipMain)
        self.coinflipMain.SetDimensions(0, 0, 1920, 1080)
        fondoCoinflip = Image('img/plantillaFondo.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmapC = StaticBitmap(p, -1, fondoCoinflip)
        atras = Image('img/atrasc.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonAtras = BitmapButton(self.bitmapC, 10, atras,size =  (atras.GetWidth(), atras.GetHeight()))
        botonAtras.Bind(EVT_BUTTON, self.atras)
        botonAtras.SetPosition((70, 870))
        self.coinsActuales = str(self.coinsInicio)
        self.coinsCoinflip = StaticText(self.bitmapC, -1, self.coinsActuales, size = Size(350, 50))
        self.betC = TextCtrl(self.bitmapC,-1,size= Size(250, 80), style = BORDER_NONE, value = '0')
        bmpCara = Image('img/cara.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonCara = BitmapButton(self.bitmapC ,11 ,bmpCara,size =  (bmpCara.GetWidth(), bmpCara.GetHeight())) 
        botonCara.Bind(EVT_BUTTON, self.coc)
        botonCara.SetPosition((1549, 438))
        bmpCruz = Image('img/cruz.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonCruz = BitmapButton(self.bitmapC, 12, bmpCruz, size =  (bmpCruz.GetWidth(), bmpCruz.GetHeight()))
        botonCruz.Bind(EVT_BUTTON, self.coc)
        botonCruz.SetPosition((1232, 438))
        bmpStart = Image('img/empezar.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonStart = BitmapButton(self.bitmapC, -1, bmpStart, size =  (bmpStart.GetWidth(), bmpStart.GetHeight()))
        botonStart.Bind(EVT_BUTTON, self.start)
        botonStart.SetPosition((1241, 588))
        self.coinsCoinflip.SetForegroundColour((250,210,0))
        self.font = Font(pointSize = 45, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.coinsCoinflip.SetFont(self.font)
        self.coinsCoinflip.SetBackgroundColour((91,22,103))
        self.coinsCoinflip.SetPosition((1355,57))
        self.betC.SetPosition((1350, 315))
        self.betC.SetForegroundColour('black')
        self.betC.SetBackgroundColour((79,0,102))
        self.betC.SetFont(self.font)
        self.coinflipMain.Show()
        self.coinflipMain.ShowFullScreen(True)
        ImgCara = Image('img/CARABASE.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        caraP = StaticBitmap(self.bitmapC,-1, ImgCara)
        caraP.SetPosition((100,100))
        return True
    
    def coc (self, event):
        self.coc = int
        id = event.GetId()
        if id == 11:
            self.coc = 1
            print('cara')
        if id == 12:
            self.coc = 2
            print('Cruz')
        return self.coc
        
    def start (self,event):
        self.fontResultado = Font(pointSize = 50, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.result = StaticText(self.bitmapC, -1, ' ')
        self.result.SetFont(self.fontResultado)
        self.result.SetBackgroundColour((146,0,75))
        self.result.SetForegroundColour('black')
        self.result.SetPosition((350,875))
        if self.validador(self.betC.Value) == True:
            print('go')
            print(f'Valor de self.bet {self.betC.Value}')
            print(f'Self.betGetValue :{self.betC.GetValue()}0000')
            x = random.randint(1,2)
            print(x)
            apuesta = int(self.betC.GetValue())
            if x == 1:
                if x == self.coc:
                    self.coinsInicio = self.coinsInicio + apuesta
                    print(f'Ganaste {apuesta}')
                    self.result.SetLabel(f'Ganaste! {apuesta} coins, ahora tienes un total de {self.coinsInicio} coins!')
                    self.betC.SetValue('0')
                else:
                    self.coinsInicio = self.coinsInicio - apuesta
                    print(f'Perdiste {apuesta}')
                    self.result.SetLabel(f'Perdiste! {apuesta} coins, ahora tienes un total de {self.coinsInicio} coins!')
                    self.betC.SetValue('0')
                anim = Animation('Cara-G.gif')
                self.ctrl = AnimationCtrl(self.bitmapC, -1, anim)
                self.ctrl.SetPosition((100,100))
                self.ctrl.Play()
                self.coinsCoinflip.SetLabel(str(self.coinsInicio))
            else:
                if x == self.coc:
                    self.coinsInicio = self.coinsInicio + apuesta
                    print(f'Ganaste {apuesta}')
                    self.result.SetLabel(f'Ganaste! {apuesta} coins, ahora tienes un total de {self.coinsInicio} coins')
                    self.betC.SetValue('0')
                else:
                    self.coinsInicio = self.coinsInicio - apuesta
                    print(f'Perdiste {apuesta}')
                    self.result.SetLabel(f'Perdiste! {apuesta} coins, ahora tienes un total de {self.coinsInicio} coins!')
                    self.betC.SetValue('0')
                anim = Animation('Cruz-G.gif')
                self.ctrl = AnimationCtrl(self.bitmapC, -1, anim)
                self.ctrl.SetPosition((100, 100))
                self.ctrl.Play()
                self.coinsCoinflip.SetLabel(str(self.coinsInicio))

## -- Stuff -- ##

    def atras(self,event):
        print("Atras")
        id = event.GetId()
        if id == 1:
            self.mainBackground.Destroy()
        elif id == 10:
            self.coinflipMain.Hide()
            self.mainBackground.Show()
        elif id == 20:
            self.mesasBlackjack.Destroy()
        elif id == 25:
            self.blackjackMain.Destroy()


    def validador(self,check):
        checkC = (self.betC.GetValue())
        cadenaDeCaracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','v','x','y','z']
        if checkC in cadenaDeCaracteres:
            print('Error de validacion.')
            self.result.SetLabel(f'Porfavor introduzca un valor numerico')
            return False
        else:
            checkI = int(self.betC.GetValue())
            if checkI <= self.coinsInicio:
                print('pass')
                return True
            else:
                print('Error de validacion.')
                self.result.SetLabel(f'No cuentas con las coins suficientes')
                return False

## -- Blackjack -- ##

    def blackjack(self,event):
        fontResultado = Font(pointSize = 30, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.mesasBlackjack = Frame(None, 21, 'Blackjack')
        self.p1 = Panel(self.mesasBlackjack)
        imgFondo2 = Image ('img/PlantillaFondoA.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        fondo = StaticBitmap(self.p1,-1,imgFondo2)
        atras = Image('img/atrasa.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        botonAtras = BitmapButton(fondo, 20, atras,size =  (atras.GetWidth(), atras.GetHeight()))
        botonAtras.Bind(EVT_BUTTON, self.atras)
        botonAtras.SetPosition((70, 870))
        self.mazos = TextCtrl(fondo, -1, value = '1',size=Size(200,65))
        ficha10 = Image("img/ficha10.png",BITMAP_TYPE_ANY).ConvertToBitmap()
        ficha10Button = BitmapButton(fondo, 21, ficha10,size =  (ficha10.GetWidth(), ficha10.GetHeight()))
        ficha10Button.Bind(EVT_BUTTON, self.entrada)
        ficha10Button.SetPosition((83,236))
        ficha20 = Image('img/ficha20.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        ficha20Button = BitmapButton(fondo, 22, ficha20, size =  (ficha20.GetWidth(), ficha20.GetHeight()))
        ficha20Button.Bind(EVT_BUTTON, self.entrada)
        ficha20Button.SetPosition((265,534))
        ficha30 = Image('img/ficha30.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        ficha30Button = BitmapButton(fondo, 23,ficha30,size =  (ficha30.GetWidth(), ficha30.GetHeight()))
        ficha30Button.Bind(EVT_BUTTON, self.entrada)
        ficha30Button.SetPosition((999,534))
        ficha40 = Image('img/ficha40.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        ficha40Button = BitmapButton(fondo,24,ficha40,size =  (ficha40.GetWidth(), ficha40.GetHeight()))
        ficha40Button.Bind(EVT_BUTTON,self.entrada)
        ficha40Button.SetPosition((1269,236))  
        self.coinsViewB = StaticText(fondo,-1, label = (str(self.coinsInicio)))
        self.coinsViewB.SetPosition((1335, 920))
        self.coinsViewB.SetFont(self.font)
        self.coinsViewB.SetForegroundColour('black')
        self.mesasBlackjack.SetDimensions(0,0,1920, 1080)
        self.mesasBlackjack.ShowFullScreen(True)
        self.coinsViewB.SetBackgroundColour ('white')
        self.mazos.SetPosition((834,813))
        self.mazos.SetFont(fontResultado)
        anim = Animation('load.gif')
        self.ctrl = AnimationCtrl(fondo, -1, anim)
        self.ctrl.SetPosition((704,-100))
        self.ctrl.Play()
        self.mesasBlackjack.Show()
        return True
    
    def entrada(self,event):
        self.apuestaB = 0
        id = event.GetId()
        if id == 21:
            self.apuestaB = 10
        elif id == 22:
            self.apuestaB = 20
        elif id == 23:
            self.apuestaB = 30
        elif id ==24:
            self.apuestaB = 40
        print(f'Set bet to : {self.apuestaB}')
        self.newstart()
        return self.apuestaB

    def validadorB(self,event):
        if self.apuestaB <= self.coinsInicio:
            print('pass')
            self.newstart()
            return True
        else:
            print('Error de validacion.')
            validacion = StaticText(self.p1, -1, (f'No cuentas con las coins suficientes, tienes '))
            validacion.SetFont(self.fontResultado)
            validacion.SetForegroundColour('black')
            validacion.SetPosition((260,933))
            return False
    
    def newstart (self):
        plantilaFondo = Image('img/PlantillaFondoB.jpg',BITMAP_TYPE_ANY).ConvertToBitmap()
        self.fontr = Font(pointSize = 15, family = FONTFAMILY_ROMAN, style = FONTSTYLE_MAX, weight = FONTWEIGHT_LIGHT)
        self.blackjackMain = Frame(None, -1, 'Blackjack')
        self.p8 = Panel(self.blackjackMain)
        atras = Image('img/atrasb.jpg', BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmapB = StaticBitmap(self.p8, -1, plantilaFondo)
        botonAtras = BitmapButton(self.bitmapB, 25, atras,size =  (atras.GetWidth(), atras.GetHeight()))
        botonAtras.Bind(EVT_BUTTON, self.atras)
        botonAtras.SetPosition((70, 870))
        for g in range(len(self.ph)):
            self.descarte(self.contents)
        for z in range(len(self.dh)):
            self.descarte(self.contents)
        self.ndeck()
        random.shuffle(self.contents)
        self.ph.append(self.contents.pop(0))
        self.dh.append(self.contents.pop(0))
        self.ph.append(self.contents.pop(0))
        self.dh.append(self.contents.pop(0))
        print(f'Player hand {self.ph}')
        print(f'Dealer hand {self.dh}')
        hit = Image('img/hit.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        buttonHit = BitmapButton(self.bitmapB, -1, hit,size =  (hit.GetWidth(), hit.GetHeight()))
        buttonHit.Bind(EVT_BUTTON, self.hit)
        buttonHit.SetPosition((30,355))
        stand = Image('img/stand.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        buttonStand = BitmapButton(self.bitmapB, -1, stand,size =  (stand.GetWidth(), stand.GetHeight()))
        buttonStand.Bind(EVT_BUTTON, self.stand)
        buttonStand.SetPosition((30,628))
        double = Image('img/double.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        buttonDouble = BitmapButton(self.bitmapB,-1,double, size =  (double.GetWidth(), double.GetHeight()))
        buttonDouble.Bind(EVT_BUTTON, self.double)
        buttonDouble.SetPosition((245,255))
        newHand = Image('img/newHand.png',BITMAP_TYPE_ANY).ConvertToBitmap()
        buttonNewHand = BitmapButton(self.bitmapB,-1,newHand,size =  (newHand.GetWidth(), newHand.GetHeight()))
        buttonNewHand.Bind(EVT_BUTTON, self.newHand)
        buttonNewHand.SetPosition((245,498))
        self.coinsViewB = StaticText(self.bitmapB,-1, label = (str(self.coinsInicio)))
        self.coinsViewB.SetPosition((1380, 950))
        self.coinsViewB.SetFont(self.font)
        self.coinsViewB.SetBackgroundColour('white')
        self.coinsViewB.SetForegroundColour('black')
        self.bitmapCreator(1)
        self.bitmapCreator(0)
        self.Calcular(1)
        self.Calcular(2)
        self.blackjackMain.SetDimensions(0,0,1920, 1080)
        self.blackjackMain.ShowFullScreen(True)
        self.blackjackMain.Show()
        self.st2 = StaticText(self.bitmapB, -1, ' ')
        self.st2.SetFont(self.fontr)
        self.st2.SetBackgroundColour('black')
        self.st2.SetForegroundColour('white')
        self.st2.SetPosition((45,48))
        return True

    def hit (self,event):
        print('Hit Player')
        self.ph.append(self.contents.pop(0))
        self.Calcular(1)
        if self.puntos < 21:
            print('player pass')
            self.bitmapCreator(1)
            self.st2.SetLabel('Hit!')
        else:
            print('players loss')
            self.coinsInicio -= self.apuestaB
            print(f'loss {self.apuestaB}')
            self.st2.SetLabel(f'Perdiste {self.apuestaB}!, tus puntos son mayores a 21')
            self.coinsViewB.SetLabel(str(self.coinsInicio))
            self.cartasD()

    def double(self,event):
        print('double')
        self.apuestaB = self.apuestaB * 2
        if self.apuestaB <= self.coinsInicio:
            print('pass')
            print(self.apuestaB)
            self.st2.SetLabel('Double bet!')
            return self.apuestaB
        else:
            self.st2.SetLabel(f'No cuentas con las coins suficientes para apostar!')

    def newHand(self,event):
        print('New Hand')
        self.st2.SetLabel('New Hand!')
        self.descarte(self.contents)
        self.ph.append(self.contents.pop(0))
        self.ph.append(self.contents.pop(0))
        print(f'New Cards : {self.ph}')
        self.bitmapCreator(1)

    def stand(self,event):
        self.Calcular(1)
        self.bot()
        if self.puntos > self.puntosDealer:
            self.coinsInicio += self.apuestaB
            print(f'win {self.apuestaB}')
            self.st2.SetLabel(f'Ganaste {self.apuestaB}!')
            self.coinsViewB.SetLabel(str(self.coinsInicio))
            self.cartasD()
        elif self.puntos < self.puntosDealer:
            self.coinsInicio -= self.apuestaB
            print(f'loss {self.apuestaB}')
            self.st2.SetLabel(f'Perdiste {self.apuestaB}!, la casa gana por diferencia de puntos')
            self.coinsViewB.SetLabel(str(self.coinsInicio))
            self.cartasD()
        elif self.puntos == self.puntosDealer:
            print(f'empate')
            self.st2.SetLabel(f'Empate, las apuestas se han cancelado!')
            self.coinsViewB.SetLabel(str(self.coinsInicio))
            self.cartasD()
    
    def bot(self):
        self.Calcular(0)
        if self.puntosDealer <= 16:
            print('Hit Dealer')
            self.dh.append(self.contents.pop(0))
            self.Calcular(0)
            self.bitmapCreator(0)
            self.st2.SetLabel('Hit Dealer!')
            if self.puntosDealer > 21:
                print('Dealer Bust')
                self.coinsInicio += self.apuestaB
                self.st2.SetLabel(f'La casa supera la suma de 21, gana {self.apuestaB} el jugador!')
                self.coinsViewB.SetLabel(str(self.coinsInicio))
                self.cartasD()

    def descarte (self,deck):
        for i in self.ph and self.dh:
            self.cartasDescartadas.append(i)
        self.ph = []
        self.dh = []
        print('Discard Complete')

    def Calcular(self, PoD):
        print(self.ph)
        pod = PoD
        numeroDeAces = 0
        if pod == 1:
            self.puntos = 0
            for card in self.ph:
                temp = card.split()
                if temp[0].isdigit():
                    self.puntos += int(temp[0])
                elif temp[0] == 'Ace':
                    self.puntos += 11
                    numeroDeAces += 1
                else:
                    self.puntos += 10
            while numeroDeAces > 0 and self.puntos > 21:
                numeroDeAces -= 1
                self.puntos -= 10

            return self.puntos, print(f'la suma total de las cartas del jugador es de {self.puntos} ')
        else:
            self.puntosDealer = 0
            for card in self.dh:
                temp = card.split()
                if temp[0].isdigit():
                    self.puntosDealer += int(temp[0])
                elif temp[0] == 'Ace':
                    self.puntosDealer += 11
                    numeroDeAces += 1
                else:
                    self.puntosDealer += 10
            while numeroDeAces > 0 and self.puntosDealer > 21:
                numeroDeAces -= 1
                self.puntosDealer -= 10

            return self.puntosDealer, print(f'la suma total de las cartas del dealer es de {self.puntosDealer} ')

    def ndeck(self):
        self.contents = ['02 of Diamonds',
         '02 of Hearts',
         '02 of Clubs',
         '02 of Spades',
         '03 of Diamonds',
         '03 of Hearts',
         '03 of Clubs',
         '03 of Spades',
         '04 of Diamonds',
         '04 of Hearts',
         '04 of Clubs',
         '04 of Spades',
         '05 of Diamonds',
         '05 of Hearts',
         '05 of Clubs',
         '05 of Spades',
         '06 of Diamonds',
         '06 of Hearts',
         '06 of Clubs',
         '06 of Spades',
         '07 of Diamonds',
         '07 of Hearts',
         '07 of Clubs',
         '07 of Spades',
         '08 of Diamonds',
         '08 of Hearts',
         '08 of Clubs',
         '08 of Spades',
         '09 of Diamonds',
         '09 of Hearts',
         '09 of Clubs',
         '09 of Spades',
         '10 of Diamonds',
         '10 of Hearts',
         '10 of Clubs',
         '10 of Spades',
         '0J of Diamonds',
         '0J of Hearts',
         '0J of Clubs',
         '0J of Spades',
         '0Q of Diamonds',
         '0Q of Hearts',
         '0Q of Clubs',
         '0Q of Spades',
         '0K of Diamonds',
         '0K of Hearts',
         '0K of Clubs',
         '0K of Spades',
         '0A of Diamonds',
         '0A of Hearts',
         '0A of Clubs',
         '0A of Spades']
        self.cartasDescartadas = []
        self.contents = self.contents * int(self.mazos.GetValue())
        print(f'Numero de mazos : {self.mazos.GetValue()}')
        print(f'Cantidad de cartas totales: {len(self.contents)}')

    def bitmapCreator (self,PoD):
        pod = PoD
        x = 574
        z = 1343
        if pod == 1:
            for i in range (len(self.ph)):
                g = self.ph[i]
                imgFile = str(g[:2]) + str(g[6:7]) + '.jpg'
                image = Image('./cartas/'+imgFile,BITMAP_TYPE_ANY).ConvertToBitmap()
                print(f'La carga de {imgFile} se ha realizado con exito!')
                x += 100
                i = (x, 766)
                bitmapC = StaticBitmap(self.bitmapB, -1, image, i)
        else:
            for i in range (1):
                g = self.dh[i]
                imgFile = str(g[:2]) + str(g[6:7]) + '.jpg'
                image = Image('./cartas/'+imgFile,BITMAP_TYPE_ANY).ConvertToBitmap()
                i = (z, 64)
                bitmapC = StaticBitmap(self.bitmapB, -1, image, i)
                if (len(self.dh)) > 1:
                    z += 100
                    imgFile = Image('./cartas/back.png',BITMAP_TYPE_ANY).ConvertToBitmap()
                    i = (z, 64)
                    bitmapDealer = StaticBitmap(self.bitmapB,-1,imgFile,i)
                    print(f'La carga de {imgFile} se ha realizado con exito!')
    
    def cartasD(self):
        z = 1243
        for i in range (len(self.dh)):
            z +=100
            g = self.dh[i]
            imgFile = str(g[:2]) + str(g[6:7]) + '.jpg'
            image = Image('./cartas/'+imgFile,BITMAP_TYPE_ANY).ConvertToBitmap()
            i = (z, 64)
            bitmapC = StaticBitmap(self.bitmapB, -1, image, i)

app = MyApp()
app.MainLoop()
