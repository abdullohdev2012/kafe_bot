from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
        KeyboardButton(text="🍸 ichimliklar"),
        KeyboardButton(text="🌯 lavashlar"),
        ], 
        [
        KeyboardButton(text="🍔 burgerlar"),
        KeyboardButton(text="🍕 pitsalar"),
        ],
        [
        KeyboardButton(text="🍰 shirinliklar"),
        KeyboardButton(text="location"),

         ],
    ],
    resize_keyboard=True
)


ichimliklar_menusi = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="pepsi"),
        KeyboardButton(text="fanta"),
        KeyboardButton(text="cola"),
        KeyboardButton(text=" orqaga"),
        ]
    ],
    resize_keyboard=True
)


lavashlar_menusi = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="sirli lavash"),
        KeyboardButton(text="achiq lavash"),
        KeyboardButton(text="classic lavash"),
        KeyboardButton(text="katta lavash"),
        KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)


burgerlar_menusi = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="chiz burger"),
        KeyboardButton(text="big burger"),
        KeyboardButton(text="classic burger"),
        KeyboardButton(text="achiq burger"),
        KeyboardButton(text="barbuku burger"),
        KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)


pitsalar_menusi = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="pipironi"),
        KeyboardButton(text="gavayskiy"),
        KeyboardButton(text="mesnoy"),
        KeyboardButton(text="barbukur"),
        KeyboardButton(text="orqaga"),
        ]
    ],
    resize_keyboard=True
)

shirinliklar_menusi = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text="pirojniy"),
        KeyboardButton(text="pechenya"),
        KeyboardButton(text="tort"),
        KeyboardButton(text=" orqaga"),
        ]
    ],
    resize_keyboard=True
)