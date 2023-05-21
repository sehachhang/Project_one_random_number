Number2 = 0

def on_button_pressed_a():
    music.set_tempo(120)
    for index in range(2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    for index2 in range(2):
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    basic.show_icon(IconNames.HEART)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_shake():
    global Number2
    basic.clear_screen()
    Number2 = randint(1, 6)
    if Number2 == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif Number2 == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
    elif Number2 == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif Number2 == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif Number2 == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_sound_quiet():
    basic.show_icon(IconNames.SMALL_HEART)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)
