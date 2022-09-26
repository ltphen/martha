from distutils.log import debug
from app import app

def main():
    app.run(debug=1, host="::", port="5000")

if __name__ == "__main__":
    main()