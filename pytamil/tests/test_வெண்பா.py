import pytest
from pytamil.தமிழ் import எழுத்து
from pytamil.தமிழ் import வெண்பா



@pytest.mark.parametrize("பத்தி", \
    [ 
        #நளவெண்பா - கடவுள் வணக்கம் - 1
        ('''ஆதித் தனிக்கோல மானா னடியவற்காச்
            = தேமா புளிமாங்காய் தேமா கருவிளங்காய்
            சோதித் திருத்தூணிற் றோன்றினான் வேதத்தின்
            = தேமா புளிமாங்காய் கூவிளம் தேமாங்காய்
            முன்னின்றான் வேழம் முதலே யெனவழைப்ப
            = தேமாங்காய் தேமா புளிமா கருவிளங்காய்
            என்னென்றா னெங்கட் கிறை
            = தேமாங்காய் தேமா மலர்'''),

    # ('''ஆதித் தனிக்கோல மானா னடியவற்காச்
    # = தேமா புளிமாங்காய் தேமா கருவிளங்காய்
    # சோதித் திருத்தூணிற் றோன்றினான் வேதத்தின்
    # = தேமா புளிமாங்காய் கூவிளம் தேமாங்காய்
    # முன்னின்றான் வேழம் முதலே யெனவழைப்ப
    # = தேமாங்காய் தேமா புளிமா கருவிளங்காய்
    # என்னென்றா னெங்கட் கிறை
    # = தேமாங்காய் தேமா மலர்''' ),
    ])
def test_சீர்கொடு(பத்தி):   
    
    # extract செய்யுள் lines only
    பாடல்_அடிகள் =  [ அடி.strip() for i,அடி in enumerate(பத்தி.strip().splitlines()) if not i%2 ]
    பாடல் =  "\n".join(பாடல்_அடிகள்)
    சீர்_அடிகள் =  [ அடி.strip() for i,அடி in enumerate(பத்தி.strip().splitlines()) if i%2 ]

    அடிவரிசை = வெண்பா.சீர்கொடு(பாடல்)
    புது_சீர்_அடிகள் = ["= "+" ".join(அடி) for அடி in அடிவரிசை]

    assert சீர்_அடிகள் == புது_சீர்_அடிகள்
    
	

