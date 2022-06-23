""" ======================================================================
Final Project - Audio Manipulation
File: AudioManipulationfile
Author: Julian Evans, Nawal Maqbool, Owen Lindstrom
"""

from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk
from tkinter import *





#Songs
song1 = AudioSegment.from_wav('Songs/apologize.wav')
song2 = AudioSegment.from_wav('Songs/beatit.wav')
song3 = AudioSegment.from_wav('Songs/billionaire.wav')
song4 = AudioSegment.from_wav('Songs/igottafeeling.wav')
song5 = AudioSegment.from_wav('Songs/oceaneyes.wav')
song6 = AudioSegment.from_wav('Songs/revenge.wav')


#Spleeter Vocals wav files

vocal1 = AudioSegment.from_wav('Vocal/apologize_vocals.wav')
Vocal2 = AudioSegment.from_wav('Vocal/beatit_vocals.wav')
vocal3 = AudioSegment.from_wav('Vocal/billionaire_vocals.wav')
Vocal4 = AudioSegment.from_wav('Vocal/igottafeeling_vocals.wav')
vocal5 = AudioSegment.from_wav('Vocal/oceaneyes_vocals.wav')
Vocal6 = AudioSegment.from_wav('Vocal/revenge_vocals.wav')

#Spleeter beat wav files

Beat1 = AudioSegment.from_wav('Beat/apologize_beat.wav')
Beat2 = AudioSegment.from_wav('Beat/beatit_beat.wav')
Beat3 = AudioSegment.from_wav('Beat/billionaire_beat.wav')
Beat4 = AudioSegment.from_wav('Beat/igottafeeling_beat.wav')
Beat5 = AudioSegment.from_wav('Beat/Oceaneyes_beat.wav')
Beat6 = AudioSegment.from_wav('Beat/revenge_beat.wav')


# # convert mp3 to wav
# src = "test.mp3"
# dst = "test.wav"
#
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")


#Gui setup
class User:
    """An object containing a GUI program"""

    def __init__(self):
        """Initialize the User object and all its widgets"""

        self.rootWin = tk.Tk()
        self.rootWin.title("Audio Manipulation")
        self.rootWin.config(background="pink")
        self.rootWin.geometry("1000x1000")


        self.myLabel = tk.Label(self.rootWin, font='ComicSans 40 bold', fg="yellow", borderwidth=False)
        self.myLabel.place(relx=.5, rely=.05, anchor=CENTER)
        self.myLabel["text"] = "Select and audio"



        quitButton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"

        Apologizebutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        Apologizebutton["text"] = "Apologize     By: Baby Keem"
        Apologizebutton.place(relx=.5, rely=.20, anchor=CENTER)
        Apologizebutton["command"] = self.Apologize_Songs

        beatitbutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        beatitbutton["text"] = "Beat It     By: Michael Jackson"
        beatitbutton.place(relx=.5, rely=.27, anchor=CENTER)
        beatitbutton["command"] = self.Beatit_Songs

        billionairebutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        billionairebutton["text"] = "Billionaire     By: Bruno Mars"
        billionairebutton.place(relx=.5, rely=.34, anchor=CENTER)
        billionairebutton["command"] = self.Billionaire_Songs

        igottafeelingbutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        igottafeelingbutton["text"] = "I Gotta Feeling     By: Black Eye'd Peals"
        igottafeelingbutton.place(relx=.5, rely=.41, anchor=CENTER)
        igottafeelingbutton["command"] = self.Igottafeeling_Songs

        oceaneyesbutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        oceaneyesbutton["text"] = "Ocean Eyes     By: Billie Eilish"
        oceaneyesbutton.place(relx=.5, rely=.48, anchor=CENTER)
        oceaneyesbutton["command"] = self.Oceaneyes_Songs

        revengebutton = tk.Button(self.rootWin, borderwidth=0, font='Merriweather 30')
        revengebutton["text"] = "Revenge     By: XXX TENTACION"
        revengebutton.place(relx=.5, rely=.55, anchor=CENTER)
        revengebutton["command"] = self.Revenge_Songs



