# mylife_myrules
### Використані бібліотеки
1) **_collections_**, а саме _deque_ для реалізації черги
2) **_random_** :
    - _randint_ : шанс на випадкову подію ```randint(1,8) == 2```
   - _choice_ : рандомний вибір стрічки, наприклад погоди ``` self.weather = choice(['warm', 'rainy', 'overcast']) ```
### Алгоритм
- Він полягає в тому, що ```self.state``` це функція, як об'єкт, тобто ```self.state = self.sleep```<br>
А сама логіка і умови прописані в кожному стані(функції), типу так:<br><br>
	<img src="https://github.com/UCUgllekk/mylife_myrules/assets/61622309/e5cc5c34-01f1-44f0-b0a2-2a24b9870743" height='400'><br>
* Це основна функція, яка відповідає за події протягом дня:<br><br>
	<img src="https://github.com/UCUgllekk/mylife_myrules/assets/61622309/7f2f0cfc-9c3f-43b0-88c9-9ec9d5c52926" height="200">
- FSM клас, в якому прописаний спеціальний метод ```pop()```, котрий видаляє перший елемент з черги і одразу ж запускає функцію, також є функція ```add_event()``` котра додає подію, тобто стан, в чергу.<br><br>
	<img src="https://github.com/UCUgllekk/mylife_myrules/assets/61622309/7872c458-3f1d-4da9-8388-3543d83da3b1" height="400"><br>
## Діаграма
<img src="https://github.com/UCUgllekk/mylife_myrules/assets/61622309/85ef0cdf-7aad-4d81-a9d6-785a2facfb6e"><br>
