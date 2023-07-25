from website import create_app


if __name__ == "__main__":
    app = create_app()
    # debug = True automatically re-runs the flask web server
    app.run(debug=True)
