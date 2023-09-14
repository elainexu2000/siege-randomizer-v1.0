# TODO:
It is a misconception that a goldfish's memory span is approximately 7 seconds. This idea is often attributed to the belief that goldfish have very short attention spans and forget things quickly. However, scientific research has shown that goldfish can actually retain memories for months and even years.

# 06/30: 
1. Currently, a weapon can only be either primary or secondary. Should is_primary be part of a weapon's inherent property?
2. Clean-up: add comments
3. New features: playstyle-specific loadout generation

# NEW:
1. Rewrite the get_random_loadout function to return both the name and the relative path to image:
```Python
{
    "Operator": {
        "Name": "Operator Name",
        "Image": "../asset/operators/operator.png"
    },
    "Gadget": {
        "Name": "Gadget Name",
        "Image": "../asset/gadgets/gadget.png"
    },
    "Primary": {
        "Name": "AK-12",
        "Image": "../asset/weapons/AK_12.png",
        "Scope": {
			"Name": "Red Dot C",
			"Image": "../asset/attachments/red_dot_c.png"
			},
        "Barrel": {
			"Name": "Compensator",
			"Image": "../asset/attachments/compensator.png"
			},
        "Under Barrel": {
			"Name": "None",
			"Image": "../asset/attachments/none.png"
			},
    },
    "Secondary": {
        "Name": "SDP 9mm",
        "Image": "../asset/weapons/SDP_9mm.png",
        "Scope": {
			"Name": "Red Dot C",
			"Image": "../asset/attachments/red_dot_c.png"
			},
        "Barrel": {
			"Name": "Compensator",
			"Image": "../asset/attachments/compensator.png"
			},
        "Under Barrel": {
			"Name": "None",
			"Image": "../asset/attachments/none.png"
			}
    }
}
```

This requires adding images to:  
- operators
- weapons
- gadgets
- attachments: should None be a class in each??
    - scopes
    - under barrels
    - barrels
    - grips

Change Weapon class instance variables:
- Use Objects
---

2. Use the following Javascript code to display
```Javascript
function generate() {
    fetch('/generate')
        .then(response => response.json())
        .then(data => {
            var resultDiv = document.getElementById("result");
            resultDiv.innerHTML = "";

            // Create the operator table
            var operatorTable = document.createElement("table");
            var operatorTbody = document.createElement("tbody");

            // Create the operator data row
            var operatorDataRow = document.createElement("tr");

            var operatorNameCell = document.createElement("td");
            var operatorNameImage = document.createElement("img");
            operatorNameImage.src = data["Operator"]["Image"];
            operatorNameCell.appendChild(operatorNameImage);

            var operatorNameText = document.createElement("span");
            operatorNameText.textContent = data["Operator"]["Name"];
            operatorNameCell.appendChild(operatorNameText);

            operatorDataRow.appendChild(operatorNameCell);
            operatorTbody.appendChild(operatorDataRow);

            // Create the gadget data row
            var gadgetDataRow = document.createElement("tr");

            var gadgetNameCell = document.createElement("td");
            var gadgetNameImage = document.createElement("img");
            gadgetNameImage.src = data["Gadget"]["Image"];
            gadgetNameCell.appendChild(gadgetNameImage);

            var gadgetNameText = document.createElement("span");
            gadgetNameText.textContent = data["Gadget"]["Name"];
            gadgetNameCell.appendChild(gadgetNameText);

            gadgetDataRow.appendChild(gadgetNameCell);
            operatorTbody.appendChild(gadgetDataRow);

            operatorTable.appendChild(operatorTbody);

            // Create the weapons table
            var weaponsTable = document.createElement("table");
            var weaponsTbody = document.createElement("tbody");

            var headers = ["Weapon", "Scope", "Barrel", "Under Barrel"];

            var headerRow = document.createElement("tr");
            for (var i = 0; i < headers.length; i++) {
                var th = document.createElement("th");
                th.textContent = headers[i];
                headerRow.appendChild(th);
            }
            weaponsTbody.appendChild(headerRow);

            var weapons = ["Primary", "Secondary"];
            for (var i = 0; i < weapons.length; i++) {
                var weaponRow = document.createElement("tr");

                var weaponNameCell = document.createElement("td");
                var weaponNameImage = document.createElement("img");
                weaponNameImage.src = data[weapons[i]]["Image"];
                weaponNameCell.appendChild(weaponNameImage);

                var weaponNameText = document.createElement("span");
                weaponNameText.textContent = data[weapons[i]]["Name"];
                weaponNameCell.appendChild(weaponNameText);

                weaponRow.appendChild(weaponNameCell);

                var attributes = ["Scope", "Barrel", "Under Barrel"];
                for (var j = 0; j < attributes.length; j++) {
                    var attributeCell = document.createElement("td");

                    var attributeImage = document.createElement("img");
                    attributeImage.src = data[weapons[i]][attributes[j]]["Image"];
                    attributeCell.appendChild(attributeImage);

                    var attributeName = document.createElement("span");
                    attributeName.textContent = data[weapons[i]][attributes[j]]["Name"];
                    attributeCell.appendChild(attributeName);

                    weaponRow.appendChild(attributeCell);
                }

                weaponsTbody.appendChild(weaponRow);
            }

            weaponsTable.appendChild(weaponsTbody);

            // Append both tables to the resultDiv
            resultDiv.appendChild(operatorTable);
            resultDiv.appendChild(weaponsTable);
        });
}
```

3. Add a parameter to generate() to generate Attacker / Defender


## Easy tasks to do when procrastinating: 
1. Download every weapon's img from ubisoft website; sort by weapon type
2. Same thing for scope, barrel, grip, laser, op icon
3. Add None!

## Actually implement this:
1. ~~Import Flask and create a new Flask application:~~
	```Python
	from flask import Flask
	app = Flask(__name__)
	```
2. ~~Define a route for API endpoint:~~
	```Python
	# Define a route for the /api/random-loadout URL
	# When a client sends a GET request to the /api/random-loadout URL, Flask will call the random_loadout() function and return the response to the client.
	@app.route('/api/random-loadout')
	def random_loadout():
		loadout = operator.get_random_loadout()
		# return the loadout dictionary in JSON format
		return jsonify(loadout)
	```
3. ~~Run flask application:~~
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
