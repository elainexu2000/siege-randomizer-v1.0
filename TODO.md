# TODO:

## Easy task to do when procrastinating: 
1. Download every weapon's img from ubisoft website; sort by weapon type
2. Same thing for scope, barrel, grip, laser, op icon

## Actually implement this:
1. Import Flask and create a new Flask application:
	```
	from flask import Flask
	app = Flask(__name__)
	```
2. Define a route for API endpoint:
	```
	# Define a route for the /api/random-loadout URL
	# When a client sends a GET request to the /api/random-loadout URL, Flask will call the random_loadout() function and return the response to the client.
	@app.route('/api/random-loadout')
	def random_loadout():
		loadout = operator.get_random_loadout()
		# return the loadout dictionary in JSON format
		return jsonify(loadout)
	```
3. Run flask application:
	```
	if __name__ == '__main__':
    app.run()
	```

## Project design:
1. Integrating backend to frontend.
	
2. What do you want your page to look like?
	- Info/image to be displayed?
	- Page design: haha i'm so good at this (..)
3. Deployment: Github page? Heroku?
4. Additional features to support?
	- **TRANSLATION: yeah why do my friends speak so many different languages??**
		- but not THAT many languages -- _additional attributes_ viable?
		- actually just kidding i have no friends
	- Map selection + random spawn location
		- How to store that information for the session?
	- User-input random tactics


## Program logics:
1. Exception handling:
	- Should add_gadget throw exception when sides don't match?  
		(i.e. trying to add c4 to an attacker)   
		user shouldn't be able to interact with this <- prob not
2. Should i take object-oriented to the extreme and make separate classes for scope/barrel/laser/grip?
	- So that a Weapon *has* A scope, *has* a barrel,..., and a Scope *has* an attribute (path to image)...


## Minor stuff:
1. Font: which font to use? (preferably matching siege's)
	- License issue
	- Include as a resource
2. Asset fine-tuning:
	- No HUD icon image for 'hard breach charge' and 'impact emp grenade':  
		- a. Use a different style (in-game screen capture?) OR  
		- b. draw my own?? <-- how?
	- Make transparent background for barrel images
3. Information accuracy:
	- Double check: weapons incompatible with laser?  
		- DMR: OTs-03, CSRX 300  
		- LMG: G8A1  
		- MP: C75  
		- Handgun: GSH-18  
	- Double check: OTs-03 doesn't have reflex C??
