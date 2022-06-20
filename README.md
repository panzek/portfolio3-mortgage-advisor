# Mortgage Advisor

* **Introduction**

**Mortgage Advisor** is a mortgage calculator application for first time buyers of housing property in Ireland. This application has relied on the information and data provided by the Central Bank of Ireland in its overview of the new Mortgage lending in Ireland for half of 2021 (H12021), particularly in the areas of the interest rate and Loan to Value limit.

The Central Bank of Ireland’s mortgage lending measures were introduced in February 2015. “The measures set limits on the size of mortgages that consumers can borrow through the use of loan-to-value (LTV) and loan-to-income (LTI) limits.” Loan to Value (LTV) is the percentage of the property’s value that a buyer can borrow and how much of it that would have to be paid upfront in the form of a deposit. And Loan to Income (LTI) is the limit the maximum amount someone buyers can borrow to 3.5 times their annual income. 

* **The Goal of the Quiz**

**The goal of this application** is to calculate the mortgage and provide the first-time buyer (the user) an estimate of the monthly mortgage repayment, based on the data provided by the user: Price of the property, Loan Amount, and the number of years for the loan repayment. The mortgage calculator is a basic app, interactive, and easy to use. However, it is for illustrative purposes only. The application runs in a Command Line Interface and is deployed through Heroku.

![Mortgage Advisor Mockup](doc/images/)

