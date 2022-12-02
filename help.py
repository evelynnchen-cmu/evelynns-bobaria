from classes import *

###################################
#view
###################################
def helpScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    #changes the current help scene screen
    if app.curHelpScene == 1:
        drawGameHelp(canvas)
    elif app.curHelpScene == 2:
        drawShopHelp(app, canvas)
    elif app.curHelpScene == 3:
        drawKitchenHelp(app, canvas)
    elif app.curHelpScene == 4:
        drawEvalHelp(app, canvas)
    
    #if the user came from the game, they should only see their current screen's help screen
    if not app.cameFromGame:    
        if app.curHelpScene == 4:
            drawButton(canvas, app.help_doneBtnDms, 'Done')
        else:
            drawButton(canvas, app.help_nextBtnDms, 'Next')
            
        if app.curHelpScene != 1:
            drawButton(canvas, app.help_backBtnDms, 'Back')
    else:
        drawButton(canvas, app.help_doneBtnDms, 'Go to Game')
    
def drawGameHelp(canvas):
    canvas.create_text(500, 100, text="Welcome to Evelynn's Bobaria!", font='Courier 35 bold')
    canvas.create_text(450, 300, text=
        """
        Your journey to becoming a master bobarista begins today.\n
        As a bobarista at Evelynn's Bobaria, you must do the following:\n
        1. Take the customer's order\n
        2. Make the drink order\n
        3. Present the drink to the customer for evaluation.\n\n
        Click 'Next' to visit the shop and see how the masters do it!
        """, font='Courier 15 bold')
    
def drawShopHelp(app, canvas):
    canvas.create_text(500, 25, text='Shop Screen', font='Courier 25 bold')
    canvas.create_text(250, 175, text="""
        Sit behind the counter and wait\n
        until a customer appears. When they\n
        do, click on 'Take Order' to take\n
        their order.
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.isCustScene, (400, 225))))
    
    canvas.create_text(225, 400, text="""
        Once you have their order,\n
        click on 'Kitchen' to go make it.
        """, font='Courier 13 bold')
    canvas.create_image(700, 425, image=ImageTk.PhotoImage(scaleImage(app, app.gotOrderScene, (400, 225))))
    
def drawKitchenHelp(app, canvas):
    canvas.create_text(500, 25, text='Kitchen Screen', font='Courier 25 bold')
    canvas.create_text(250, 175, text="""
        Click and drag each ingredient over to\n
        the cup to add it to the drink.\n
        Be accurate with how much you add.\n
        Customers are more lenient at first,\n
        but won't be for long...
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.addIngScene, (400, 225))))
    
    canvas.create_text(225, 400, text="""
        Once you added all ingredients,\n
        click 'Mix' to mix the drink.\n
        Then click 'Evaluate' to present\n
        the drink to the customer.
        """, font='Courier 13 bold')
    canvas.create_image(695, 425, image=ImageTk.PhotoImage(scaleImage(app, app.mixedDrinkScene, (400, 225))))
    
    
    # photoImage = app.addIngGif[app.spriteCounter]
    # canvas.create_image(700, 175, image=photoImage)
    
def drawEvalHelp(app, canvas):
    canvas.create_text(500, 25, text='Evaluation Screen', font='Courier 25 bold')
    canvas.create_text(250, 175, text="""
        Let the customer evaluate the drink\n
        and calculate its score and the amount\n
        of tips. Remember, customers are \n
        impatient. The quicker you are, the\n
        more tips you receive!
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.custCritiqueScene, (400, 225))))
    
    canvas.create_text(230, 400, text="""
        Once the customer made up their mind,\n
        you'll be able to see the results on\n
        your right-hand side. Click 'Done' to\n
        return to the shop counter.
        """, font='Courier 13 bold')
    canvas.create_image(700, 425, image=ImageTk.PhotoImage(scaleImage(app, app.custEvalScene, (400, 225))))
        
###################################
#controller
###################################
        
def helpScreen_mouseReleased(app, event):
    # next button check
    if isValidClick(event.x, event.y, app.help_nextBtnDms) and app.curHelpScene < 4 and not app.cameFromGame:
        app.curHelpScene += 1
    # back button check
    if isValidClick(event.x, event.y, app.help_backBtnDms) and app.curHelpScene > 1 and not app.cameFromGame:
        app.curHelpScene -= 1
    #done button
    if isValidClick(event.x, event.y, app.help_doneBtnDms) and (app.curHelpScene == 4 or app.cameFromGame):
        if not app.cameFromGame:
            app.mode = 'startScreen'
        else:
            if app.curHelpScene == 2:
                app.mode = 'shopScreen'
            elif app.curHelpScene == 3:
                app.mode = 'kitchenScreen'
            elif app.curHelpScene == 4:
                app.mode = 'evaluationScreen'
        
def helpScreen_timerFired(app):
    pass
    # if app.curHelpScene == 2:
    #     app.spriteCounter = (1 + app.spriteCounter) % len(app.addIngGif)