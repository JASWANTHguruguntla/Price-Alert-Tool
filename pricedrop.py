import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import re

def get_price(url):
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Cache-Control': 'max-age=0'
        })
        soup = BeautifulSoup(response.content, 'html.parser')

        price_element = soup.select_one('.a-price-whole') #amazon
        # price_element = soup.select_one('.Nx9bqj CxhGGd') #flipkart

        if price_element:
            price_text = price_element.text.strip()
            price_number = re.findall(r'[\d,]+', price_text)
            if price_number:
                price = float(price_number[0].replace(',', ''))
                return price
        return None
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def send_email(subject, body, to_email, from_email, from_password):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def track_price(url, target_price, check_interval, to_email, from_email, from_password):
    while True:
        current_price = get_price(url)
        if current_price is not None:
            print(f"Current Price: ₹{current_price}")
            if current_price <= target_price:
                subject = "Product Price Dropped!"
                body = f"The price dropped to ₹{current_price}!\nThis is below your target price of ₹{target_price}.\nCheck the product here: {url}"
                send_email(subject, body, to_email, from_email, from_password)
                break
            else:
                print("Price not yet low enough, checking again later.")
        else:
            print("Could not retrieve the current price, will try again.")

        time.sleep(check_interval)

if __name__ == "__main__":
    url = "https://www.amazon.in/ASUS-Vivobook-14-inch-Windows-E1404FA-NK521WS/dp/B0BVMM9CW5/?_encoding=UTF8&pd_rd_w=XCND0&content-id=amzn1.sym.2c27e899-f178-4798-841c-1b75fe8abb18&pf_rd_p=2c27e899-f178-4798-841c-1b75fe8abb18&pf_rd_r=QTRJ7GZ79G8MAJNY3FQ2&pd_rd_wg=p5zB8&pd_rd_r=3dd2dfdc-8eed-4fa1-b996-366b48954f99&ref_=pd_hp_d_atf_dealz_cs"
    target_price = 34990
    check_interval = 3600

    from_email = "jaswanthmemories@gmail.com"
    from_password = "elco jqzg moqc pfwt"
    to_email = "guruguntlaviswanatha@gmail.com"

    print("Starting price tracking...")
    track_price(url, target_price, check_interval, to_email, from_email, from_password)
