def jsonTranslation(_command):
        if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, a\
nd pass it back, to get stored along with the command                                                                                                
                factoryState=FactoryState.objects[0]
                jsonString=render_to_string(_command + ".html", {'command': _command, 'factoryState' : factoryState})
        else:
                jsonString=""
        return jsonString
