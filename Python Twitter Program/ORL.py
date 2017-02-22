 
from twitter import *

con_secret = 'Yhh3C8qvN4S0R8ZeXWILgMbKa'#'Lwoxkf3OhshvdAYPvDofu0yW4' #'Yhh3C8qvN4S0R8ZeXWILgMbKa' #'fS2GnfQvIfogzVEVYHeYME0JV'
con_secret_key = 'RcNNeQUJVqlJOh38Yi7QzIPAvU2q9qPIOeoUjoL8Q7tyNY9eoI'#'bfzsNGpd3cKXSCxZgtO4sEs8o6OmzdmkCg4fHMZnXezyZfeK2A'#'RcNNeQUJVqlJOh38Yi7QzIPAvU2q9qPIOeoUjoL8Q7tyNY9eoI' #'a2QxoARIy3pcqCv3paXT0PQOvUUFUShyVxQty7jgEJI0BTIx7g'
token = '251130208-zNOVClWw9uVB9rhnaKL3dvD2jbo56LKTu6E6ebM4'#'710769614704107522-e8qNDpccBRUddb1NBgpQsJVF4TPQXqv' #'251130208-zNOVClWw9uVB9rhnaKL3dvD2jbo56LKTu6E6ebM4' #'2804059393-rVrID2JBkZ9kl0Bfhno1yGmwJqyMYSKXTXxeLS0'
token_key = '4JbTOtDN5XTlpmKdqs35y1uY5R6Wb9zK9GfX2Xf3keT5w'#'17GcYcTnJ30UlnXGEjQYtmCHKoF3XstqN7m5afDWzNl8W' #'4JbTOtDN5XTlpmKdqs35y1uY5R6Wb9zK9GfX2Xf3keT5w' #'HngdNxjQ8nFtTGw48H2XeVh71gsA8c2hvSuStMaZGIlFD'
     
def twitterOpen():
    print("Twitter Authenticating")
    #enter the corresponding information from your Twitter application:
    t = Twitter(
        auth=OAuth(token, token_key, con_secret, con_secret_key))
    print("Twitter Authenticated Successfully")
    return(t)

def twitterStatus(t,sta):
    # Update your status
    print("Updating Status")
    t.statuses.update(status=str(sta))
    print("Status Updated Successfully")

def twitterSendMessage(t,u,msg):
    # Send a direct message
    print("Sending Message")
    t.direct_messages.new(
    user=str(u),
    text=str(msg))
    print("Message Sent Successfully")

def twitterSendImage(t,msg,ph):
    print("Sending Photo")
    with open(str(ph), "rb") as imagefile:
        imagedata = imagefile.read()
        t_up = Twitter(domain='upload.twitter.com',
        auth=OAuth(token, token_key, con_secret, con_secret_key))
        id_img1 = t_up.media.upload(media=imagedata)["media_id_string"]
        id_img2 = t_up.media.upload(media=imagedata)["media_id_string"]
        # - finally send your tweet with the list of media ids:
        t.statuses.update(status=str(msg), media_ids=",".join([id_img1, id_img2]))
    print("Photo Uploaded Successfully")
