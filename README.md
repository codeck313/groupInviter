# groupInviter
To send mass message (like group invitation) over on WhatsApp using Chromium Driver

##  Setup
Install the stuff:

    pip install selenium
    sudo apt-get install chromium-browser

Get the chromium driver for your version of chromium browser from [here](https://chromedriver.chromium.org/) or you can try using the one along with the repo.

Supposing we have a `get-your-own.csv` file in the following format 
| Name | Email Id | Phone Number |
|--|--|--|
| Something | Better@than.nothing.com | 3141592653 |
| Nice | Looking@table.com  |  7785522548 |

    dataBaseName = 'get-your-own.csv'
    nameRow = 0
    numberRow = 2

To send a message like this
![image](https://user-images.githubusercontent.com/23121752/124000076-d8f14100-d9f0-11eb-8375-1b20bb8411d6.png)
Enter the following changes in the script:

 - Msg1 and Msg2 are in 2 different lines.
      
   
        msg1 = "I am"
        msg2 = "Lazy"
    
 - Increase the delay time  between the page being loaded and the text
   being entered (do this if the text is not getting entered properly.  
   ` delayTime = 15`

## Troubleshooting

 - In case things get broken check the chat's text box tag like this 
   
   ![Screenshot from 2021-06-30
   22-25-55](https://user-images.githubusercontent.com/23121752/124001512-55385400-d9f2-11eb-8d7c-b5053ffed5b1.png)
   and replace it in this line's class name
   
       msg_box = driver.find_element_by_class_name('_2A8P4')
       
 - You might need to change the send button tag as well  ![Screenshot
   from 2021-06-30
   22-29-25](https://user-images.githubusercontent.com/23121752/124001871-b7915480-d9f2-11eb-8cbf-7678157d147e.png)
   
   `<button
   class="_1E0Oz"><span data-testid="send" data-icon="send"
   class="">...</button>`
   
   and replace it here
   
   `driver.find_element_by_class_name('_1E0Oz').click()`

