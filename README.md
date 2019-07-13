# tigera-coding-challenge
Coding challenge for Tigera interview

- Written in python, using Flask
- Approximate time: 4 hours

# Prerequisites
Ensure Docker & pytest are installed (instructions for Ubuntu):
```
sudo apt install docker.io
sudo apt install python-pytest
```

# Docker container build/run instructions
To build & run the Docker container, enter:
```
sudo bash start.sh
```
After the container builds and runs, it can be accessed via http://127.0.0.1/.

# Unit tests instructions
To run unit tests, enter the following:
```
cd tests/
pytest
```

# Notes
- If the application fails to access the name generator URL, it will display a joke with a default name
- This happens if you request a joke too many times due to the name generator URL returning 508 (resource limit exceeded)
