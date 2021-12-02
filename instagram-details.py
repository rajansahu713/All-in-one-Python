# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

username = input("Enter the username: ")
# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, username)
print(profile.username)
print(profile.userid)
print(profile.full_name)
print(profile.biography)
print(profile.followers)
print(profile.followees)
print(profile.get_profile_pic_url())
print(type(profile))