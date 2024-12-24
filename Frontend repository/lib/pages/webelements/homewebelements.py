from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.XPATH, "//div[@class='c_neb-item-value']")
    signin_button = (By.XPATH, "(//div[@class='mc6t-main-content']//div[@tabindex='0'])[3]")
    search_button = (By.XPATH, "//input[@data-test-destination]")
    name_tag_input = (By.XPATH, "//div[@class='c_neb-item-value']")
    name_dropdown_column_input = (By.XPATH, "//input[@aria-label='Destino']")
    search_tag_input = (By.XPATH, "//button[@type='submit']")
    cancel_button = (By.XPATH, "//div[@aria-label='Remove value']")
    create_column_disabled_button = (By.XPATH, "//div[@aria-haspopup='listbox']")
    #menu paths
    main_navigation_button = (By.XPATH, "//div[@class='mc6t-nav-button']/div")
    flights_button = (By.XPATH, "//ul[@class='HtHs-nav-list']//a[@href='/flights']")
    stays_button = (By.XPATH, "//ul[@class='HtHs-nav-list']//a[@href='/stays']")
    cars_button = (By.XPATH, "//ul[@class='HtHs-nav-list']//a[@href='/cars']")
    explore_button = (By.XPATH, "(//ul[@class='HtHs-nav-list']//a)[4]")
    news_button = (By.XPATH, "(//ul[@class='HtHs-nav-list']//a)[5]")
    direct_button = (By.XPATH, "(//ul[@class='HtHs-nav-list']//a)[6]")
    the_best_moment_button = (By.XPATH, "(//ul[@class='HtHs-nav-list']//a)[7]")
    business_button = (By.XPATH, "(//ul[@class='HtHs-nav-list']//a)[8]")
    trip_button = (By.XPATH, "(//div[@class='pRB0-nav-items'])[3]//a")


    language_button = (By.XPATH, "(//div[@class='pRB0-nav-items'])[4]/div[1]")
    currency_button = (By.XPATH, "(//div[@class='pRB0-nav-items'])[4]/div[2]")

    area_expanded_button = (By.XPATH, "//div[@aria-expanded]//div[@class='c-ulo-content']")
    exit_button = (By.XPATH, "//button[@aria-disabled]//div[@class='Py0r-button-container']")