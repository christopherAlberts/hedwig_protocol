import os
import time

def hedwig_protocol(listen_or_take, file_name, take_this):

    # THERE ARE TWO PARTS TO THIS FUNCTION:
    # -------------------------------------------------------------------------------------
    #
    # LISTEN:
    # This code is ment to be placed in a continues while loop.
    # If "listen" is selected the code will monitors a specific folder.
    # If there are text files inside, it will choose the oldest one and return the output.
    # Following this it will also remove the file.
    #
    # listen_or_take = "listen"
    # filename = The file path of the file you are monitoring.
    # take_this = ""
    #
    # -------------------------------------------------------------------------------------
    #
    # TAKE:
    # Code creates a file with text inside.
    #
    # listen_or_take = "take"
    # filename = The file path of the file you want to create.
    # take_this = The text you want to write to the file.
    #
    # -------------------------------------------------------------------------------------

    if listen_or_take == "listen":

        try:

            # Counts number of files in folder.
            file_count = sum([len(files) for r, d, files in os.walk(file_name)])

            if file_count > 0:
                # The following code is used to determine the oldest file in the folder.
                path = file_name
                os.chdir(path)
                files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

                oldest_file = files[0]
                # newest_file = files[-1]

                # now do something with the oldes file....
                fr = open(oldest_file)
                text = fr.read()
                fr.close()

                os.remove(oldest_file)  # Removes oldest file.

                return text

        except:
            # When a file is being copied while the Hedwig_protocol is running
            # it can cause and error, a delay helps with this.
            time.sleep(1)

    elif listen_or_take == "take":

        # WRITE TO A FILE
        fw = open(file_name, 'w')
        fw.write(take_this)
        fw.close()

