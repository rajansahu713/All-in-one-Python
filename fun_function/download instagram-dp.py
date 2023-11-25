import instaloader

ig=instaloader.Instaloader()

db=input("Enter the username: ")

ig.download_profile(db,profile_pic_only=True)