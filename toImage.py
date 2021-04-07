import csv
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import StringIO
#F7765A
#09C12B
#C8D114
#CE4BAA
with open('./test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            font  =  ImageFont.truetype ( 'arial.ttf', 42 )
            im  =  Image.new ( "RGB", (1028,1028), '#09C12B' )
            draw  =  ImageDraw.Draw ( im )
            text_x, text_y = font.getsize(row[1])
            x = (1028 - text_x)/5
            y = (1028 - text_y)/5
            draw.text ( (x,y), 'School : ' + row[1], font=font, fill='blue' )
            draw.text ( (x,y+70), 'Class : ' + row[2], font=font, fill='blue' )
            draw.text ( (x,y+150), 'StudentName : ' + row[4] + ' ' + row[5], font=font, fill='blue' )
            draw.text ( (x,y+220), 'Username : ' + row[3], font=font, fill='white' )
            draw.text ( (x,y+290), 'Password : ' + row[6], font=font, fill='white' )

            draw.text ( (x,y+390), 'Some footer text', font=font, fill='black' )
            im.save ( "./" + row[0] +"_credentials.jpg", format="JPEG" )
            line_count += 1
    print(f'Processed {line_count} lines.')


