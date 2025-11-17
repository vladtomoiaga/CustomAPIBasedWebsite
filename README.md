# Introduction
### Custom API Based Website

- This simple project fetches exchange data from an external API and displays it in an HTML table.
- Users are required to create an account on the API provider's website in order to receive an `access_key`.
- After viewing company data, users can click a hyperlink to generate an interactive graph of the selected company

## Index

- [About the project](#about-the-project)
  - [Built with](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)


<!-- ABOUT THE PROJECT -->
## About the project

This small web app connects to the Marketstack API to retrieve financial data, which is displayed in a table on the homepage.
Each company has a detail page where users can see more information and click a hyperlink to generate an interactive Plotly graph of the stock history.

It demonstrates a simple way to integrate third-party APIs with a Flask-based web application.


### Built with

In this section you will find the important technologies for this project.

* Python
* Flask
* Bootstrap 5
* Pandas
* Plotly



<!-- GETTING STARTED -->
## Getting Started

### Installation

Below is how you can install and setting up the website.


1. Clone the repo
   ```sh
   git clone https://github.com/vladtomoiaga/CustomAPIBasedWebsite.git
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage

* Start the Flask server
* Open your browser at http://127.0.0.1:5000
* The homepage displays stock data in a table
* Click on a company to go to its detail page
* On the detail page, click the hyperlink to generate and view the company’s interactive Plotly graph
* Make sure you have a valid API `access_key` configured
* The data is fetched live from the exchange API (https://api.marketstack.com)
