# PageRank_in_Python
Determine important users in a Friend graph using PageRank. 
***
The data was gathered from [Yelp Dataset challenge](https://www.yelp.com/dataset_challenge). It's a collection of JSON documents. Each JSON document represents an user in the below format:  
<pre>{
    "user_id": "encrypted user id",
    "name": "first name",
    "review_count": number of reviews,
    "yelping_since": date formatted like "2009-12-19",
    "friends": ["an array of encrypted ids of friends"],
    "useful": "number of useful votes sent by the user",
    "funny": "number of funny votes sent by the user",
    "cool": "number of cool votes sent by the user",
    "fans": "number of fans the user has",
    "elite": ["an array of years the user was elite"],
    "average_stars": floating point average like 4.31,
    "compliment_hot": number of hot compliments received by the user,
    "compliment_more": number of more compliments received by the user,
    "compliment_profile": number of profile compliments received by the user,
    "compliment_cute": number of cute compliments received by the user,
    "compliment_list": number of list compliments received by the user,
    "compliment_note": number of note compliments received by the user,
    "compliment_plain": number of plain compliments received by the user,
    "compliment_cool": number of cool compliments received by the user,
    "compliment_funny": number of funny compliments received by the user,
    "compliment_writer": number of writer compliments received by the user,
    "compliment_photos": number of photo compliments received by the user,
    "type": "user"
}</pre>
  
  
