def turn(e):
    if '-' in e:
        spliter='-'
    elif ':' in e:
        spliter=':'
    else:
        return e
    (mins,secs)=e.split(spliter)
    return mins+'.'+secs
