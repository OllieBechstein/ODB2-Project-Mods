name = "Food Planet"
version = "1.0"
description = "Adds a new food based planet to Slipways for use with the Billy Mod."
contents = [
    # a spreadsheet that defines new objects added to the game by your mod
    # you probably need this one
    
    "things.xls",

    # code for the new additions
    
    "code.py",
    
    # localized text for your mod
    
    "text-english.xls" / lang("english"), # this is the english version

    # custom graphics/sound for your mod
    # uncomment the lines below only after creating an asset bundle with the Slipways asset tool
    # refer to the modding documentation for details on how to do that
    
    #"assets.win", "assets.mac",
]
