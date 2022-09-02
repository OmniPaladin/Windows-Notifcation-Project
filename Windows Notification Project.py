import time
from winotify import Notification, audio
#imports the necessary things for the projects. 

toast = Notification(app_id="Samii", title="Important Information!", 
                    msg = "CLICK THE LINK!", duration = "long")  #icon = r"C:\Users\Samii
#determines what the actual notifcation shows
                   

toast.set_audio(audio.Default, loop=False)
#makes the sound of the project

toast.add_actions(label="CLICK ME NOW!", launch="https://www.google.com/search?q=samii+shabuse&rlz=1C1CHBD_enUS905US905&sxsrf=ALiCzsa1uGdJwWGcx1zOw4X3aAdcrFoLsg:1662157144078&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiixYjxkff5AhVcjYkEHTwTDYAQ_AUoAnoECAEQBA&biw=1090&bih=845&dpr=1#imgrc=kX0hcuImUuwBxM")
#sets the button up for the notification, and creates a link on where to go!

toast.show()
#allows the notification to be shown 