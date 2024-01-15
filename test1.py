def update_dict(key, value, defaults={}):
    defaults[key] = value
    print(defaults)
    
    
update_dict(key='fruit', value='apple')
update_dict(key='vegetable', value='tomato', defaults = {'tree': 'oak'})
update_dict(key='car', value='ferrari')

### improve script performance
import requests
 
 
def get_page(category: str, page_id: int) -> str:
    if page_id:
        url = 'https://www.ozon.ru/brand/{0}/?page={1}'.format(category, page_id)
    else:
        url = 'https://www.ozon.ru/brand/{0}/'.format(category)
    print('get url: {0}'.format(url))
    response = requests.get(url)
    return response.text
 
 
def load_data():
    category_list = ['adidas-144082850', 'puma-87235756']
    for category in category_list:
        for page_id in range(50):
            text = get_page(category, page_id)
            # обрабатываем полученный текст, сохраняем в файл/базу
 
 
if __name__ == '__main__':
    load_data()
### updated with concurrent.futures
import concurrent.futures

def load_data():
    category_list = {'adidas-144082850', 'puma-87235756'}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_category = {executor.submit(get_page, category, page_id): category for category in category_list for page_id in range(50)}
        for future in concurrent.futures.as_completed(future_to_category):
            category = future_to_category[future]
            text = future.result()
            process_text(text)

def get_page(category, page_id):
    # TODO: Implement the logic to fetch the page for the given category and page_id
    pass

def process_text(text):
    # TODO: Implement the processing logic here
    pass
###
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