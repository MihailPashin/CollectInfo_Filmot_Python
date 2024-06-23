class Boundary:
    def __init__(self):
        self.keywords = []

    def set_num_keywords(self):
        while True:
            try:
                num_keywords = int(input("Enter the number of keywords: "))
                if num_keywords <= 0 or num_keywords > 7:
                    print("Number of keywords should be [1,6]. Please try again.")
                    continue
                return num_keywords
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def set_keywords(self, num_keywords):
        for i in range(num_keywords):
            keyword = input(f"Enter keyword {i + 1}: ")
            self.keywords.append(keyword)

    def start(self):
        num_keywords = self.set_num_keywords()
        self.set_keywords(num_keywords)
        url = self.construct_url(self.keywords)
        print("Generated URL:")
        print(url)

    def construct_url(self, keywords):
        base_url = "https://filmot.com/search/"
        keyword_string = '%2C+'.join(f'%22{keyword.replace(" ", "+")}%22' for keyword in keywords)
        params = "?sortField=viewcount&sortOrder=asc&gridView=1&"
        return f"{base_url}{keyword_string}/{1}/{50}{params}"

    def get_keywords_list(self):
        return self.keywords
