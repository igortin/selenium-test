##How to Selenium

1. Create tests.py

2. Open python3 console

3. Command
```bash
	form tests import *
```
4. Command to specify URI
```bash
	uri = file_uri("counter.html")
```

5. Command open programmatically URI, driver is Selenium
```bash
	driver.get(uri)
```
6. Command show Title web page
```bash
	drivaer.title
```
7. Command show html src page
```bash
	driver.page_source
```
8. Command to simulate user behavior
```bash
	inc = drivaer.find_element_by_id("inc") 
	# create variable increase ans store element with id="increase" 

	# clock on button
	inc.click()

	for i in range(5):
           increase.click()

	dec = driver.find_element_by_id("dec")
	for i in range(5):
	   dec.click()
```