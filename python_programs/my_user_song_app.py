class my_user_song_app:
    def __init__(self):
        # Initialize the user base with some default users
        # This is a simple in-memory user base for demonstration purposes.
        # self.my_user_base = ['Hari','Sophia','Julian','Shrinal']
        # self.user_songs = dict()
        # self.user_songs['Hari'] = ['Song1', 'Song2']
        # self.user_songs['Sophia'] = ['Song3', 'Song4']
        # self.user_songs['Julian'] = ['Song5']
        # self.user_songs['Shrinal'] = ['Song6', 'Song7', 'Song8']

    def get_user_base(self):
        """
        Get the list of users.
        """
        return self.my_user_base
    
    def add_user(self, user):
        """
        Add a new user to the user base.
        If the user already exists, do nothing.
        """
        if user not in self.my_user_base:
            self.my_user_base.append(user)
        else:
            print(f"User {user} already exists in the user base.")

    def delete_user(self,user):
        """
        Delete a user from the user base.
        If the user does not exist, do nothing.
        """
        if user in self.my_user_base:
            self.my_user_base.remove(user)
            # Also remove the user's song list if it exists
            if user in self.user_songs:
                del self.user_songs[user]
            else:
                print(f"User {user} exists in the userbase, but, does not have a song list to delete.")
        else:
            print(f"User {user} does not exist in the user base.")

    # Is case-sensitive here ( for safety ) 
    def get_song_list_by_user_id(self,user_id):
        """
        Get the song list for a specific user.
        If the user does not have a song list, return an empty list.
        """
        if(user_id not in self.my_user_base):
            return []
        if user_id not in self.user_songs:
            return []
        return self.user_songs.get(user_id)
    
    def add_song_to_user(self, user_id, song):
        """
        Add a song to the user's song list.
        If the user does not exist, create a new entry.
        """
        if user_id not in self.user_songs:
            self.user_songs[user_id] = []
        self.user_songs[user_id].append(song)

    def delete_song_from_user(self, user_id, song):
        """
        Delete a song from the user's song list.
        If the user does not exist or the song is not in the user's list, do nothing.
        """
        if user_id in self.user_songs and song in self.user_songs[user_id]:
            self.user_songs[user_id].remove(song)

    


    
