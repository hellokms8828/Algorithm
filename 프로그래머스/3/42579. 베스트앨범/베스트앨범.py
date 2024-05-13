def solution(genres, plays):
    song_dict = {}
    genre_total_plays = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in song_dict:
            song_dict[genre] = []
            genre_total_plays[genre] = 0
        song_dict[genre].append((i, play))
        genre_total_plays[genre] += play

    for genre in song_dict:
        song_dict[genre].sort(key=lambda x: (-x[1], x[0]))

    answer = []
    for genre, _ in sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True):
        answer.extend(song_dict[genre][:2])

    return [song[0] for song in answer]


# def solution(genres, plays):
#     answer = []
#     song_dict = dict()

#     for i in range(len(genres)):
#         if genres[i] not in song_dict:
#             song_dict[genres[i]] = [[i, plays[i]]]
#         else:
#             song_dict[genres[i]].append([i, plays[i]])
    
#     for i in song_dict:
#         song_dict[i].sort(key=lambda x: (-x[1], x[0]))
    

#     cpr_dict = dict()
#     for i in song_dict:
#         cpr_dict[i]=song_dict[i][0][1]
    
#     cpr_dict = dict(sorted(cpr_dict.items(), key=lambda x: x[1], reverse=True))

#     for i in cpr_dict:
#         if(len(song_dict[i])==1):
#             answer.append(song_dict[i][0][0])
#         else:
#             answer.append(song_dict[i][0][0])
#             answer.append(song_dict[i][1][0])
    
#     return answer