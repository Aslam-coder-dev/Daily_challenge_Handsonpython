print("----- Welcome to Smart Playlist Intelligence System -----")

user = "CricketFan"

username = input("Enter Username: ")

if username != user:
    print("Access denied!! Access is only allowed for the Doremon family members")
else:
    print("Login Successful!")
    print("🏏 Fun fact: This system is designed by a Cricket Fan!")

    music_lover = input("Do you love music? (yes/no): ").lower()

    if music_lover != "yes":
        print("This system is for music lovers only.")
        print("Please explore another field that matches your interest.")
    else:
        print("Great! Let's analyze Nobita's playlist...")

        playlist = []
        durations = input("Enter song durations in seconds (space separated): ").split()

        for d in durations:
            playlist.append(int(d))

        if any(dur <= 0 for dur in playlist):
            print("Invalid Playlist!! Playlist contains non-positive durations.")
        else:
            total = sum(playlist)
            no_of_songs = len(playlist)

            print("Total Duration:", total, "seconds")
            print("Songs:", no_of_songs)

            repetitive = False
            for dur in playlist:
                if playlist.count(dur) > 1:
                    repetitive = True
                    break

            if total < 300:
                category = "Too Short Playlist"
                recom = "Add more songs"

            elif total > 3600:
                category = "Too Long Playlist"
                recom = "Consider shortening your playlist"

            elif repetitive:
                category = "Repetitive Playlist"
                recom = "Add variety"

            elif max(playlist) - min(playlist) <= 300:
                category = "Balanced Playlist"
                recom = "Good listening session"

            else:
                category = "Irregular Playlist"
                recom = "Adjust song durations for better flow"

            print("Category:", category)
            print("Recommendation:", recom)
