import logging
from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton
from aiogram import Bot ,Dispatcher ,executor,types
from tugmalar import *
# from reply_btn import *
from inline_btn import  my_inline_btn

logging.basicConfig(level=logging.INFO)

BOT_TOKEN ="6227937062:AAEGkSHU5wKvQdGBNto-JssCWVyjYeKmqmg"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start","menu"])
async def bot_start_handler(message :types.Message):
    await message.answer("Assalomu aleykum bu feed up", reply_markup=bosh_menu)

@dp.message_handler(text="🍸 ichimliklar")
async def bot_start_handler(message :types.Message):
    await message.answer("mana ", reply_markup=ichimliklar_menusi)    

@dp.message_handler(text="🌯 lavashlar")
async def bot_start_handler(message :types.Message):
    await message.answer("mana ", reply_markup=lavashlar_menusi)  


@dp.message_handler(text="🍔 burgerlar")
async def bot_start_handler(message :types.Message):
    await message.answer("mana ", reply_markup=burgerlar_menusi)  
    
  
@dp.message_handler(text="🍕 pitsalar")
async def bot_start_handler(message :types.Message):
    await message.answer("mana ", reply_markup=pitsalar_menusi) 

@dp.message_handler(text="🍰 shirinliklar")
async def bot_start_handler(message :types.Message):
    await message.answer("mana ", reply_markup=shirinliklar_menusi)  


@dp.message_handler(text="pepsi")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://babymarket.uz/wp-content/uploads/2020/05/peps_cola_05-l.jpg",caption="""
pepsi:
0,5 l - 6000 so'm
1 l - 9000 so'm
1,5 l - 12000so'm
2 l - 15000 so'm
    
    """)  
@dp.message_handler(text="fanta")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://ru.coca-cola.uz/content/dam/one/uz/ru/section-header-mobile/fanta-header_mobile_image.jpg",caption=
                               """
fanta
0,5 l - 6000 so'm
1 l - 9000 so'm
1,5 l - 12000so'm
2 l - 15000 so'm
    
    """)  
@dp.message_handler(text="cola")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://elitalco.kz/upload/images/26897_508874_09.jpeg", caption="""
cola
0,5 l - 6000 so'm
1 l - 9000 so'm
1,5 l - 12000so'm
2 l - 15000 so'm
    
    """)      

@dp.message_handler(text="achiq lavash")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://zira.uz/wp-content/uploads/2022/06/shaurma-18.jpg", caption="""
lavash:
katta - 23000 so'm
kichik - 19000 so'm  

    """)     

@dp.message_handler(text="sirli lavash")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20lavash.jpg", caption="""
lavash:
  katta - 21000 so'm
  kichik - 18000 so'm  

    """)  
@dp.message_handler(text="classic lavash")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://thumbs.dreamstime.com/b/shawarma-lavash-%D1%81-%D0%BC%D1%8F%D1%81%D0%BE%D0%BC-%D0%B8-%D0%BE%D0%B2%D0%BE%D1%89%D0%B0%D0%BC%D0%B8-%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8-%D0%BD%D0%BE%D0%BC%D0%B5%D1%80%D0%B0-%D1%81%D1%82%D1%83%D0%B4%D0%B8%D0%BE-199102677.jpg", caption="""
lavash:
  katta - 20000 so'm
  kichik - 17000 so'm  

    """)     
@dp.message_handler(text="katta lavash")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://yukber.uz/image/cache/catalog/lavash-700x700.jpg", caption="""
lavash:
  katta - 20000 so'm
  kichik - 17000 so'm  

    """)       

@dp.message_handler(text="chiz burger")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://www.sargento.com/assets/Uploads/Recipe/Image/burger_0.jpg", caption="""
lavash:
  katta - 30000 so'm
  kichik - 27000 so'm  

    """) 
@dp.message_handler(text="big burger")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://assets.epicurious.com/photos/5c745a108918ee7ab68daf79/1:1/w_2560%2Cc_limit/Smashburger-recipe-120219.jpg", caption="""
lavash:
  katta - 31000 so'm
  kichik - 28000 so'm  

    """)    

@dp.message_handler(text="classic burger")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://rustlersonline.com/wp-content/uploads/2020/09/Cheeseburger-5-1180x878.png", caption="""
burger:
  katta - 29000 so'm
  kichik - 26000 so'm  

    """)

@dp.message_handler(text="achiq burger")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://pasta.uz/upload/products/Triple.jpg", caption="""
burger:
katta - 32000 so'm
kichik - 30000 so'm  

