from server import api
import os

def main():
    port = int(os.environ.get("PORT", 5000))
    api.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()