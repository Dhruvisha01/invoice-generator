# invoice-generator
A python project to automate invoice generation

Integrating google sheets - 

The first step is to create a project on https://console.cloud.google.com/ wherein you will integrate the API's required for your project.
Once you create a new project you have to enable the following API's -
1) Google drive 
2) Google sheets

Once you add the google drive API it will ask you to create credentials. Follow the steps and you should see a JSON file gets downloaded. Save this file.
Open up the json file that was downloaded earlier and find the client email. Copy the email and share your google sheet with that email address.
Next we install 2 modules - gspread and oauth2client
To do this enter 'pip install gspread oauth2client' in your command prompt/terminal
Next place the JSON file in the same directory as your python file and write your code

Writing on the image - 

The first step is to install the library needed for this -
So we write this in your command prompt or terminal - ' pip install pillow '
This is all we need for editing our image. The next step is to follow the code


