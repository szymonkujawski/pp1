facebook = True
twitter = False
instagram = True

fb_number = 0
if facebook==True:
    fb_number = fb_number + 1
else:
    fb_number = fb_number

tw_number = 0
if twitter==True:
    tw_number = tw_number + 1
else:
    tw_number = tw_number

ig_number = 0
if instagram==True:
    ig_number = ig_number + 1
else:
    ig_number = ig_number

sum = 0
sum = fb_number+tw_number+ig_number

if sum>=2:
    print("You can be a good influencer")
else:
    print("You cannot")