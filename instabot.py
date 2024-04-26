import instaloader

bot = instaloader.Instaloader()
# Only while acessing a private account that you follow 
#Code to be added -> bot.login(user="Your_username",passwd="Your_password") 
#Use this code to log-in to your account.

def getBasicInfo():
    profileId = input('Enter the userid of the profile\n')
    profile = instaloader.Profile.from_username(bot.context, profileId)
    print("Username:", profile.username)
    print("User ID:", profile.userid)
    print("Followers Count:", profile.followers)
    print("Following Count:", profile.followees)
    print("Number of Posts:", profile.mediacount)
    print("Bio:", profile.biography)
    print("External URL:", profile.external_url)
    print("\n")

def searchInfo():
    searchItem = input("Enter the search keyword\n")
    search_results = instaloader.TopSearchResults(bot.context, searchItem)
    print("\n")
    
    for username in search_results.get_profiles():
        print(username)

    print("\n")

    for hashtag in search_results.get_hashtags():
        print(hashtag)
    
    print("\n")


def downloadPost():
    userId = input("Enter the userid of the profile\n")
    profile = instaloader.Profile.from_username(bot.context, userId)

    posts = profile.get_posts()
    count = 0
    for index, post in enumerate(posts, 1):
        if count < 5:
            bot.download_post(post, target=f"{profile.username}_{index}") # setting file directory and filename
            count += 1
        else:
            break

if __name__ == '__main__':
    option = '0'
    while option != '4':
        option =  input("Select your option\n1)Get profile Info\n2)Search for Top Profiles and Hashtags\n3)Downoad Profile posts\n4)Exit\n\n")

        if option == '1':
            getBasicInfo()
        elif option == '2':
            searchInfo()
        elif option == '3':
            downloadPost()
        elif option == '4':
            exit
        else:
            print("Wrong input. Please try again")

