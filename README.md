#Amazon Price Tracker
<p>This script monitors the price of a product on Amazon India and sends an email notification when the price drops below a specified target. 
   It uses web scraping (BeautifulSoup) to extract price details and SMTP to send alerts via email.</p>

<h3>Features</h3>
<p>✅ Scrapes the current price of a product from Amazon using requests and BeautifulSoup.</p>
<p>✅ Compares it with the target price set by the user</p>
<p>✅ Sends an email alert when the price drops</p>
<p>✅ Runs at a specified interval to check the price automatically.</p>
<h3>Setup & Usage</h3>
<h5>Run on Google Colab(Recommended)</h5>
<p>1.Open Google Colab<br/>
2.Upload the script (price_tracker.py)<br/>
3.Configure & add Email Credentials<br/>
   
For security, use Google App Passwords instead of your regular password:<br/>
. Enable 2-Step Verification in Google<br/>
. Generate an App Password (Google App Passwords)<br/>
. Enter the from_email, from_password(Generated app Password),to_email<br/>
. Run the Code.<br/>
. Check the Email for the price tracking Updates</p>

