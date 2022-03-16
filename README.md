# web-scraping-challenge

Step 1 - Scraping
Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.
Save results into a Mongo Database


1.1
NASA Mars News
Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

1.2
JPL Mars Space Images - Featured Image
Visit the url for the Featured Space Image site here.
Make sure to find the image url to the full size .jpg image.
Make sure to save a complete url string for this image.

1.3
Mars Facts
Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Used Pandas to convert the data to a HTML table string.

1.4
Mars Hemispheres
Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


Step 2 - MongoDB HTML and Flask Application
Convert Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all ofscraping code from above and return one Python dictionary containing all of the scraped data.

Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
Make sure the template has a button so users can access this easily
Store the return value in Mongo as a Python dictionary.

Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Bootstrap Quartz was used but any one will do. 

Additional Notes:
Some of the code stored here is commented out. This is due to the owner's local host repeatedly causing lxml errors despite the correct installations. However, by using the original Juypter notebook to pass in values into the MongoDB database and then editing values in the database (namely turning the passed html in part 1.3 which is registered as a string in mongo to the Code type), the site works as intended. It will newly scrape information from the newest news and get new images on occassion. 
