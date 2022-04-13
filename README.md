# cms-scraper
A selenium-based python script to scrape my own data.

![photo_2022-04-13 19 10 45](https://user-images.githubusercontent.com/46195225/163234021-f822ec16-bbd7-4782-8ee2-2ac656cb17ed.jpeg)


Since a private dashboard didn't allow me to download a series of PDFs unless I clicked on each of them in a paginated view, I decided to scrape my data with a selenium-based python script. This is done by the `main.py`.

The downloaded files were all saved with the same name (the click action triggered an automatic download, without the dialog box opening): the `renamer.py` script parses the content of each PDF stored in the `pdf` folder, looks for a specific text using a regex and renames the file using the matched text.
