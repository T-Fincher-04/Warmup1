from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)
        self.accept('escape', self.quit)
        self.parent =self.loader.loadModel("./Assets/cube")
        self.disableMouse()
        self.camera.setPos(0.0, 0.0, 250.0)
        self.camera.setHpr(0.0, -90.0, 0.0)
        self.accept('escape', self.quit)
        self.accept('arrow left', self.negativeX,[1])
        self.accept('arrow left-up', self.negativeX, [0])

        x = 0
        for i in range(100):
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(50.0 * math.cos(theta),50.0 * math.sin(theta), 0.0 * math.tan(theta))
            red = 0.6 + random.random() * 0.4
            green =  0.6 + random.random() * 0.4
            blue =  0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06

    def quit(self):
        sys.exit()
    
    def negativeX(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
            self.taskMgr.remove('moveNegativeX')

    def moveNegativeX(self, task):
        self.fighter.setX(self.fighter, -1)
        return task.cont
        
import math, sys, random



app = MyApp()
app.run()