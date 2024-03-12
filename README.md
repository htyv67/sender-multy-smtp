# Overview

The Bulk Send Randomizer is a Python script designed for efficiently sending bulk emails to a recipient list by employing randomized parameters such as SMTP servers, subjects, messages, links, names , proxys and headers. This script ensures a diverse and randomized approach to email delivery, enhancing the chances of successful delivery while bypassing spam filters.

Utilizing randomized elements in crucial aspects of email composition, this script allows for a dynamic and versatile approach to mass email sending. The randomization helps increase the likelihood of bypassing spam filters, optimizing the delivery of emails to intended recipients.


## Features:

- **Enhanced Email Spam Bypass**:
  - Utilizes randomized SMTP server, subject, message, name, link, and proxies to increase the likelihood of bypassing spam filters.

- **Flexible Sending Modes**:
  - Offers two sending modes:
    - **Slow Mode**:
      - *Description*: Allows for a slower email delivery pace, incorporating a specified delay between each email.
      - *Usage*: Ideal for controlled delivery, reducing server load, and avoiding detection.
    
    - **Fast Mode**:
      - *Description*: Utilizes multiple threads for fast email dispatch, allowing choice between 'random' or 'sequential' sending orders.
      - *Random Order*: Provides diversity by sending emails randomly.
      - *Sequential Order*: Sends emails in a structured, sequential manner.
    
- **HTML Template Customization**:
  - Enables extensive customization of email content by modifying or replacing HTML templates within the `templates` folder. Users can add multiple HTML templates, allowing for varied and distinct emails tailored to different recipients. This ensures versatile and personalized email content creation and dispatch, supporting simultaneous distribution of various email types.
  - Utilizes tags within the subject and message, enabling personalized emails for each recipient.

- **Additional Headers**:
  - Enables users to define special email headers using the `headers.txt` file.
  
- **Proxy Support**:
  - Introduces `proxys.txt` for including a list of proxies, enhancing anonymity and varied sender information.

- **HTML Crypter**:
  - Enhances email content customization with three Python scripts—`crypter1.py`, `crypter2.py`, and `crypter3.py`— each employing distinct algorithms to generate randomized HTML templates.



## Installation:

To set up the necessary libraries, run the following command in your terminal:


pip install -r requirements.txt



## Script Usage:

1. **Update Configuration Files**:

   - Update the following files in the `settings` folder:
     

	- `settings/emails.txt`: Ensure each email address is listed on a separate line without any additional characters or spaces:
		john@example.com
		sarah@example.com

	- `settings/smtps.txt`: List SMTP servers in the format: host|port|user|passwd for each server on separate lines:
		smtp1.example.com|587|user1|password1
		smtp2.example.com|465|user2|password2

	- `settings/subjects.txt`: List subject lines for the emails on separate lines, you can use tags in the subject:
		Special Offer Inside!
		Your Exclusive Invitation ID:##random_number##

	- `settings/froms.txt`: Provide sender email addresses/names in the format: Sender Name sender@example.com :
		John Doe <john@example.com>
		Sarah Smith <sarah@example.com>

	- `settings/links.txt`: List links to include in the emails, each on a separate line.
		https://example.com/promo
		https://example.com/discount

	- `settings/proxys.txt`: List proxies in the format: host|port|user|passwd for each proxy on separate lines.
		proxy1.example.com|8080|username1|password1
		proxy2.example.com|3128|username2|password2

	- `settings/headers.txt`: Define custom email headers in each line following the standard header format.
		X-Custom-Header: Value
		Reply-To: reply@example.com

	Ensure the content in each file follows the specified format for proper functionality within the Bulk Sender Randomizer script.


2. **Customize HTML Templates**:
   - Modify or replace HTML files in the `templates` folder to create the content of the emails sent. Ensure tags (like ##email##, ##name##, etc.) are appropriately used for personalization.

3. **Run the Script**:
   - Execute the command: `python3 bulk_send_randomizer.py`
   - The script will prompt for the preferred sending mode:
     - For **Slow Mode**, enter 'slow' and provide the delay time between sending emails (in seconds).
     - For **Fast Mode**, enter 'fast'.
       - Subsequently, choose the sending order:
         - For *Random Order*, enter 'random'.
         - For *Sequential Order*, enter 'sequential'.

### Crypters Usage:

1. **Select a Crypter**:
   - Choose one of the available Python scripts (`crypter1.py`, `crypter2.py`, or `crypter3.py`).
   
2. **Run the Selected Crypter**:
   - Execute the chosen script in your terminal.
   - Input the uncrypted letter or template to generate a randomized HTML template based on the specified algorithm.
   
3. **Obtain Crypted HTML**:
   - Each crypter employs its algorithm to produce multiple randomized HTML templates.
   - Utilize the generated crypted HTML templates for personalized and varied email content within the Bulk Send Randomizer script.


## Tags:

| Tag                 | Example                  | Description                                      |
|---------------------|--------------------------|--------------------------------------------------|
| `##email##`         | `john.smith@example.com` | Email address of the user.                       |
| `##name##`          | `John Smith`             | Name of the user.                                |
| `##link##`          | `random_link`            | A random link from `links.txt`.                  |
| `##random_number##` | `2545572`                | A randomly generated number.                     |
| `##random_string##` | `8qg3qh3`                | A randomly generated string of characters.       |
| `##time##`          | `09:45:25`               | The current time.                                |
| `##date##`          | `2024-01-01`             | The current date.                                |
| `##date&time##`     | `2024-01-01 09:45:25`    | The current date and time.                       |


## Note:

    * Use this script at your own risk.
    Sending unsolicited emails is illegal in some countries, make sure to comply with the laws of your country before using this script.
    The script is for educational and testing purposes only, use it responsibly.

    * If you require additional features or customization for this script, please do not hesitate to contact us. Our team is available to assist you in finding the best solution for your specific needs. Whether you need help with installation, configuration or further development, we are here to help. Please reach out to us via telegram @zanzanmax and we will be happy to assist you

## Author:
[@zanzanmax] - The author of the script

Copyright [2024] - Licensed under the [BSD License]