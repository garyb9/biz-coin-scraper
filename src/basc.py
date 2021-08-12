import basc_py4chan as bp4

board = bp4.Board('biz')
threads = board.get_all_threads()
posts = []
for thread in threads:
    for post in thread.posts:
        posts.append(post)

1==1