""")   



@dp.message_handler(text="barbuku burger")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://pasta.uz/upload/products/Caesar.jpg", caption="""
burger:
  katta - 33000 so'm
  kichik - 31000 so'm  

    """)  


@dp.message_handler(text="pipironi")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://bravopizza.uz/wp-content/uploads/2020/04/peperoni-1.jpg", caption="""
pitsa:
  katta - 65000 so'm
  kichik - 62000 so'm  

    """)    


@dp.message_handler(text="gavayskiy")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://attuale.ru/wp-content/uploads/2018/04/a7074024-c45b-4d1d-b26a-a7dd00de056f-1024x792.jpg", caption="""
pitsa:
  katta - 66000 so'm
  kichik - 63000 so'm  

    """) 

@dp.message_handler(text="mesnoy")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://kartinkin.net/uploads/posts/2022-08/thumbs/1661233887_2-kartinkin-net-p-gavaiskaya-pitstsa-s-kuritsei-vkontakte-2.png", caption="""
pitsa:
  katta - 68000 so'm
  kichik - 63000 so'm  

    """) 



@dp.message_handler(text="barbukur")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://s23209.pcdn.co/wp-content/uploads/2021/10/BBQ-Chicken-PizzaIMG_0027-500x500.jpg", caption="""
pitsa:
katta - 69000 so'm
kichik - 62000 so'm  

    """) 

@dp.message_handler(text="pirojniy")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/w8T9289h0W4/maxresdefault.jpg ", caption="""
shirinlik:
 dona - 10000  so'm
 

    """)     
@dp.message_handler(text="pechenya")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://paulinecakeclub.ru/wp-content/uploads/2023/01/pesochnoe-pechene-na-moloke-foto-1-952x472.jpg", caption="""
shirinlik:
 dona - 5000  so'm
 

    """)    


@dp.message_handler(text="tort")
async def bot_start_handler(message :types.Message):
    await message.answer_photo(photo="https://gotovimop.com/wp-content/uploads/2022/02/tort-raduga.jpg", caption="""
shirinlik:
 dona - 100000  so'm
 

    """)     

@dp.message_handler(text="location")
async def bot_start_handler(message:types.Message) :
    await message.answer_location(41.368569418566885, 69.29784412860468)   

@dp.message_handler(text="orqaga")
async def bot_start_handler(message:types.Message) :
    await message.answer("mana",reply_markup=bosh_menu)    

# @dp.message_handler(commands=["reply"])
# async def bot_reply_handler(message :types.Message):
#     btn = await my_reply_btn()
#     await message.answer("Reply btn", reply_markup=btn)

@dp.message_handler(commands=["inline"])
async def bot_inline_handler(message :types.Message):
    btn = await my_inline_btn()
    await message.answer("inline btn", reply_markup=btn)


# @dp.message_handler()
# async def my_reply_num_handler(message:types.Message):
#     text =message.text

#     if text.isdigit():
#         await message.delete()
#         await message.answer(f" Javob: {int(text)  **2}")\
        
# @dp.callback_query_handler(text_contains = "n")
# async def my_num_callback(call:types.CallbackQuery):
#     await call.answer()
#     num = call.data.split("n")[1]
#     btn = await my_inline_btn()
#     if not num  in  call.message.text:
#         await call.message.edit_text(f" Javob:  {int(num) **3}" ,reply_markup=btn  )


if __name__ == "__main__":
    executor.start_polling(dp)



   