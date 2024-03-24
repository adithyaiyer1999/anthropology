import smtplib
from email.mime.text import MIMEText

subject = "Here's your summary of your hardwork today!"
# body = "This is the body of the text message"
sender = "aibarcaboy@gmail.com"
recipients = ["adithyaiyer1999@gmail.com", "srushtipawar12@gmail.com"]
password = "<PASSCODE>"


# Construct the complete HTML email
def insert_article(article_html,news_letter_title,nomic_url):
    text_to_send = f"""
    <html>
    <head>
      <style>
        /* Add your CSS styles here */
        body {{
          font-family: Arial, sans-serif;
          line-height: 1.6;
          margin: 0;
          padding: 0;
        }}
        .container {{
          max-width: 800px;
          margin: 20px auto;
          padding: 0 20px;
        }}
        h1, h2, h3 {{
          color: #333;
        }}
        p {{
          margin-bottom: 20px;
        }}
        .article {{
          margin-bottom: 40px;
        }}
        .article h2 {{
          color: #007bff;
        }}
      </style>
    </head>
    <body>
    
    <div class="container">
      <h1>{news_letter_title}</h1>

    {article_html}
    
     <h3>Visit your work knowledge graph:{nomic_url}</h3> 
    </div>
    </body>
    </html>
    """

    return text_to_send
import re
def generate_bullet_points(text):
    lines = text.split('\n')
    html_bullet_points = "<ul>"
    for line in lines:
        line = line.strip()
        if line.startswith('-') or re.match(r'^\d+\)', line):  # Check if line starts with '-' or numbered bullet point pattern
            html_bullet_points += f"<li>{line.strip('-1234567890) ')}</li>"  # Strip bullet point markers
        else:
            html_bullet_points += line  # Add line as it is
    html_bullet_points += "</ul>"
    return html_bullet_points

from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")


def send_email(text_summaries, nomic_url): #
    article_html = ""
    for key, value in text_summaries.items():
        bullet_points = generate_bullet_points(value)
        article_html += f"""
      <div class="article">
        <h2>{key}</h2>
        <p>{bullet_points}</p>
      </div>
    """
    emoji_html = "&#x1F601;"  # Unicode representation of the smiling face emoji
    html_with_emoji = f"{current_date} Here's all the websites you visited! {emoji_html}"
    msg = MIMEText(insert_article(article_html,html_with_emoji,nomic_url),'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


#send_email(text_to_send)