[View Live Project Here](https://mortgage-advisor.herokuapp.com/)

## Table of Contents

1. [UX - User Experience Design](#UX-user-experience-design)
    * [User Stories](#user-stories)
    * [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Wireframes](#wireframes)
    * [Flowchart](#flowchart)

2. [Features](#features)
    * [Existing features](#existing-features)
      * [Username](#username)
      * [About the application](#about-the-application)
      * [Mortgage Calculator](#mortgage-calculator)
      * [Retrieve Mortgage Calculator Results](#retrieve-mortgage-calculator-results)
      * [Delete Mortgage Calculator Results](#delete-mortgage-calculator-results)
      * [Exit the Application](#exit-the-application)
    * [Features to be implemented](#features-to-be-implemented)
  
3. [Data Model](#data-model)

4. [Technology Stack](#technology-stack)
    * [Languages Used](#languages-used)
    * [Python Libraries](#python-libraries)
    * [VSCode Extensions Used](#vscode-extensions-used)

5. [Testing](#testing)
    * [PEP8 Testing](#pep8-testing)
    * [Validator Testing](#validator-testing)
    * [Accessibility Testing](#accessibility-testing)

6. [Clone](#clone)
7. [Deployment](#deployment)
8. [Credits](#credits)
    * [Acknowledgements](#acknowledgements)

## User Experience (UX)

### User Stories

#### A new user

* As a new user, I want to be able to choose a name unique to me with which to store the results of my mortgage calculation.
  * It is a requirement that all new users of the application should create a username. And on entering a username, the application will first check if the username is in the database. If username is not found, the username entered by the user will be created automatically to enable the user proceed further.
* As a new user, I want to get different options on how to use the application.
  * The application provides a new user with 3 different options: the first option is the choice to “Run an overview of this application”. This gives a quick run down of what the application is all about and how to use it. The second option is the choice to run the mortgage calculator to calculate the monthly mortgage repayment. And the third and last option is the choice to exit the programme. All three options are independent so a user may select an option in no particular order.
* As a new user, I want to be able to run the mortgage calculator to know the estimate of my monthly repayment based on the amount I will borrow to get a mortgage.
  * The application is a mortgage calculator for first time buyers (FTB) only. The application collects only 3 data from the FTB for its calculation: Property price, Loan Amount, and number of years for the loan. The mortgage calculator is a basic app, interactive, and easy to use.
* As a new user, I want to be able to exit the program should I decide not to use it.
  * On signing into the Mortgage Advisor application, the new user is presented with 3 “new user” options. One of this options is the option to exit the program. At this “option” stage, the user name entered by the new user has been created but has not been stored. So on choosing to quit the programme, the username will automatically be removed, and will be available to be registered by the new user on return visit or by any other new user.

#### A returning/existing user

* As a returning user, I want to be able to access and retrieve my previous mortgage calculation results using my user name.
  * A returning user can access the application using their previously created username, as all usernames are stored in the spreadsheet. Previous mortgage results are also accessible to only the returning user. A returning user may choose to only access the results or delete it.
* As a returning user, I want to be able to delete my saved previous mortgage calculator results and perhaps run another mortgage calculator.
  * Returning users may choose to delete their previous saved mortgage calculator results. It is one of the options in the existing user menu list.
* As a returning user, I want to be able to exit the programme successfully at anytime.
  * The programme provides a function that enables the returning user to exit the programme. There are 3 options for a returning user immediately the user logs in. And one these three options is the option (option 3) to exit the programme.

### Design

* Color Scheme
  * The colors used in the terminal are Green color, Red color, Yellow, and Cyan.
  * These are colors provided by colorama package within python and using ASNI code to apply the colors to the terminal text

* Wireframes
  * The wireframe was created using [Balsamiq](https://balsamiq.com/). And it was designed for desktop only.

    ![Desktop - Wireframe](flowchart/mortgage_advisor_wireframe.png/)

* Flowchart
  * The flowchart was created using [Diagram.net](https://www.diagrams.net/).  

    ![Desktop - flowchart](flowchart/mortgage-advisor-flowchart.jpg/)

## Features

* **Username**
  * The Mortgage Calculator provides that all users of the application must create a username (if a new user) or enter a user name (if a returning user) to be able to use the app. It also specifies that the user name should be between 4 to 10 characters, following the the standard minimum and maximum length of a user name. It also specifies that letters, numbers, and spaces are allowed. And the username when created is stored in the database (spreadsheet). The app is configured in such a way that no two different users will have the same username.

    The username feature is configured to handle different errors:
    1. When the user did not enter any value it raises an exception with a message, “You must enter a username, please try again” with a prompt to try again.
    2. When the value entered by the user is outside the range between 4 and 10 characters, it raises an exception with a message: “Username must have at least 4 characters, please try again”.
    3. When the characters entered by the user are more than 10 characters or less than 4 characters, it raises an exception with a message.

        ![Username](doc/images/username.png)

* **About the application**:
  * The “About the application” outlines a general description of the application: what the application does and how to use it.
  * The app is for first time buyers (FTB) only and provides the user an estimate of their monthly repayment. Part of the general description is also the type of data that will be collected from the user: the amount the user will borrow, the interest rate fixed by the lending institution, and number of years for the loan. It is important that a new user knows what the Application does and how to use before proceeding further with the application. And the application is carefully configured to meet these demands. But then, the user is left with the choice not to select this first option, but to select the second which is the mortgage calculation or the third option, which is to exit the application.

    ![About the application](doc/images/)

* **Mortgage Calculator**:
  * Mortgage Calculator is the main feature of Mortgage Advisor application. It is a mortgage calculator for a First Time Buyer (FTB) only. It is here that the monthly repayment is calculated. And to effectively make the calculator it collects data from the user with three (3) inputs: Price of the property the user wants to buy, the amount the lending institution wants to lend to the user (buyer) and the number of years for the loan to be repaid.

  * The application is basic but robust enough to validate the values entered in the inputs by the user:

      1. Where the mortgage amount exceeds 90% of the purchase prices, the application throws an error. The 90% LTV limit is the standard requirement for first-time buyers of a house or apartment in Ireland. They can take out up to 90% of the purchase price and would have to make at least a 10% deposit.
      2. When the user enter a term loan that exceeds or is below the specified loan tenure range between 5 and 35 years, it throws exception. I pegged this loan tenure range only to demonstrate further the application ability to handle exceptions.
      3. Where the value entered by the user is a string and an empty string, it also catches the error.  

         * The error messages in this feature and indeed all error messages in this Mortgage Advisor application are highlighted in red colour.
         * When user entries have passed through these stringent validation processes successfully, the application outputs the results to the user, and stores the results with the user name in the (database) spreadsheet.
         * Also returned with the result, but not stored in the spreadsheet is the Loan to Value (LTV) which was calculated by the application based on the price of property and the loan amount entered by the user. A loan to value being the amount the user (property buyer) borrowed as a percentage of the price of the property.
         * The Mortgage Calculator Results is marked with a Disclaimer that the mortgage calculator is for illustrative purposes only.

      ![Mortgage Calculator](doc/images/mortgage_calculator_results.png)

* **Retrieve Mortgage Calculator Results**
  * Returning users can retrieve any previous mortgage calculator results stored in their name. It is a simple and quick process. Retrieve Mortgage Calculator results is the first option (option 1) in the existing user menu list, and on selection the results are retrieved from the database and displayed to the user to view. The returning user can then press any key to return to the existing user option section to choose the option to delete the results or the option to exit the program.

      ![Retrieve Mortgage Calculator Results](doc/images/retrieve_mortgage_calculator_results.png)

* **Delete Mortgage Calculator Results**
  * Returning users may choose to delete their previous saved mortgage calculator results. Delete Mortgage Calculator results is the second option (option 2) in the existing user menu list. On selection, delete saved mortgage calculator results, the saved results and the username are deleted. On pressing any key, the user is returned to the Welcome page as a new user.

      ![Delete Mortgage Calculator Results](doc/images/)

* **Exit the Application**
  * Exit the Application is the third option (option 3) in both the existing user and new user menu lists. When selected, the user is exited from the application with a good bye message.

      ![Exit the Application](doc/images/returning_user_exit.png)

### Features to be implemented

* The application serves its full purpose as a basic Mortgage Calculator with its main focus on the First-time buyers. However, for future improvement of the application, I intend to implement an additional feature for the calculation of the monthly mortgage repayment for a Second and Subsequent Buyer (SSB).
* SSBs are required to pay a deposit of at least 20% (80% LTV limit) of the property value instead of the 10% (90% LTV limit) for FTB.  

## Data Model

* There is a spreadsheet with one worksheet that contains the information of the user, who is a first-time buyer. And our worksheet has 5 columns for username, property value, loan size, loan term, and monthly repayment. All columns except the monthly repayment column will store the information collected from the user. The monthly column will store the mortgage calculator results.
* A Google Sheet was used to store users’ data which consist of the mortgage calculator results with the user name. And to access and update the data in the spreadsheet we use Google Drive and Google Sheet APIs.

    ![Spreadsheet](doc/images/mortgage_advisor-Google-Sheets.png)

* When improving this application in future, a SSB worksheet will be added to store mortgage calculator results of Second and Subsequent Buyers.

## Technology Stack

* Languages Used
  * [Python](https://www.python.org/)
  * [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
  * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * [JavaScript](https://www.javascript.com/)

* **Python Libraries**
  * [Colorama](https://pypi.org/project/colorama/)
  * [Diagram.net](https://www.diagrams.net/)
  * [Error and Exceptions Handling](https://docs.python.org/3/tutorial/errors.html)
  * [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html)
  * [gspread](https://pypi.org/project/gspread/ )
  * [PyFiglet](https://pypi.org/project/pyfiglet/0.7/)
  * [py-getch](https://github.com/joeyespo/py-getch)

* **VSCode Extensions Used**
  * [Markdown lint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - used For style checking and to maintaining standard.
  * [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) – a language support for python for writing a better code.

## Testing

* PEP8 Testing
  * [PEP8 online](http://pep8online.com/) was used to check the code for PEP8 requirements.

     ![Python code Validation Result](doc/images/)
* 
* Accessibility Testing
  * [Accessibility Insights](https://accessibilityinsights.io/) was used to check and fix accessibility issues.
  * [Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse) - used to test accessibility, and the check returned the reports below:

    * Desktop

        ![Lighthouse Report Desktop](doc/images/)

## Clone

* Clone from GitHub to VSCode:
    1. Log in to [GitHub](https://github.com/panzek/portfolio3-mortgage-advisor)
    2. Click on the code button beside the green gitpod button. 
    3. Copy the link and go to VSCode
    4. Press F1 to display the command palette. 
    5. Enter gitcl, select the Git: Clone command, press Enter
    6. When prompted for the Repository URL, enter the copied GitHub repository url, then press Enter. 
    7. Select (or create) the local directory into which you want to clone the project.
    8. Repository is now ready for development

* Environment Variable:
  * As shared in Slack community, which I used as a guide in setting mine up:
    1. Create virtual environment in the project folder - d:\workspaces>python –m venv my_project\venv 
    2. Activate the virtual environment - d:\workspaces>my_project\venv\Scripts\activate.bat 
    3. cd into new project folder - d:\workspaces>cd my_project
    4. To open in VSCode - d:\workspaces\my_project>code. (or right click the folder itself and select Open in VSCode)
    5. Open VSCode and Press CONTROL+SHIFT+P, type‘Python Interpreter’ and select it.
    6. Either select the venv environment from the list or click ‘Enter interpreter path’ and navigate to the venv folder, and proceed into Scripts and select python.exe 
    7. venv\Scripts\python.exe

## Deployment

* The website was deployed to Heroku Pages. These were the steps taken for the deployment:
    1. Log in to [Heroku](https://id.heroku.com/login)
        * Steps for deployment Creating a Heroku Account/App Create/login into a Heroku account.
        * Click "New" menu and select "Create new app"
        * Fill out the form; choosing a unique app name and region.
        * Click on "Create app"
    2. Configuration
  * Click on the settings menu
    * Add PORT to Config Vars and set its value to 8000
    * In the field for key, enter CREDS, all capital letters.
    * Go  to  your workspace (VScode or Gitpod)
    * copy the entire content of creds.json file,
    * Paste it into the value field and click “Add”.
  * Click “Add buildpack”
    * Set the buildpacks to Python and NodeJS (Be sure buildpacks are in this order)
  * Click on the Deploy section
    * Select Github Click connect to Github
    * Click “Search” to search for your Github repository name
    * Click “connect” to link up your Heroku app to your Github repository code
  * Scroll down to the bottom to choose your preferred mode of deployment:
    * Choose "Enable automatic deploys" or "Deploy Branch" to deploy manually - I chose the latter.
    * If successfully deployed, you will see the message "“App was  successfully deployed”
    * Click the "View" button to go to the terminal
    * Check that your app is up and running.

    [View Live Project Here](https://mortgage-advisor.herokuapp.com/)

## Credits

* [Code Institute](https://codeinstitute.net/) lectures and “Love Sandwiches” walkthrough project helped shape the ideas and techniques that frame this Portfolio Project 3 for Diploma the [Full Stack Software Development](https://codeinstitute.net/ie/full-stack-software-development-diploma/).
* Central Bank of Ireland's [New Mortgage Lending - Data and Commentary](https://www.centralbank.ie/financial-system/financial-stability/macro-prudential-policy/mortgage-measures/new-mortgage-lending-data-and-commentary) provided me with information and data resource that shape my idea that informed he creation of this project.
* [Colorama](https://youtu.be/u51Zjlnui4Y) - to output colored text to the terminal in Python  
* [Mark Down Guide](https://www.markdownguide.org/basic-syntax/)  
* [Print Colors in Python terminal](https://www.geeksforgeeks.org/print-colors-python-terminal/)
* [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors) -
* [Python Print Without Newline: Step-by-Step Guide](https://careerkarma.com/blog/python-print-without-new-line/)  - got the idea here on how to fix new line added to the end of the string in terminal colored text print functions.
* Text content of the Disclaimer under the mortgage calculation results was taken from [ESB](https://www.ebs.ie/mortgage-repayment-calculator)
* [Tinypng.com](https://tinypng.com/) – used to reduce the file size.
* [Stackoverflow](https://stackoverflow.com/) was a site I used extensively to find answers to some knotty coding issues. 
  
## Acknowledgements

* Another intervention. Another rescue. Thank you, [Matt Bodden](https://github.com/MattBCoding). Again, that you!
* For all the help and support, thank you [Akshat Garg](https://github.com/akshatnitd), my [Code Institute](https://github.com/Code-Institute-Org) mentor.
* To [Code Institute](https://github.com/Code-Institute-Org) Student care team for your care and understanding, always.
