GdScriptBook = """
GdScript Book

var | onready var
string int float
don't forget ----> hide() | show()

| - + * / %  | -= += /= *=  |
| == != | 
| / not / in / or / and / |

| int(10) / float(10.50) / Example number = 10 ---> float(number) ---> 10.0 |

| a,b,c = 10 # multiple assignment / type(number) <--show you type |
| GnuChan       /start : end : step\ |
| 0123456 --->    [0   : 10  :  2]   |

get_node(Label) or $Label -----> true false


-- very simple Timer
if timeDeck > 0:
	timeDeck -= 0.01
else:
	example play animation
------------------------------------------

-- Animation Tree\State Machine Example
var playback : AnimationNodeStateMachinePlayback


func _ready():
	playback = get("parameters/playback")
	playback.start("sit_idle")
	active = true

	if Input.is_action_just_pressed("1") and gnuChanDeck == false:
		playback.travel("sit_take_Deck")
------------------------------------------


bonus material yazılımla uyumsuz












"""