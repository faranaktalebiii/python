import instaloader

f = open("followers.tx", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close
         
loader = instaloader.Instaloader()

loader.login('testpage', '1234567')

profile = instaloader.Profile.from_username(loader.context,'testpage')

followers = profile.get_followers()
new_follower = []
for follower in followers:
    new_follower.append(follower)
    
    
for oldfollower in old_followers:
    if oldfollower not in new_follower:
        print (oldfollower)


        
newfollowers = open("newFollowers.txt", "w")
for newfollower in new_follower:
    if new_follower not in new_follower:
        newfollowers.write(new_follower + "\n")
newfollowers.close

f = open("followers.txt", "w")
for follower in new_follower:
    f.write(follower + "\n")

f.close()