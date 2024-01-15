import urllib.parse

"""

Есть строка payload
строка url encoded
Внутри строки есть телефон  To=whatsapp%3A%2B551142002991
нужно внутрь строки paylod поменять телефон так что бы после первых 4 цифр добавилась девятка
те из 551142002991 должно получиться 5511942002991

"""

payload = "SmsMessageSid=SMba69a2ca48ef1794f03f0521d5733833&NumMedia=0&WaId=553193209107&SmsStatus=received&Body=At%C3%A9+%C3%A0s+23%3A59+compro+%3B%29&NumSegments=1&ReferralNumMedia=0&From=whatsapp%3A%2B553193209107&ApiVersion=2010-04-01&To=whatsapp%3A%2B551142002991"




def fix_payload(payload: str) -> str:
    parsed_payload = urllib.parse.parse_qs(payload)
    phone_number = parsed_payload["To"][0]
    fixed_phone_number = phone_number[:5] + "9" + phone_number[5:]
    parsed_payload["To"][0] = fixed_phone_number
    fixed_payload = urllib.parse.urlencode(parsed_payload, doseq=True)
    return fixed_payload

#print(fix_payload(payload))

class Animal:
    def say(self):
        print('i am animal')
 
 
class Cat(Animal):
    pass
 
 
class Robot:
    def say(self):
        print('i am robot')
 
 
class RoboCat(Cat, Robot):
    pass
 
 
robo = RoboCat()
robo.say()

###
first_list = [[0, 1, 2], [3, 4, 5]]
second_list = list(first_list)
first_list.append([6, 7, 8])
first_list[1][0] = 9
 
print(first_list)
print(second_list)
###
def multipliers():
    return [lambda x: i * x for i in range(4)]
 
print([m(2) for m in multipliers()])
###
for site in Site.objects.all(): #todo improve django code
    print(site.user.email)
###
    У нас есть интернет-магазин на Django. Товар в нём представлен очень разнообразный, поэтому для каждой категории товара выделена отдельная модель, которая содержит специфические для неё поля. Для каждой категории товара у нас подготовлены отдельные view (20+ штук), которые содержат детализированные фильтры. 
Конечные урлы имеют вид:
 
для списка товаров в категории:
/catalog/<uniq_category_slug>/
/catalog/<uniq_category_slug>/page-2
/catalog/<uniq_category_slug>/page-3
...
 
для информации о товаре:
/catalog/<uniq_category_slug>/<product_slug>-detail
 
Мы хотим узнать, какие категории больше всего интересуют наших посетителей. Для этого создали модель, в которую планируем записывать эту информацию:
```
class UserVisits(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    date = models.DateTimeField()
    visits = models.PositiveIntegerField(default=0)
```    
 
Каким образом нам начать собирать эту статистику, чтобы не пришлось в каждом из view прописывать логику по её сбору?