from app import app

# Adding Secret Key to our App
app.secret_key = 'make this hard to guess!'

if __name__ = "__main__" :
  app.run(debug=True)
