# TODO:
It is a misconception that a goldfish's memory span is approximately 7 seconds. This idea is often attributed to the belief that goldfish have very short attention spans and forget things quickly. However, scientific research has shown that goldfish can actually retain memories for months and even years.
## Easy tasks to do when procrastinating: 
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
	
2. Page design: it's just a table with some buttons  
3. Deployment: Github page? Heroku?
4. Additional features to support:
	- **TRANSLATION: why do my friends speak so many different languages**
		- but not THAT many languages -- _additional attributes_ viable?
		- actually just kidding i have no friends
	- Map selection + random spawn location
		- How to store that information for the session?
	- Randomly choose from user-specified tactics


## Program logic:
1. Exception handling:
	- ~~Should add_gadget throw exception when sides don't match?~~  
		~~user shouldn't be able to interact with this <- prob not~~
2. Should I take object-oriented to the extreme and make separate classes for scope/barrel/laser/grip?
	- So that a Weapon *has* A scope, *has* a barrel,..., and a Scope *has* an attribute (path to image)...


## Misc:
1. Font: which font to use? (preferably one of siege's in-game font)
	- License?
	- Include as a resource if not commonly installed on user devices
2. Asset fine-tuning:
	- No HUD icon image for 'hard breach charge' and 'impact emp grenade' (and the new drone view blocking gadget):
		- a. Use a different style (in-game screen capture) OR  
		- b. Create those graphics from scratch? <-- really
	- Make transparent background for barrel images
3. Information accuracy: (checked and verified as of 5/11/23 -- many thanks to @Sunshine)
	- ~~Double check: weapons incompatible with laser?~~ <-- every gun has access to the laser under barrel, with the only exception being Kali's CSRX
		- ~~DMR: OTs-03~~, CSRX 300  
		- ~~LMG: G8A1~~  
		- ~~MP: C75~~  
		- ~~Handgun: GSH-18~~  
	- ~~Double check: OTs-03 has no access to reflex C?~~
		- That's correct! -- Cannot align properly with his gadget
