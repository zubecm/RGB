def rgb(r, g, b):
    red=''
    green=''
    blue=''
    ans=''
    h='0123456789ABCDEF'
    if r>=255:
        red='FF'
    elif r<=0:
        red="00"
    else:
        while r>0:
            red=h[r%16]+red
            r//=16
    if len(red)==1:
        red='0'+red
    if g>=255:
        green='FF'
    elif g<=0:
        green="00"
    else:
        while g>0:
            green=h[g%16]+green
            g//=16
    if len(green)==1:
        green='0'+green
    if b>=255:
        blue='FF'
    elif b<=0:
        blue="00"
    else:  
        while b>0:
            blue=h[b%16]+blue
            b//=16
    if len(blue)==1:
        blue='0'+blue
    ans=red+green+blue
    return(ans)