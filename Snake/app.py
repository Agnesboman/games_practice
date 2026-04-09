from render import View

def initializeGame():
    return renderStartView()

def renderStartView():
    v = View(300, 400)
    return v.startView()
def renderGameView():
    return null

if __name__ == "__main__":
    initializeGame()