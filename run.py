from app import create_app

app, logger = create_app()  # Unpack the app and logger

if __name__ == '__main__':
    app.run(debug=True, port=8000)
