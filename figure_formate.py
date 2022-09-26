startup="   _______    ______    ___       ___  ___\n"\
'  |   __ "\\  /    " \\  |"  |     |"  \\/"  |\n'\
'  (. |__) :)// ____  \\ ||  |      \\   \\  /\n'  \
'  |:  ____//  /    ) :)|:  |       \\  \\/ \n' \
'  (|  /   (: (____/ //  \\  |___    /   / \n' \
' /|__/ \\   \\        /  ( \\_|:  \\  /   /  \n' \
'(_______)  \\"_____/    \_______)|___/  \n' \
'                                     \n' \
'  ______        __        _______    \n' \
' /" _  "\\      /""\\      /"      \\   \n' \
'(: ( \\___)    /    \\    |:        |  \n' \
' \/ \\        /'' /\\  \\   |_____/   )  \n' \
' //  \\ _    //  __''  \\   //      /   \n' \
'(:   _) \\  /   /  \\  \\ |:  __   \\   \n' \
' \_______)(___/    \\___)|__|  \\___)  \n'\
'\n By Xiaoyong Wei @ COMP 1012\n'\
' SEP 24, 2022'

print(startup)

def encode2rect(pic):
    rows=pic.split('\n')
    rectcode_c=[]
    maxlen=0
    for row in rows:
       maxlen=max(maxlen,len(row))
    for row in rows:
        row_new=row+" "*(maxlen-len(row))
        rectcode_c.append(row_new)
    rectcode=[]
    for s in rectcode_c:
        rectcode.append([ord(c) for c in s])
    return rectcode

#startcode=encode2rect(startup)
#print(startcode)

car="    ____\n"\
" __/  |_\_\n"\
"|  _     _``-.\n"\
"'-(_)---(_)--'\n"

# carcode=encode2rect(car)
# print(carcode)

dog="  .\n"\
" ..^____/\n"\
"`-. ___ )\n"\
"  ||  ||"

# dogcode=encode2rect(dog)
# print(dogcode)


dog2="        __\n"\
"   (___()'`;\n"\
"   /,    /`\n"\
"   \\\"--\\"

dogcode=encode2rect(dog2)
print(dogcode)

crashed='   ___              _              _   _ \n'\
'  / __\\ __ __ _ ___| |__   ___  __| | / \\\n'\
' / / | \'__/ _` / __| \'_ \\ / _ \\/ _` |/  /\n'\
'/ /__| | | (_| \\__ \\ | | |  __/ (_| /\\_/ \n'\
'\\____/_|  \\__,_|___/_| |_|\\___|\\__,_\\/  \n'

print(crashed)
crashedcode=encode2rect(crashed)
print(crashedcode)