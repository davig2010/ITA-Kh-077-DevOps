from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
"https://media.glamour.com/photos/580e1dc07a52574c7ef91071/master/w_1920%2Cc_limit/giphy%2520(1).gif",
"https://media.glamour.com/photos/580e1e70114e233c0c9c84fb/master/w_1920%2Cc_limit/cat%2520playing%2520ping%2520pong%2520ball%2520-%2520Imgur.gif",
"https://media.glamour.com/photos/580e1edafa71013257a9180f/master/w_1920%2Cc_limit/giphy%2520(2).gif",
"https://media.glamour.com/photos/580e393c7cbc533f7e7eae16/master/w_1920%2Cc_limit/Cat-Slide.gif",
"https://media.glamour.com/photos/580e254efa71013257a91810/master/w_1920%2Cc_limit/Showing%2520who's%2520really%2520the%2520boss.%2520-%2520Imgur.gif",
"https://media.glamour.com/photos/580e1f287cbc533f7e7eae0d/master/w_1920%2Cc_limit/giphy%2520(5).gif",
"https://media.glamour.com/photos/580e1d3cfa71013257a9180d/master/w_1920%2Cc_limit/Cat%2520in%2520a%2520box%2520on%2520a%2520skateboard%2520-%2520Imgur.gif",
"https://media.glamour.com/photos/580e1f078bd9950546d001f5/master/w_1920%2Cc_limit/giphy%2520(6).gif",
"https://media.glamour.com/photos/580e1f31114e233c0c9c84fc/master/w_1920%2Cc_limit/giphy%2520(7).gif",
"https://media.glamour.com/photos/580e1f6a9ee18bbc22ab57ef/master/w_1920%2Cc_limit/giphy%2520(9).gif",
"https://media.glamour.com/photos/580e2a729ee18bbc22ab57f4/master/w_1920%2Cc_limit/it's%252012%2520and%2520i%2520want%2520to%2520sleep%2520right%2520now%2520-%2520Imgur.gif",
"https://media.glamour.com/photos/580e1f887cbc533f7e7eae0e/master/w_1920%2Cc_limit/giphy%2520(10).gif"
]

@app.route('/')
def index():
    url = random.choice (images)
    return render_template ('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