#---

    def go(self):
        """This takes no inputs, and sets the GUI running"""
        self.rootWin.mainloop()

    def quit(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.rootWin.destroy()
    def quit2(self):
        """This is a callback method attached to the quit button.
                        It destroys the window 2, which ends the program"""
        self.rootWin2.destroy()
    def quit3(self):
        """This is a callback method attached to the quit button.
                        It destroys the window 3, which ends the program"""
        self.rootWin3.destroy()
    def quit4(self):
        """This is a callback method attached to the quit button.
                        It destroys the window 4, which ends the program"""
        self.rootWin4.destroy()

# This is def for all songs to bring to new window which song clicked
    def Apologize_Songs(self):
        '''This function defines the song Apologize and opens up a new window with all the functions on it.
        The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
        button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")


        self.songname = tk.Label(self.rootWin2, text = "Apologize     By: Baby Keem"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)


        speedbutt = tk.Button(self.rootWin2, borderwidth=0, text="speed", font='Merriweather 30',
                              command=self.speedbuttonApologize)
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["text"] = "Reverse"
        reversebutt["command"] = self.reverseApologize

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalApologize

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatApologize

        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2



    def Beatit_Songs(self):
        '''This function defines the song Beat It and opens up a new window with all the functions on it.
                The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
                button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")
        self.songname = tk.Label(self.rootWin2, text = "Beat It     By: Michael Jackson"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)

        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2

        # This is where you add the functions for changing song (speed up.....)
        speedbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        speedbutt["text"] = "speed"
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)
        speedbutt["command"] = self.speedbuttonBeatit

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt["text"] = "Reverse"
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["command"] = self.reverseBeatit

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalBeatit

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatBeatit

    def Billionaire_Songs(self):
        '''This function defines the song Billionaire and opens up a new window with all the functions on it.
                The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
                button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")
        self.songname = tk.Label(self.rootWin2, text = "Billionaire      By: Bruno Mars"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)

        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2

        # This is where you add the functions for changing song (speed up.....)
        speedbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        speedbutt["text"] = "speed"
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)
        speedbutt["command"] = self.speedbuttonBillionaire

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt["text"] = "Reverse"
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["command"] = self.reverseBillionaire

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalBillionaire

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatBillionaire

    def Igottafeeling_Songs(self):
        '''This function defines the song I Gotta Feeling and opens up a new window with all the functions on it.
                The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
                button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")
        self.songname = tk.Label(self.rootWin2, text = "I Gotta Feeling     By: Black Eye'd Peals"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)

        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2

        # This is where you add the functions for changing song (speed up.....)
        speedbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        speedbutt["text"] = "speed"
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)
        speedbutt["command"] = self.speedbuttonIgottafeeling

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt["text"] = "Reverse"
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["command"] = self.reverseIgottafeeling

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalIgottafeeling

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatIgottafeeling

    def Oceaneyes_Songs(self):
        '''This function defines the song Oceaneyes and opens up a new window with all the functions on it.
                The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
                button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")
        self.songname = tk.Label(self.rootWin2, text = "Ocean Eyes     By: Billie Eilish"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)

        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2

        # This is where you add the functions for changing song (speed up.....)
        speedbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        speedbutt["text"] = "speed"
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)
        speedbutt["command"] = self.speedbuttonoceaneyes

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt["text"] = "Reverse"
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["command"] = self.reverseOceaneyes

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalOceaneyes

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatOceaneyes

    def Revenge_Songs(self):
        '''This function defines the song Revenge and opens up a new window with all the functions on it.
                The functions have a speed button, a reverse button, a vocals button, and a beat button. it also has a quit
                button to exit that window.'''
        self.rootWin2 = tk.Tk()
        self.rootWin2.title("Song")
        self.rootWin2.geometry("1000x1000")
        self.rootWin2.config(background="blue")
        self.songname = tk.Label(self.rootWin2, text = "Revenge     By: XXX TENTACION"
                                  , fg = "black", font = "25")
        self.songname.place(relx=.5, rely=.1, anchor=CENTER)


        quitButton = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit2

        # This is where you add the functions for changing song (speed up.....)
        speedbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        speedbutt["text"] = "speed"
        speedbutt.place(relx=.5, rely=.3, anchor=CENTER)
        speedbutt["command"] = self.speedbuttonRevenge

        reversebutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        reversebutt["text"] = "Reverse"
        reversebutt.place(relx=.5, rely=.45, anchor=CENTER)
        reversebutt["command"] = self.reverseRevenge

        vocalbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        vocalbutt["text"] = "Vocals"
        vocalbutt.place(relx=.5, rely=.6, anchor=CENTER)
        vocalbutt["command"] = self.vocalRevenge

        beatbutt = tk.Button(self.rootWin2, borderwidth=0, font='Merriweather 30')
        beatbutt["text"] = "Beat"
        beatbutt.place(relx=.5, rely=.75, anchor=CENTER)
        beatbutt["command"] = self.beatRevenge

#This is where I add the functions buttons for each manipulation
    # ------Speed
    def speedbuttonApologize(self):
        '''This function creates a window when clicked on the button it brings you to a new window
        and adds a label on the screen as well as a user input for the user to select a speed for the song Apologize.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                          "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
            input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song1._spawn(song1.raw_data, overrides={"frame_rate": int(song1.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song1.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx= .5, rely= .4, anchor=CENTER)



    def speedbuttonBeatit(self):
        '''This function creates a window when clicked on the button it brings you to a new window
                and adds a label on the screen as well as a user input for the user to select a speed for the song Beat it.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                          "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
                        input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song2._spawn(song2.raw_data, overrides={"frame_rate": int(song2.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song2.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx= .5, rely= .4, anchor=CENTER)


    def speedbuttonBillionaire(self):
        '''This function creates a window when clicked on the button it brings you to a new window
                and adds a label on the screen as well as a user input for the user to select a speed for the song Billionaire.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                          "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
                        input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song3._spawn(song3.raw_data, overrides={"frame_rate": int(song3.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song3.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx= .5, rely= .4, anchor=CENTER)


    def speedbuttonIgottafeeling(self):
        '''This function creates a window when clicked on the button it brings you to a new window
                and adds a label on the screen as well as a user input for the user to select a speed for the song I gotta feeling.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                          "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
                        input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song4._spawn(song4.raw_data, overrides={"frame_rate": int(song4.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song4.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx= .5, rely= .4, anchor=CENTER)


    def speedbuttonoceaneyes(self):
        '''This function creates a window when clicked on the button it brings you to a new window
                and adds a label on the screen as well as a user input for the user to select a speed for the song Oceaneyes.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                  "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
                        input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song5._spawn(song5.raw_data, overrides={"frame_rate": int(song5.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song5.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx=.5, rely=.4, anchor=CENTER)


    def speedbuttonRevenge(self):
        '''This function creates a window when clicked on the button it brings you to a new window
                and adds a label on the screen as well as a user input for the user to select a speed for the song Revenge.'''
        self.rootWin3 = tk.Tk()
        self.rootWin3.title("speed")
        self.rootWin3.geometry("1000x1000")
        self.rootWin3.config(background="blue")
        instrLabel = tk.Label(self.rootWin3, text="Type a number between 0 - 2. (Below 1 will "
                                                          "slow song down and above 1 will speed song up)",
                              relief=tk.RAISED,
                              padx=5, pady=5)
        instrLabel.place(relx=.5, rely=.3, anchor=CENTER)

        userinput = tk.Entry(self.rootWin3, relief=tk.RAISED)
        userinput.place(relx=.5, rely=.35, anchor=CENTER)

        quitButton = tk.Button(self.rootWin3, borderwidth=0, font='Merriweather 30')
        quitButton.place(relx=.5, rely=.9, anchor=CENTER)
        quitButton["command"] = self.quit
        quitButton["text"] = "Quit"
        quitButton["command"] = self.quit3

        def doit():
            '''This function takes the user input and applies to change the speed of the song they selected. The users
                        input must be between 0 and 2'''
            x = userinput.get()
            y = float(x)
            if 0 < float(y) < 2:
                song_changedR = song6._spawn(song6.raw_data, overrides={"frame_rate": int(song6.frame_rate * y)})
                song_changedR = song_changedR.set_frame_rate(song6.frame_rate)
                play(song_changedR)

            else:
                errorbutt = Label(self.rootWin3, text="Silly individual. Please enter number between 0 and 2.")
                errorbutt.place(relx=.5, rely=.5, anchor=CENTER)

        work = Button(self.rootWin3, text="click", command=doit)
        work.place(relx= .5, rely= .4, anchor=CENTER)

#---------Reverse

    def reverseApologize(self):
        '''This function plays the song Apologize in reverse when the reverse button is pressed.'''
        reversesongA = song1.reverse()
        play(reversesongA)

    def reverseBeatit(self):
        '''This function plays the song Beat it in reverse when the reverse button is pressed.'''
        reversesongB = song2.reverse()
        play(reversesongB)

    def reverseBillionaire(self):
        '''This function plays the song that is selected in reverse when the reverse button is pressed.'''
        reversesongBi = song3.reverse()
        play(reversesongBi)

    def reverseIgottafeeling(self):
        '''This function plays the song I gotta feeling in reverse when the reverse button is pressed.'''
        reversesongI = song4.reverse()
        play(reversesongI)

    def reverseOceaneyes(self):
        '''This function plays the song Oceaneyes in reverse when the reverse button is pressed.'''
        reversesongO = song5.reverse()
        play(reversesongO)

    def reverseRevenge(self):
        '''This function plays the song Revenge in reverse when the reverse button is pressed.'''
        reversesongR = song6.reverse()
        play(reversesongR)

#-------Vocals

    def vocalApologize(self):
        '''This function plays the vocals of the song Apologize when the vocal button is pressed.'''
        play(vocal1)

    def vocalBeatit(self):
        '''This function plays the vocals of the song Beat it when the vocal button is pressed.'''
        play(Vocal2)

    def vocalBillionaire(self):
        '''This function plays the vocals of the song Billionaire when the vocal button is pressed.'''
        play(vocal3)

    def vocalIgottafeeling(self):
        '''This function plays the vocals of the song I gotta Feeling when the vocal button is pressed.'''
        play(Vocal4)

    def vocalOceaneyes(self):
        '''This function plays the vocals of the song Oceaneyes when the vocal button is pressed.'''
        play(vocal5)

    def vocalRevenge(self):
        '''This function plays the vocals of the song Revenge when the vocal button is pressed.'''
        play(Vocal6)

#------Beat

    def beatApologize(self):
        '''This function plays the beat of the song Apologize when the beat button is pressed.'''
        play(Beat1)

    def beatBeatit(self):
        '''This function plays the beat of the song Beat it when the beat button is pressed.'''
        play(Beat2)

    def beatBillionaire(self):
        '''This function plays the beat of the song Billionaire when the beat button is pressed.'''
        play(Beat3)

    def beatIgottafeeling(self):
        '''This function plays the beat of the song I gotta feeling when the beat button is pressed.'''
        play(Beat4)

    def beatOceaneyes(self):
        '''This function plays the beat of the song Oceaneyes when the beat button is pressed.'''
        play(Beat5)

    def beatRevenge(self):
        '''This function plays the beat of the song Revenge when the beat button is pressed.'''
        play(Beat6)


# --- here it goes...
myGui = User()
myGui.go()
