from classes import *

###################################
#view
###################################
def startScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    drawButton(canvas, app.start_startBtnDms, 'Start')

###################################    
#controller
###################################
def startScreen_mouseReleased(app, event):
    # start button
    if isValidClick(event.x, event.y, app.start_startBtnDms):
        app.mode = 'shopScreen'