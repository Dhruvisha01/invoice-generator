# import gspread to open a spreadsheet by title,key or URL and make changes in it
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import pillow library to edit the image using python
from PIL import Image, ImageFont, ImageDraw
#import smtplib for sending mail using the smtp server
import smtplib
#importing imghdr for attaching the image files
import imghdr
# for sending mails
from email.message import EmailMessage


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) # add your json file here and refer to the above variable

client = gspread.authorize(creds)

sheet = client.open("Dummy_Datasheet").sheet1  # Open the spreadsheet named Dummy_Datasheet. In case of multiple sheets write sheet2, sheet3

data = sheet.get_all_records()  # Get a list of all records

length = len(data)# gives the number of items in the sheet
i = 1
#Get the various fonts required to write on your image in the same directory as your python file
title_font1 = ImageFont.truetype('futura.ttf', 27)
title_font2 = ImageFont.truetype('arial.ttf', 23)
title_font3 = ImageFont.truetype('arial.ttf', 25)
title_font4 = ImageFont.truetype('arial.ttf', 27)
title_font5 = ImageFont.truetype('arialbd.ttf', 27)
title_font6 = ImageFont.truetype('arialbd.ttf', 23)

# Getting the data from the sheet
while i <= length:
    my_image = Image.open("invoice-real.png") # pass the image name that you wish edit
    row = sheet.row_values(i + 1) # getting the complete row's value in the form of a list
    # storing each and every element of the row in a different variable
    identity = row[3]
    name = row[4]
    email_id = row[5]
    address1 = str(row[7])
    address2 = str(row[8])
    pincode = row[9]
    description = row[10]
    price = row[11]
    contact = row[12]
    amount = price
    amount_paid = price
    date = '10th January, 2021'
    total = price
    mode = 'Online/Gpay'

    image_editable = ImageDraw.Draw(my_image) # Use this function to draw on the image you passed earlier
    # writing the data imported earlier on to the image at the various coordinates
    # parameters passed are (x,y) coordinates with top right being (0,0) , data, and the font
    image_editable.text((759, 222), name, (0, 0, 0), font=title_font1)
    image_editable.text((759, 258), email_id, (0, 0, 0), font=title_font2)
    image_editable.text((759, 290), address1, (0, 0, 0), font=title_font2)
    image_editable.text((759, 320), address2, (0, 0, 0), font=title_font2)
    image_editable.text((759, 351), pincode, (0, 0, 0), font=title_font2)
    image_editable.text((759, 376), 'Phone: ' + str(contact), (0, 0, 0), font=title_font2)
    image_editable.text((152, 487), identity, (0, 0, 0), font=title_font4)
    image_editable.text((152, 515), date, (0, 0, 0), font=title_font4)
    image_editable.text((70, 701), description, (0, 0, 0), font=title_font4)
    image_editable.text((700, 701), price, (0, 0, 0), font=title_font4)
    image_editable.text((970, 701), amount, (0, 0, 0), font=title_font4)
    image_editable.text((980, 896), total, (0, 0, 0), font=title_font3)
    image_editable.text((970, 933), amount_paid, (0, 0, 0), font=title_font5)
    image_editable.text((297, 1066), mode, (0, 0, 0), font=title_font6)

    my_image.save(name + ".png") # saving the image individually with each person's name
    print(i)

    # sending the mail

    msg = EmailMessage()
    msg['Subject'] = 'TEST MAIL'
    msg['From'] = 'Your email id here'
    msg['To'] = email_id # email id imported above from the sheet
    msg.set_content('Testing')

    files = [name + ".png"]

    # selecting the file name with each individual person's name for attaching in the mail

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # enter parameters based on your mail - this is for gmail
        smtp.login('Your email id here', 'Your password')
        smtp.send_message(msg)
    i = i+1

