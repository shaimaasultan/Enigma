
import random
import math
import numpy as np
from matplotlib import pyplot as plt

Lang_EN = 'EN'
Lang_AR = 'AR'

LangChar_Str = ''
Encode_mapList = []
encod_PunckDict = {}
decode_mapList = [] 

Source_message_file = 'C:\\Enigma\\SourceText.txt' 
decode_key_file = 'C:\\Enigma\\Key.txt'
Encrypted_file = 'C:\\Enigma\\EncryptedText.txt'
Decrypted_file = 'C:\\Enigma\\Decrypted.txt'

Lang_NumbersDict =  {  '0':'10000111','2':'100211' , '3':'10031', '4':'10041', '5': '100051', '6':'10061', '7':'10071', '8':'10081', '9': '10091'}

def set_language(lang):
    if lang == 'EN':
        ENbaseKey = "abcdefghijklmnopqrstuvwxyz ,.-'/()[]}{:=?!"
       
        ENkeymap = ['10000211', '208' , '207','206', '205', '204', '203', '202', '201', '109', '108' , '107'
            ,'106', '105', '104', '103', '102','1001' , '222' , '333', '444','555','666','777','888','999'
            ,'10000511', '10000611', '10000711', '10000811' ,'10000311' , '@' , '*' , '`' , '$','+','^','&','|','>','<' ,':' , '=' , '?' , '.','!' ]

        ENdecode_ch = {'`':'37' , '*':'17','$':'157', '@':'161','+':'61','.':'113','^':'193','&':'247','|':'27' , '>':'7' , '<':'9' 
                       , '?':'57' , ':' : '23' , '=':'13' , '!':'199'}
        ENdecode_map =  ['10000111' ,'100211' ,'10031' , '10041' ,'100051','10061', '10071', '10081', '10091', '10000211' 
        , '208' , '207' ,'206', '205' , '204', '203', '202' , '201' , '109' , '108','107','106','105','104'
        ,'103','102', '1001', '222' , '333' , '444','555', '666','777','888','999'
        ,'10000511','10000611','10000711','10000811','10000311']
        LangChar_Str = ENbaseKey
        Encode_mapList = ENkeymap
        encod_PunckDict = ENdecode_ch
        decode_mapList = ENdecode_map

    elif lang == 'AR':
        ARbaseKey = "ضصثقفغعهخحجدشسيبلاتنمكطئءؤرلاىةوزظذأإِا ,.-'/()[]}{:=?!"

        ARkeymap = ['10000211', '208' , '207','206', '205', '204', '203', '202', '201', '109', '108' , '107'
            ,'106', '105', '104', '103', '102','1001' , '222' , '333', '444','555','666','777','888','999'
           , '13011' , '13021', '13031','13041','13051','13061','13071','13081' , '13191' , '14801','15801','17901' , '18501'
            ,'10000511', '10000611', '10000711', '10000811' ,'10000311' , '@' , '*' , '`' , '$','+','^','&','|','>','<' ,':' , '=' , '?' , '.','!' ]

        ARdecode_ch = {'`':'37' , '*':'17','$':'157', '@':'161','+':'61','.':'113','^':'193','&':'247','|':'27' , '>':'7' , '<':'9' 
                       , '?':'57' , ':' : '23' , '=':'13' , '!':'199'}

        ARdecode_map =  ['10000111' ,'100211' ,'10031' , '10041' ,'100051','10061', '10071', '10081', '10091'
        , '10000211' , '208' , '207' ,'206', '205' , '204', '203', '202' , '201' , '109' , '108','107'
        ,'106','105','104','103','102', '1001', '222' , '333' , '444','555', '666','777','888','999'
        , '13011' , '13021', '13031','13041','13051','13061','13071','13081' , '13191' , '14801','15801' ,'17901' , '18501'
        ,'10000511','10000611' ,'10000711','10000811','10000311']

        LangChar_Str = ARbaseKey
        Encode_mapList = ARkeymap
        encod_PunckDict = ARdecode_ch
        decode_mapList = ARdecode_map

    #print(len(LangChar_Str) , len(Encode_mapList) , len(encod_PunckDict) , len(decode_mapList) , LangChar_Str , lang)

    return LangChar_Str , Encode_mapList , encod_PunckDict , decode_mapList

def read_text(filepath):
    with open(filepath , "r" , encoding='UTF-8') as f:
        instr = f.read()
    return instr

def save_text(filepath , txt ):
    with open(filepath , "w" , encoding='UTF-8') as f:
        f.write(txt)

def generate_random(text ,length):
    return ''.join(random.sample(text,length))

def encode(encodestr , map = Encode_mapList ,base= LangChar_Str ):    
    #Num = Encode_Num
    for key,val in Lang_NumbersDict.items():
        encodestr = encodestr.replace(key,val)
    
    for i , v in enumerate(base):
        #if i >= len(map):
        #    print( i , len(map), len(base))
        encodestr = encodestr.replace( v , map[i])
    return encodestr  

def Decode(decodestr , map = decode_mapList ,base= LangChar_Str):    
    #print('decode key FUNCTION', decodestr[:40] , map ,base )
    for i , v in enumerate(base):
        if i >= len(map) :
            print("encode map list" , i , len(base) , len(map), Encode_mapList , decode_mapList , map)
        else:
            decodestr = decodestr.replace(map[i] , v)
    for key,val in Lang_NumbersDict.items():
        decodestr = decodestr.replace(val , key)   
    return decodestr    

