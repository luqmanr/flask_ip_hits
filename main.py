from flask import Flask, request
import os

# Creating the instance of the class Flask
app = Flask(__name__)

# Create new log data if available
@app.route('/')
def update_data():
    # make log dir if not exists
    if not os.path.exists("log"):
        os.makedirs("log/")

    # get ip address
    ip_addr = f"log/{request.remote_addr}"

    # read file if exists
    if os.path.exists(ip_addr):
        with open(ip_addr, "r") as f:
            num_visited = f.read()
            num_visited = int(num_visited)
            num_visited += 1
            f.close()
    # if not, num_visited = 1
    else:
        num_visited = "1"

    # create/update log file
    with open(ip_addr, "w") as f:
        f.write(str(num_visited))
        f.close()

    return_msg = f"""User Address: {request.remote_addr} <-- user ip was set to {request.remote_addr}
Hits: {num_visited}
    """
    return return_msg

# Run the application
if __name__ == '__main__':
    app.run(port=5001, debug=True)