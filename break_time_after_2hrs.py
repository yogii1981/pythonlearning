import time
import webbrowser

Total_breaks = 3
break_count = 0

print("This program started on"+time.ctime())
while(break_count < Total_breaks):
    time.sleep(7200)#music break after every 2 hour
    webbrowser.open("https://www.youtube.com/watch?v=aq-CKdT6IG4")
    break_count = break_count + 1