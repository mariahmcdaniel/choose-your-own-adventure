print("\nHowdy, this is a choose your own adventure game! Make your selections based on the prompts to test your fate!\n")

print( 
    '''     _____
     _.'_____`._
   .'.-'  12 `-.`.
  /,'           `.\.
 //         /    \.\.
;;         /       ::
|| 9  ----O      3 ||
::                 ;;
 \.\.              //
  \`.           ,'/
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
   '--'       '--'
   '''
)


alarm = input("\"Beeeep Beeeep\" ugh theres your alarm, another day of work.. time to get up... or do you want to press snooze? enter \"G\" to get up or \"S\" to snooze: ")

if alarm.lower() == "s":
    print("ahh 9 more minutes.. you get up and get ready for work at the sound of the next alarm. Time for breakfast! What are you having today?\n")
    print(
        '''
                       .-~-.
                     .'     '.
                    /         \\
            .-~-.  :           ;
          .'     '.|           |
         /         \           :
        :           ; .-~""~-,/
        |           /`        `'.
        :          |             \\
         \         |             /
          `.     .' \          .'
            `~~~`    '-.____.-'
                       
    
    '''
        )
    print(
        '''
        
        _.-------._
      .' _|_|_|_|_ '.
     / _|_|_|_|_|_|_ \\
    | |_|_|_|_|_|_|_| |
    |_|_|_|_|_|_|_|_|_|
    | |_|_|_|_|_|_|_| |
    | |_|_|_|_|_|_|_| |
     \ -|_|_|_|_|_|- /
      '. -|_|_|_|- .'
        `---------`
        '''
    )
    breakfast = input("\nAre you feeling eggs or waffles? Enter \"E\" for eggs or \"W\" for waffles: ")
