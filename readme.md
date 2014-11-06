# music chat

make music by sending chat messages to each other on your local network.

## installation

the program only runs on mac os.

you need to install the sox library:

`brew install sox`

## run

there are three programs: the player, the sender, and the looper.

start the player in one terminal and the sender in another.

````
python player.py
````

````
python sender.py
````

after picking a name for yourself, type a message on the sender side and send it off by pressing enter. the player will receive it and play it as sounds.

run these programs on as many computers as you want.

make music.

also try out the looper! it's similar to the sender, but you can only enter one message that it will then loop for you. (hint: run as many loopers in parallel as you want!)

## if it doesn't work

the ip address range is hard-coded in base.py. if your local ip addresses are different, change it in the code.

## i don't like it

oh. sorry. order a pizza and watch a movie maybe?