def ReshapeToImage(encodestr , map = decode_mapList , punk = encod_PunckDict ):
    #print('reshape encode string' , encodestr , map)
    for i in map:
        encodestr = encodestr.replace( str(i) , 'X'+str(int(i)%255)+'X')     
    
    for key , val in punk.items():
        encodestr = encodestr.replace( key , 'X'+str(val)+'X')   
    return encodestr
  

def Decode_Image(img , map = decode_mapList  , base= LangChar_Str , language = Lang_EN):

    LangChar_Str , Encode_mapList , encod_PunckDict , decode_mapList = set_language(language)  

    map = Encode_mapList
    base = LangChar_Str
    
    message_list = []
    key_list = []
    key = False
    char_to_encode = len(base)
    decode_text = ''
    start = 0
    end = -1 

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if str(img[y][x][0]) == '255' and str(img[y][x][1]) == '255' and str(img[y][x][2]) =='255' and key == False:
                key= True
            if key == False :
                key_list.append(img[y][x][0])
                key_list.append(img[y][x][1])
                key_list.append(img[y][x][2])
            else:
                message_list.append(img[y][x][0])
                message_list.append(img[y][x][1])
                message_list.append(img[y][x][2]) 

    decode_ch=encod_PunckDict

    for i in decode_mapList:
        decode_ch[i] = str(int(i)%255)

    mapch = dict((str(v),k) for k,v in decode_ch.items())
    encoded_message = []
    for i in message_list:
        if mapch.get(str(i)) != None :
            encoded_message.append(mapch.get(str(i)))
        if str(i) in ['1' , '4']:
            encoded_message.append(str(i))
        
    encoded_message = ''.join(encoded_message)

    encoded_key = []
    for i in key_list:
        if mapch.get(str(i)) != None :
            encoded_key.append(mapch.get(str(i)))
    
    encoded_key = ''.join(encoded_key)
    key = Decode(decodestr = encoded_key  , map = Encode_mapList ,base= LangChar_Str)  
    #print('Key from Image : ' , key)

    for j in range(0,len(key), char_to_encode):
        word_key = key[j:j+char_to_encode]
        space_code = map[word_key.find(' ')]
        i = encoded_message.find(space_code , start , end)
        word = encoded_message[start:i]
        start = i+len(space_code)   
        decode_text = decode_text + Decode(word , map = Encode_mapList , base=word_key) + ' '
        #print(decode_text)
    save_text(Decrypted_file, decode_text)
    return (decode_text)


def Encrypt_To_Image(source_file = Source_message_file 
        ,  Encrypted_file = Encrypted_file
        ,  key_file = decode_key_file 
        ,  language = Lang_EN):
    
    LangChar_Str , Encode_mapList , encod_PunckDict , decode_mapList = set_language(language)   

    encodetxt = ''
    decode_key= ''

    random_char_map_key = generate_random(LangChar_Str , len(LangChar_Str))
    source_file_text = read_text(source_file)

    for word in source_file_text.split(' '):
        random_char_map_key = generate_random(LangChar_Str , len(LangChar_Str))
        #print(random_char_map_key)
        decode_key = decode_key + random_char_map_key
        encoded_word = encode(word.lower()+' ',map=Encode_mapList, base=random_char_map_key)
        encodetxt = encodetxt  + encoded_word 
    
    image_list = ReshapeToImage(encodetxt , map = decode_mapList , punk= encod_PunckDict).split('X')
    massage_image = [i for i in image_list if len(i) >0 and i.isnumeric() ]
    

    Encoded_Key = encode(decode_key,map=Encode_mapList,base=LangChar_Str)
    key_list = ReshapeToImage(Encoded_Key , map = decode_mapList , punk= encod_PunckDict).split('X')
    key_image = [i for i in key_list if len(i) >0 and i.isnumeric() ]
    #print('key_image', key_image)

    #print('message' , encodetxt[:40])
    #print('reshape' , image_list[:40])
    #print('decode_key', decode_key[:40])
    #print('decode_key', Encoded_Key[:40])
    #print('key_list', key_list[:40])
    #print('key_image', key_image[:40])
 
    text_and_key = key_image + ['255','255','255','255','255','255','255','255','255'] + massage_image
    l = [i for i in text_and_key if len(i) >0 and i.isnumeric() ]
    channel = 3
    image_dim = math.ceil(math.sqrt(len(l)/channel))
    # Create an empty image
    img = np.zeros((image_dim, image_dim, channel), dtype=np.uint8)
    diff = ((image_dim* image_dim) * 3) - len(l)
    for i in range(diff+1):
        l.append(l[len(l)-1])

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y][x][0] = l.pop(0)
            img[y][x][1] = l.pop(0)
            img[y][x][2] = l.pop(0)

    plt.imshow(img)
    plt.title(label=source_file_text[:150],loc='left')
    plt.show()


    save_text(Encrypted_file, encodetxt)
    save_text(key_file,decode_key)
    #print("==================================")
    #print("1- Random encode char map key : {0} ".format( random_char_map_key ))
    print("================original TEXT==================")
    print(source_file_text[:200])
    print("================ENCODE==================")
    print(encodetxt[:200])
    print("==================================")
    return encodetxt , img

    