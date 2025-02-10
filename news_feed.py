from datetime import datetime

class News:
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def publish(self):
        return f"News:\n{self.text}\nCity: {self.city}\nPublished on: {self.date}\n{'-' * 30}\n"


class PrivateAd:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        return f"Private Ad:\n{self.text}\nExpires on: {self.expiration_date.strftime('%Y-%m-%d')} ({self.days_left} days left)\n{'-' * 30}\n"


class UniqueRecord:
    def __init__(self, headline, content, author):
        self.headline = headline
        self.content = content
        self.author = author
        self.publish_time = datetime.now().strftime("%H:%M:%S on %Y-%m-%d")

    def publish(self):
        return f"Unique Record:\nHeadline: {self.headline}\n{self.content}\nAuthor: {self.author}\nPublished at: {self.publish_time}\n{'-' * 30}\n"


class NewsFeedApp:
    def __init__(self, filename="news_feed.txt"):
        self.filename = filename

    def add_record(self, record):
        with open(self.filename, "a") as file:
            file.write(record.publish())

    def run(self):
        while True:
            print("\nWelcome to the News Feed App")
            print("1. Add News")
            print("2. Add Private Ad")
            print("3. Add Unique Record")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                text = input("Enter the news text: ")
                city = input("Enter the city: ")
                news = News(text, city)
                self.add_record(news)

            elif choice == "2":
                text = input("Enter the ad text: ")
                expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")
                ad = PrivateAd(text, expiration_date)
                self.add_record(ad)

            elif choice == "3":
                headline = input("Enter the headline: ")
                content = input("Enter the content: ")
                author = input("Enter the author: ")
                unique = UniqueRecord(headline, content, author)
                self.add_record(unique)

            elif choice == "4":
                print("Exiting the News Feed App. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = NewsFeedApp()
    app.run()
