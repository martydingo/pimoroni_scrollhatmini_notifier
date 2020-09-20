import time
import scrollphathd

# Taken from the official examples at https://github.com/pimoroni/scroll-phat-hd/blob/master/examples/simple-scrolling.py and tweaked slightly


def scrollMsg(message):
    scrollphathd.clear()                         # Clear the display and reset scrolling to (0, 0)
    length = scrollphathd.write_string(message)  # Write out your message
    scrollphathd.show()                          # Show the result
    time.sleep(0.5)                              # Initial delay before scrolling

    length -= scrollphathd.width

    # Now for the scrolling loop...
    while length > 0:
        scrollphathd.scroll(1)                   # Scroll the buffer one place to the left
        scrollphathd.show()                      # Show the result
        length -= 1
        time.sleep(0.02)                         # Delay for each scrolling step

    time.sleep(0.5)                              # Delay at the end of scrolling
    scrollphathd.clear()