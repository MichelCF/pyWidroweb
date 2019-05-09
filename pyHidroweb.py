# -*- coding: utf-8 -*-
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

home = os.path.expanduser('~')

def wait_load_items(driver, xpath):

	waiting_time = 0
	find_element = 0 
	while not(find_element): 
		try:
			driver.find_element_by_xpath(xpath)
			find_element = 1 
		except:
			print(waiting_time, xpath)
			time.sleep(1)
			waiting_time += 1
		if waiting_time == 300:
			print('Tempo de espera excedito. Processo encerrado.')
			exit()

def click_css_selector(driver, css_selector):
	waiting_time = 0
	find_element_css = 0
	while not(find_element_css):
		try:
			driver.find_element_by_css_selector(css_selector).click()
			find_element_css = 1
		except:
			time.sleep(1)
			waiting_time += 1

		if waiting_time == 300:
			print('Tempo de espera excedido.')
			break

def download_hidroweb(id_station, dir_out = 'Downloads', time_close_browser = 5):


    # display = Display(visible=0, size=(800,600))
    # display.start()

    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.dir",dir_out)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream")
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.manager.focusWhenStarting", False)  
    fp.set_preference("browser.download.useDownloadDir", True)
    fp.set_preference("browser.helperApps.alwaysAsk.force", False)
    fp.set_preference("browser.download.manager.alertOnEXEOpen", False)
    fp.set_preference("browser.download.manager.closeWhenDone", True)
    fp.set_preference("browser.download.manager.showAlertOnComplete", False)
    fp.set_preference("browser.download.manager.useWindow", False)
    fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
    fp.set_preference("pdfjs.disabled", True)

    driver = webdriver.Firefox(firefox_profile=fp)
    url = 'http://www.snirh.gov.br/hidroweb/publico/apresentacao.jsf'
    driver.get(url)
    time.sleep(1)
    driver.get(url)
    waiting_time = 0
    find_element = 0
    while  not(find_element):
        try:
            driver.find_element_by_link_text('Séries Históricas').click()
            find_element = 1
        except:
            time.sleep(1)
            waiting_time += 1
        if waiting_time == 300:
            print('Tempo de espera excedido. Processo encerrado.')
            exit()
	
    wait_load_items(driver, '//*[@id="form:fsListaEstacoes:codigoEstacao"]')
    driver.find_element_by_xpath('//*[@id="form:fsListaEstacoes:codigoEstacao"]').send_keys([id_station, Keys.ENTER])
    click_css_selector(driver, '#form\\:fsListaEstacoes\\:bt')
    wait_load_items(driver, '//div[contains(@class, "checkbox i-checks")]')
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//div[contains(@class, "checkbox i-checks")]').click()
        click_css_selector(driver, '#form\\:fsListaEstacoes\\:fsListaEstacoesC\\:radTipoArquivo-componente > div:nth-child(2) > div:nth-child(2)')
        click_css_selector(driver, '#form\\:fsListaEstacoes\\:fsListaEstacoesC\\:btBaixar')
    except Exception as e:
        print(e)
		
    time.sleep(time_close_browser) #espera 5 segundos para termina o download
    driver.quit()


