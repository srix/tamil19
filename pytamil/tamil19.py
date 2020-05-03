# -*- coding: utf-8 -*-

import sys

#FIXME: use PYTHONPATH with module directory
sys.path.append('../pytamil')

from pytamil import தமிழ்
from தமிழ் import இலக்கணம் as இல
from தமிழ் import புணர்ச்சி
from தமிழ் import எழுத்து
from தமிழ் import மாத்திரை
import os


# print( எழுத்து.எழுத்துக்கள்['மெல்லினம்'])
# print( எழுத்து.எழுத்துக்கள்['குறில்'] )

# print (தமிழ்.வட்டெழுத்து('வணக்கம்'))


# print ( எழுத்து.தொடர்மொழி_ஆக்கு('விருந்து', 'ஓம்பல்' ))

# print( இல.தொடர்மொழி_ஆக்கு('விருந்து', 'ஓம்பல்'))
# print( இல.தொடர்மொழி_ஆக்கு('மெய்', 'எழுத்து'))
# print( இல.தொடர்மொழி_ஆக்கு('மெய்', 'பழுத்து'))
# print( இல.தொடர்மொழி_ஆக்கு('முள்', 'இலை'))
# print( இல.தொடர்மொழி_ஆக்கு('உயிர்', 'எழுத்து'))
# print( இல.தொடர்மொழி_ஆக்கு('வேல்', 'எறிந்தான்'))


# விதிகள் =[]
# விதிகள் = getவிதிகள்(entries,விதிகள்)
# சான்றுகள் = []
# சான்றுகள் = getசான்றுகள்(entries, சான்றுகள்)
# print(விதிகள்)
# print(சான்றுகள்)

# result = புணர்ச்சி.check("(...)(இ,ஈ,ஐ)" ,"மணிதன்")
# print (result)
# result = புணர்ச்சி.check("(...)(உயிர்)" , "மணி")
# print (result)
# result = புணர்ச்சி.check("(உயிர்)(...)" , "அடி")
# print (result)

# print(புணர்ச்சி.தொடர்மொழி_ஆக்கு( 'உயிர்' , 'எழுத்து'))

# புணர்ச்சி.புணர்ச்சிசெய்('''சே|உடம்படுமெய்(ய்)|சும்மா +  சும்மா|திரிதல்(வ்)|அடி ,
#                       சே|உடம்படுமெய்(வ்) + திரிதல்(வ்)|அடி,
#                       சே|உடம்படுமெய்(வ்) + திரிதல்(வ்)|அடி ''')

# புணர்ச்சி.புணர்ச்சிசெய்('''சே|உடம்படுமெய்(ய்)|சும்மா +  சும்மா|திரிதல்(வ்)|அடி ,
#                       சே|உடம்படுமெய்(வ்) + திரிதல்(வ்)|அடி''')
# புணர்ச்சி.புணர்ச்சிசெய்('சேய் +இயல்பு+ அவ்')
# புணர்ச்சி.தொடர்மொழி_ஆக்கு('சே', 'அடி' )
# புணர்ச்சி.தொடர்மொழி_ஆக்கு('கண்', 'மங்கியது')

# print(மாத்திரை.மாத்திரை_கொடு('புணர்ச்சிசெய்'))
# print(மாத்திரை.மொத்தமாத்திரை('புணர்ச்சிசெய்'))
# print(மாத்திரை.printtree("ஊக்கம்"))
print(மாத்திரை.மாத்திரைவரிசை_கொடு("ஊக்கம்"))
# outfilename = os.path.join(os.path.dirname(__file__),'தமிழ்/resources/மாத்திரைoutput.txt')
# மாத்திரை.printtree_tofile("ஊக்கம்", outfilename)


# print(புணர்ச்சி.தொடர்மொழி_ஆக்கு( 'மணி' , 'அடித்தான்'))
# print(புணர்ச்சி.தொடர்மொழி_ஆக்கு( 'மெய்', 'எழுத்து'))
# print(புணர்ச்சி.தொடர்மொழி_ஆக்கு( 'நிலா', 'ஒளி'))
