from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button')  # Войти в аккаунт
    REGISTER_LINK = (By.XPATH, '//a[@href="/register"]')  # Зарегистрироваться
    NAME_FIELD = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]/div//input')  # Поле имя в форме регистрации
    EMAIL_FIELD = (By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]/div//input')  # Поле эмейл в форме регистрации
    PASSWORD_FIELD = (By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][3]/div//input')  # Поле пароль в форме регистрации
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Зарегистрироваться кнопка в форме регистрации
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # Кнопка входа в форме входа
    ENTRANCE_TITLE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок Вход
    INCORRECT_PASSWORD_HINT = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Подсказка о неправильном пароле
    PLACE_AN_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка оформить заказ
    EMAIL_FIELD_SIGH_IN = (By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]/div//input')  # Поле эмейл в форме входа
    PASSWORD_FIELD_SIGH_IN = (By.XPATH, './/fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]/div//input')  # Поле парое в форме входа
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # Кнопка личный кабинет
    ENTER_TITLE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок вход
    PERSONAL_NAME_FIELD = (By.XPATH, '//input[@name="Name"]')  # Поле имя в лк
    PERSONAL_LOGIN_FIELD = (By.XPATH, '//input[@name="name" and @type="text"]')  # Поле логин в лк
    PERSONAL_PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')  # Поле пароль в лк
    ENTER_LINK = (By.XPATH, '//a[@href="/login"]')  # Кнопка войти в форме регистрации
    RECOVERY_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')  # Восстановить пароль линк
    PERSONAL_ACCOUNT_LINK = (By.XPATH, '//a[@href="/account"]')  # Ссылка персональный аккаунт
    PROFILE_SIDEBAR = (By.XPATH, '//ul[@class="Account_list__3KQQf mb-20"]')  # Сайдбар в лк
    PERSONAL_ACCOUNT_HINT = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]')  # Подсказка в лк
    ASSEMBLE_A_BURGER_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')  # Подсказка в лк
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/account/profile"]') # Кнопка профиля
    CONSTRUCTION_BUTTON = (By.XPATH, '//a[@href="/" and @class="AppHeader_header__link__3D_hX"]') # Кнопка конструктор
    STELLAR_BURGERS_BUTTON = (By.XPATH, '//a[@href="/" and not(@class="AppHeader_header__link__3D_hX")]') # Кнопка стеллар бургер
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Кнопка выход
    NEW_USER_HINT = (By.XPATH, '//p[@class="undefined text text_type_main-default text_color_inactive mb-4"]') # Информация для нового пользователя
    FILLINGS_SECTION_BUTTON = (By.XPATH, '//div[@style="display: flex;"]/div[3]') # Кнопка начинки
    FILLINGS_TITLE = (By.XPATH, '//h2[text()="Начинки"]') # Начинки заголовок
    SAUCES_SECTION_BUTTON = (By.XPATH, '//div[@style="display: flex;"]/div[2]') # Кнопка соусы
    SAUCES_TITLE = (By.XPATH, '//h2[text()="Соусы"]')  # Соусы заголовок
    BUNS_SECTION_BUTTON = (By.XPATH, '//div[@style="display: flex;"]/div[1]') # Кнопка булочки
    BUNS_TITLE = (By.XPATH, '//h2[text()="Булки"]') # Булочки заголвок
