def say_hello(name, language):
    
    if language=="FR":
        print(f"Bonjour {name}")

    elif language=="NL":
        print(f"Dag {name}")

    elif language=="EN":
        print(f"Hello {name}")

    else:
        raise Exception("You didn't inputed known language")